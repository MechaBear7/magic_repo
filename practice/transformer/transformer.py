import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_seq_len=5000):
        super().__init__()
        pe = torch.zeros(max_seq_len, d_model)
        position = torch.arange(0, max_seq_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x):
        x = x + self.pe[:, : x.size(1)]
        return x


class RMSNorm(nn.Module):
    def __init__(self, embed_dim, eps=1e-6):
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(embed_dim))

    def forward(self, x):
        normed_x = x * torch.rsqrt(x.pow(2).mean(dim=-1, keepdim=True) + self.eps)
        return self.weight * normed_x


class MuiltiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        assert self.embed_dim % self.embed_dim == 0, "embed_dim must be divised by num_heads."

        self.head_dim = self.embed_dim // self.num_heads

        self.query = nn.Linear(self.embed_dim, self.embed_dim)
        self.key = nn.Linear(self.embed_dim, self.embed_dim)
        self.value = nn.Linear(self.embed_dim, self.embed_dim)

        self.fc_out = nn.Linear(self.embed_dim, self.embed_dim)

    def forward(self, x, mask=None):
        batch_size, seq_len, _ = x.size()

        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.key(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        attention = torch.matmul(Q, K.transpose(-1, -2)) / (self.head_dim**0.5)

        if mask is not None:
            attention = attention.masked_fill(mask == 0, -1e9)

        attention = torch.softmax(attention, dim=-1)
        out = torch.matmul(attention, V)
        out = out.transpose(1, 2).contiguous().reshape(batch_size, seq_len, -1)

        self.fc_out(out)


class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(d_ff, d_model)

    def forward(self, x):
        x = self.linear1(x)
        x = self.dropout(F.silu(x))
        x = self.linear2(x)
        return x


class TransformerBlock(nn.Module):
    def __init__(self, args, layer_id):
        super().__init__()
        self.args = args
        self.layer_id = layer_id

        self.attention = MuiltiHeadAttention(self.args.d_model, self.args.n_heads)
        self.ffn = FeedForward(self.args.d_model, self.args.d_ff, self.args.dropout)

        self.attention_norm = RMSNorm(self.args.d_model, eps=1e-6)
        self.ffn_norm = RMSNorm(self.args.d_model, eps=1e-6)

        self.dropout1 = nn.Dropout(self.args.dropout)
        self.dropout2 = nn.Dropout(self.args.dropout)

    def forward(self, x, mask=None):
        h = x + self.dropout1(self.attention_norm(self.attention(x, mask)))
        out = h + self.dropout2(self.ffn_norm(self.ffn(h)))
        return out


class Transformer(nn.Module):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.pos_encoder = PositionalEncoding(args.d_model)
        self.layers = nn.ModuleList([TransformerBlock(args, idx) for idx in range(args.n_layers)])
        self.norm = RMSNorm(args.d_model, eps=1e-6)
        self.out = nn.Linear(args.d_model, args.output_dim)

    def forward(self, x, mask):
        x = self.pos_encoder(x)
        for layer in self.layers:
            x = layer(x, mask)
        x = self.norm(x)
        out = self.out(x)
        return out
