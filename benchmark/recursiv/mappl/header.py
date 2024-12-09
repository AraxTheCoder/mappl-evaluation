import torch
from functools import *

import sys
sys.setrecursionlimit(32767)

TensorIntBool = torch.tensor([0, 1], dtype=torch.int)
max_tries=2**256

@cache
def cached_partial(func, *args):
    return partial(func, *args)

@cache
def auto_invoke_partial(func, *args, **kwargs):
    if not args and not kwargs: 
        return func()  
    else:
        return partial(func, *args, **kwargs) 

def LogSumExp(f, lo, hi):
    int_lo = int(lo)
    int_hi = int(hi)
    log_probs = torch.tensor([f(z) for z in range(int_lo, int_hi+1)])
    return torch.logsumexp(log_probs, dim=-1)

# @cache
# https://github.com/python/cpython/blob/326f0ba1c5dda1d9613dbba11ea2470654b0d9c8/Lib/functools.py#L652

def float_tensor(d):
    return torch.tensor(d, dtype=torch.float)

def halt(*args):
    return None

def halt_transformed(*args):
    return torch.zeros(1)
