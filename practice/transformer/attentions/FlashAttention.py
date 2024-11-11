import torch
import torch.nn as nn


def default_softmax(x):
    x_softmax = torch.softmax(x, dim=-1)
    print("default softmax: ", x_softmax)
    return x_softmax


def block_online_softmax(x):
    # 将 x 分成块，每个块大小为 3
    x_blocks = torch.split(x, split_size_or_sections=3, dim=0)

    # 计算第一个块的最大值和归一化后的和
    x_block_0 = x_blocks[0]
    x_block_0_max = x_block_0.max()
    x_block_0_sum = torch.exp(x_block_0 - x_block_0_max).sum()

    # 计算第二个块的最大值和归一化后的和
    x_block_1 = x_blocks[1]
    x_block_1_max = x_block_1.max()
    x_block_1_sum = torch.exp(x_block_1 - x_block_1_max).sum()

    # 在线更新：计算两个块的最大值和
    x_block_1_max_update = torch.max(x_block_0_max, x_block_1_max)
    x_block_1_sum_update = x_block_0_sum * torch.exp(x_block_0_max - x_block_1_max_update) + x_block_1_sum * torch.exp(x_block_1_max - x_block_1_max_update)

    # 最后计算整个 x 的在线 Softmax
    x_online_softmax = torch.exp(x - x_block_1_max_update) / x_block_1_sum_update
    print("block online softmax: ", x_online_softmax)
    return x_online_softmax


def multi_block_online_softmax(x):
    # Split `x` into blocks along dimension 0
    x_blocks = torch.split(x, split_size_or_sections=2, dim=0)

    # Calculate max and sum for each block
    M = [block.max() for block in x_blocks]
    L = [torch.exp(block - m).sum() for block, m in zip(x_blocks, M)]

    # Initialize variables to track the running max and normalized sum
    M_old = torch.tensor([0.0], device=x.device, dtype=x.dtype)
    L_old = torch.tensor([0.0], device=x.device, dtype=x.dtype)

    # Online multi-block update of max and sum
    for m, l in zip(M, L):
        M_new = torch.max(m, M_old)
        L_new = L_old * torch.exp(M_old - M_new) + l * torch.exp(m - M_new)

        M_old = M_new
        L_old = L_new

    # Calculate the final softmax
    x_multi_block_online_softmax = torch.exp(x - M_old) / L_old
    print("multi block online softmax:", x_multi_block_online_softmax)
    return x_multi_block_online_softmax


