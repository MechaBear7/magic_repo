        O = torch.zeros_like(Q)
            L = torch.zeros(Q.shape[:-1], device=x.device).unsqueeze(-1)
            M = torch.ones(Q.shape[:-1], device=x.device).unsqueeze(-1) * NEG_INF

            Q_Blocks = torch.split(Q, self.Q_BLOCKS_SIZE, dim=-2)
            K_Blocks = torch.split(K, self.KV_BLOCKS_SIZE, dim=-2)
            V_Blocks = torch.split(V, self.KV_BLOCKS_SIZE, dim=-2)

            O_Blocks = list(torch.split(O, self.Q_BLOCKS_SIZE, dim=-2))
            L_Blocks = list(torch.split(L, self.Q_BLOCKS_SIZE, dim=-2))
            M_Blocks = list(torch.split(M, self.Q_BLOCKS_SIZE, dim=-2))

            for i in range(len(Q_Blocks)):
                Q_i = Q_Blocks[i]

                li = L_Blocks[i]
                mi = M_Blocks[i]
                for j in range(len(K_Blocks)):
                    K_j = K_Blocks[j]
                    V_j = V_Blocks[j]

                    S_ij = torch.matmul(Q_i, K_j.transpose(-1, -2)) / (self.head_dim**0.5)
                    m_block_ij, _ = torch.max(S_ij, dim=-1, keepdim=True)

                    l_block_ij = torch.sum(torch.exp(S_ij - m_block_ij), dim=-1, keepdim=True) + EPSILON

                    mi_new = torch.maximum(mi, m_block_ij)
                    li_new = li * torch.exp(mi - mi_new) + l_block_ij

                    # 更新 O_Blocks[i]
                    O_Blocks[i] = O_Blocks[i] * (li / li_new) * torch.exp(mi - mi_new) + torch.matmul(torch.exp(S_ij - mi_new), V_j) / li_new

                    mi = mi_new
                    li = li_new

                # 归一化 O_Blocks[i]
                O_Blocks[i] = O_Blocks[i] / li_new
                L_Blocks[i] = li_new
                M_Blocks[i] = mi_new

            out = torch.cat(O_Blocks, dim=-2)
            out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)