import torch
import torch.nn as nn


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, num_heads):
        super().__init__()
        assert embed_size % num_heads == 0, "embed_size must be divised by num_heads."
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.head_dim = embed_size // self.num_heads

        # Linear Layers for Query, Key, Value
        self.query = nn.Linear(self.embed_size, self.embed_size)
        self.key = nn.Linear(self.embed_size, self.embed_size)
        self.value = nn.Linear(self.embed_size, self.embed_size)

        # Final Layer for concatenating attention
        self.fc_out = nn.Linear(self.embed_size, self.embed_size)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()

        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.key(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        attention = torch.matmul(Q, K.transpose(-1, -2)) / (self.head_dim**0.5)
        attention = torch.softmax(attention, dim=-1)

        out = torch.matmul(attention, V)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)

        return self.fc_out(out)


class MultiQueryAttention(nn.Module):
    def __init__(self, embed_size, num_heads):
        super().__init__()
        assert embed_size % num_heads == 0

        self.embed_size = embed_size
        self.num_heads = num_heads
        self.head_dim = embed_size // num_heads

        # Linear Layer for Query(Multi-Query), Shared Key and Value
        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, self.head_dim)
        self.value = nn.Linear(embed_size, self.head_dim)

        # Final Linear Layer for output
        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()

        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.key(x).unsqueeze(1)
        V = self.value(x).unsqueeze(1)

        attention = torch.matmul(Q, K.transpose(-1, -2)) / (self.head_dim**0.5)
        attention = torch.softmax(attention, dim=-1)

        out = torch.matmul(attention, V)
        out = out.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_size)

        return self.fc_out(out)


class GroupQueryAttention(nn.Module):
    def __init__(self, embed_size, num_heads, num_groups):
        super().__init__()
        assert embed_size % num_heads == 0
        assert num_heads % num_groups == 0

        self.embed_size = embed_size
        self.num_heads = num_heads
        self.num_groups = num_groups
        self.head_dim = embed_size // num_heads
        self.head_per_group = num_heads // num_groups

        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, self.head_per_group * self.head_dim)
        self.value = nn.Linear(embed_size, self.head_per_group * self.head_dim)

        self.fc_out = nn.Linear(embed_size, embed_size)

    def forward(self, x):
        batch_size, seq_len, _ = x.size()

        # Multi-Head Query
        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        # Grouped Key and Value
        K = self.key(x).view(batch_size, seq_len, self.head_per_group, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_len, self.head_per_group, self.head_dim).transpose(1, 2)

        # Split Queries into Groups and Compute Attention within each group
        grouped_out = []
        for group_idx in range(self.num_groups):
            q_group = Q[:, group_idx * self.head_per_group : (group_idx + 1) * self.head_per_group]
            k_group = K[:, group_idx].unsqueeze(1)
            v_group = V[:, group_idx].unsqueeze(1)

            attention = torch.matmul(q_group, k_group.transpose(-1, -2)) / (self.head_dim**0.5)
            attention = torch.softmax(attention, dim=-1)

            out = torch.matmul(attention, v_group).transpose(1, 2)
            grouped_out.append(out)

        grouped_out = torch.cat(grouped_out, dim=-1).view(batch_size, seq_len, self.embed_size)

        return self.fc_out(grouped_out)


if __name__ == "__main__":
    mock_tensor = torch.randn((512, 1024, 64))

    GQA = GroupQueryAttention(64, 8, 2)

    result = GQA(mock_tensor)
    print(result)
