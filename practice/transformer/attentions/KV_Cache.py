# author: xiaodongguaAIGC
# KV-Cache + Generation + decoder

import torch
import torch.nn as nn


class MultiHeadAttentionWithKVCache(nn.Module):
    def __init__(self, embed_size, num_heads):
        super().__init__()
        self.embed_size = embed_size
        self.num_heads = num_heads
        self.head_dim = embed_size // num_heads

        assert embed_size % num_heads == 0, "Embed size must be divisible by num_heads."

        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)
        self.fc_out = nn.Linear(embed_size, embed_size)

        self.cache_k = None
        self.cache_v = None

    def forward(self, x, use_cache=True):
        batch_size, seq_len, _ = x.size()

        Q = self.query(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.key(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.value(x).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        # Concatenate cached K and V if they exist and caching is enabled
        if use_cache and self.cache_k is not None and self.cache_v is not None:
            K = torch.cat([self.cache_k, K], dim=2)
            V = torch.cat([self.cache_v, V], dim=2)

        # Update caches if use_cache is enabled
        if use_cache:
            self.cache_k = K.detach()
            self.cache_v = V.detach()

        attention = torch.matmul(Q, K.transpose(-1, -2)) / (self.head_dim**0.5)
        attention = torch.softmax(attention, dim=-1)

        out = torch.matmul(attention, V).transpose(1, 2).contiguous()
        out = out.view(batch_size, seq_len, self.embed_size)

        return self.fc_out(out)

    def reset_cache(self):
        """Clears the cache."""
        self.cache_k = None
        self.cache_v = None


if __name__ == "__main__":
    embed_size = 6
    num_heads = 2
    input_tensor = torch.randn(3, 2, embed_size)
    mha_kv_cache = MultiHeadAttentionWithKVCache(embed_size, num_heads)

    for i in range(5):
        print(f"Generating token {i}... input shape: {input_tensor.shape}")
        output = mha_kv_cache(input_tensor)
        print("Output shape:", output.shape)
        new_token_tensor = torch.randn(3, 1, embed_size)
        input_tensor = new_token_tensor