def batch_online_softmax(X_batch):
    print("#######################")
    # Split input batch into two blocks along the second dimension
    d = X_batch.shape[1]
    X_batch_block_0 = X_batch[:, : d // 2]
    X_batch_block_1 = X_batch[:, d // 2 :]

    # Compute max and sum for each block
    X_batch_0_max = X_batch_block_0.max(dim=1, keepdim=True).values
    X_batch_0_sum = torch.exp(X_batch_block_0 - X_batch_0_max).sum(dim=1, keepdim=True)

    X_batch_1_max = X_batch_block_1.max(dim=1, keepdim=True).values
    X_batch_1_sum = torch.exp(X_batch_block_1 - X_batch_1_max).sum(dim=1, keepdim=True)

    # Update max and sum across blocks for each batch element
    # Use the global max across both blocks
    X_batch_max = torch.maximum(X_batch_0_max, X_batch_1_max)
    X_batch_sum = X_batch_0_sum * torch.exp(X_batch_0_max - X_batch_max) + X_batch_1_sum * torch.exp(X_batch_1_max - X_batch_max)

    # Calculate final softmax with the adjusted max and sum
    X_batch_online_softmax = torch.exp(X_batch - X_batch_max) / X_batch_sum
    print("True softmax:", torch.softmax(X_batch, dim=-1))
    print("Batch online softmax:", X_batch_online_softmax)
    return X_batch_online_softmax


class FlashAttention(nn.Module):
    def __init__(self, embed_size, num_heads):
        super().__init__()
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.head_dim = embed_size // num_heads

        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)

        self.Q_BLOCKS_SIZE = 16
        self.KV_BLOCKS_SIZE = 16

    def forward(self, x, use_flash_attention="v1"):
        NEG_INF = torch.tensor(-1e10, device=x.device)
        EPSILON = torch.tensor(1e-6, device=x.device)

        batch_size, seq_len, _ = x.size()

        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.key(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        if use_flash_attention is None:
            attention = torch.matmul(Q, K.transpose(-1, -2)) / (self.head_dim**0.5)
            attention = torch.softmax(attention, dim=-1)
            out = torch.matmul(attention, V).transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)
        elif use_flash_attention == "v1":
            O = torch.zeros_like(Q)
            L = torch.zeros(Q.shape[:-1], device=x.device).unsqueeze(-1)
            M = torch.ones(Q.shape[:-1], device=x.device).unsqueeze(-1) * NEG_INF

            Q_Blocks = torch.split(Q, self.Q_BLOCKS_SIZE, dim=-2)
            K_Blocks = torch.split(K, self.KV_BLOCKS_SIZE, dim=-2)
            V_Blocks = torch.split(V, self.KV_BLOCKS_SIZE, dim=-2)

            O_Blocks = list(torch.split(O, self.Q_BLOCKS_SIZE, dim=-2))
            L_Blocks = list(torch.split(L, self.Q_BLOCKS_SIZE, dim=-2))
            M_Blocks = list(torch.split(M, self.Q_BLOCKS_SIZE, dim=-2))

            for j in range(len(K_Blocks)):
                K_j = K_Blocks[j]
                V_j = V_Blocks[j]
                for i in range(len(Q_Blocks)):
                    Q_i = Q_Blocks[i]
                    S_ij = torch.matmul(Q_i, K_j.transpose(-1, -2)) / (self.head_dim**0.5)
                    m_block_ij, _ = torch.max(S_ij, dim=-1, keepdim=True)  # 当前块的最大值

                    l_block_ij = torch.sum(torch.exp(S_ij - m_block_ij), dim=-1, keepdim=True) + EPSILON

                    li = L_Blocks[i]
                    mi = M_Blocks[i]

                    mi_new = torch.maximum(mi, m_block_ij)

                    li_new = li * torch.exp(mi - mi_new) + l_block_ij * torch.exp(m_block_ij - mi_new)

                    O_Blocks[i] = O_Blocks[i] * (li / li_new) * torch.exp(mi - mi_new) + torch.matmul(torch.exp(S_ij - mi_new), V_j) / li_new
                    L_Blocks[i] = li_new
                    M_Blocks[i] = mi_new

            out = torch.cat(O_Blocks, dim=-2)
            out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)
        elif use_flash_attention == "v2":
            # O = torch.zeros_like(Q)
            # L = torch.zeros(Q.shape[:-1], device=x.device).unsqueeze(-1)
            # M = torch.ones(Q.shape[:-1], device=x.device).unsqueeze(-1) * NEG_INF

            # Q_Blocks = torch.split(Q, self.Q_BLOCKS_SIZE, dim=-2)
            # K_Blocks = torch.split(K, self.KV_BLOCKS_SIZE, dim=-2)
            # V_Blocks = torch.split(V, self.KV_BLOCKS_SIZE, dim=-2)

            # O_Blocks = list(torch.split(O, self.Q_BLOCKS_SIZE, dim=-2))
            # L_Blocks = list(torch.split(L, self.Q_BLOCKS_SIZE, dim=-2))
            # M_Blocks = list(torch.split(M, self.Q_BLOCKS_SIZE, dim=-2))

            # for i in range(len(Q_Blocks)):
            #     Q_i = Q_Blocks[i]

            #     li = L_Blocks[i]
            #     mi = M_Blocks[i]
            #     for j in range(len(K_Blocks)):
            #         K_j = K_Blocks[j]
            #         V_j = V_Blocks[j]

            #         S_ij = torch.matmul(Q_i, K_j.transpose(-1, -2)) / (self.head_dim**0.5)
            #         m_block_ij, _ = torch.max(S_ij, dim=-1, keepdim=True)

            #         l_block_ij = torch.sum(torch.exp(S_ij - m_block_ij), dim=-1, keepdim=True) + EPSILON

            #         mi_new = torch.maximum(mi, m_block_ij)
            #         li_new = li * torch.exp(mi - mi_new) + l_block_ij * torch.exp(m_block_ij - mi_new)

            #         O_Blocks[i] = O_Blocks[i] * (li / li_new) * torch.exp(mi - mi_new) + torch.matmul(torch.exp(S_ij - mi_new), V_j) / li_new

            #         mi = mi_new
            #         li = li_new

            #     # 归一化 O_Blocks[i]
            #     O_Blocks[i] = O_Blocks[i] / li_new
            #     L_Blocks[i] = li_new
            #     M_Blocks[i] = mi_new

            # out = torch.cat(O_Blocks, dim=-2)
            # out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)
            pass

        return self.fc_out(out)


if __name__ == "__main__":
    # x = torch.tensor([-0.3, 0.2, 0.5, 0.7, 0.1, 0.8])
    # default_softmax(x)
    # block_online_softmax(x)
    # multi_block_online_softmax(x)

    # batch_x = torch.randn(2, 6)
    # batch_online_softmax(batch_x)

    flash_attention_model = FlashAttention(64, 8)
    input_tensor = torch.randn((512, 128, 64))

    result = flash_attention_model(input_tensor, use_flash_attention=None)
    flash1_result = flash_attention_model(input_tensor, use_flash_attention="v1")
    flash2_result = flash_attention_model(input_tensor, use_flash_attention="v2")

    # 检查 FlashAttention 的输出是否与 MultiHeadAttention 的输出一致
    print(torch.allclose(result, flash1_result, atol=1e-6))
    print(torch.allclose(result, flash2_result, atol=1e-6))
