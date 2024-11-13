import torch


def precompute_freqs_cis(embed_size, end, theta=1000):
    freqs = 1.0 / (theta ** torch.arange(0, embed_size, 2)[: embed_size // 2].float() / embed_size)
    t = torch.arange(end, device=freqs.device, dtype=torch.float32)
    freqs = torch.outer(t, freqs)
    freqs_cis = torch.polar(torch.ones_like(freqs), freqs)
    return freqs_cis  # (end, embed_size // 2)


def apply_rotary_emb(xq, xk, freqs_cis):
    xq = torch.view_as_complex(xq.float().reshape(*xq.shape[:-1], -1, 2))
    xk = torch.view_as_complex(xk.float().reshape(*xk.shape[:-1], -1, 2))

    xq = torch.view_as_real(xq * freqs_cis).flatten(3)
    xk = torch.view_as_real(xk * freqs_cis).flatten(3)

    return xq, xk


if __name__ == "__main__":
    max_len = 2048
    batch_size, seq_len, num_heads, head_dim = 128, 512, 8, 64

    freqs_cis = precompute_freqs_cis(head_dim, max_len * 2)
    freqs_cis = freqs_cis[:seq_len]
    freqs_cis = freqs_cis.reshape(1, freqs_cis.size(0), 1, freqs_cis.size(1))

    Q = torch.ones(batch_size, seq_len, num_heads, head_dim)
    K = torch.ones(batch_size, seq_len, num_heads, head_dim)

    Q, K = apply_rotary_emb(Q, K, freqs_cis)

    print(K)
