import torch
from typing import Tuple


def precompute_freqs_cis(dim: int, end: int, theta: float = 10000.0):
    freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))  # 计算得到 0, 2, 4, ..., dim-2 的频率
    t = torch.arange(end, device=freqs.device, dtype=torch.float32)  # 生成一个从 0 到 end-1 的数组，表示时间序列
    freqs = torch.outer(t, freqs)  # 计算 t 和 freqs 的外积，得到一个 (end, dim // 2) 的矩阵
    freqs_cis = torch.polar(torch.ones_like(freqs), freqs)  # 将频率转换为复数形式，得到一个 (end, dim // 2) 的复数矩阵，用于旋转编码
    return freqs_cis


def reshape_for_broadcast(freqs_cis: torch.Tensor, x: torch.Tensor):
    ndim = x.ndim
    assert 0 <= 1 < ndim
    shape = [d if i == 1 or i == ndim - 1 else 1 for i, d in enumerate(x.shape)]
    return freqs_cis.view(*shape)


def apply_rotary_emb(
    xq: torch.Tensor,
    xk: torch.Tensor,
    freqs_cis: torch.Tensor,
) -> Tuple[torch.Tensor, torch.Tensor]:
    xq_ = torch.view_as_complex(xq.float().reshape(*xq.shape[:-1], -1, 2))  # (32, 1024, 1, 64)
    xk_ = torch.view_as_complex(xk.float().reshape(*xk.shape[:-1], -1, 2))  # (32, 1024, 1, 64)
    freqs_cis = reshape_for_broadcast(freqs_cis, xq_)  # （1, 1024, 1, 64）
    xq_out = torch.view_as_real(xq_ * freqs_cis).flatten(3)
    xk_out = torch.view_as_real(xk_ * freqs_cis).flatten(3)
    return xq_out.type_as(xq), xk_out.type_as(xk)


max_len = 1024
batch_size, seq_len, embed_dim = 32, 1024, 128

freqs_cis = precompute_freqs_cis(embed_dim, max_len)  # (1024, 64)

Q = torch.randn(batch_size, seq_len, 1, embed_dim)  # (32, 1024, 1, 128)
K = torch.randn(batch_size, seq_len, 1, embed_dim)  # (32, 1024, 1, 128)

result = apply_rotary_emb(Q, K, freqs_cis)
