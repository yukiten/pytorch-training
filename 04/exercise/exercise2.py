import torch
from torch import nn

if __name__=="__main__":
    
    _in = torch.ones((32, 1024))
    print("===== problem 1 =====")
    print(repr(_in.size()))
    
    fc = nn.Linear(1024, 256)
    out = fc(_in)
    print("===== problem 2 =====")
    print(repr(out.size()))
    
    fc2 = nn.Linear(1024, 2048)
    print("===== problem 3 =====")
    print(repr(fc2(_in).size()))
    
    print("===== appendix =====")
    print(repr(out.view(-1, 16, 16).size()))