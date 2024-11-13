import torch
import torch.nn as nn


class RMSNorm(nn.Module):
    def __init__(self, embed_size, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(embed_size))

    def norm(self, x):
        x = x * torch.rsqrt(x.pow(2).mean(dim=-1, keepdim=True) + self.eps)
        return x

    def forward(self, x):
        x = self.norm(x.float()).type_as(x)
        return self.weight * x
