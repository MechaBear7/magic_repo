import torch
import torch.nn as nn


class RMSNorm(torch.nn.Module):
    def __init__(self, dim: int, eps: float = 1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def _norm(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        # 这里的 x.float() 确保将 tensor 转换为 float32 形式，提供足够的精度来计算平方和均值，避免由于数据类型导致的数值不稳定的问题
        # 后面的 type_as 将 tensor 重新转为原数据类型，保持类型一致
        output = self._norm(x.float()).type_as(x)
        return output * self.weight  # 进行逐元素的缩放
