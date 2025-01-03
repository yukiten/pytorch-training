import torch
import numpy as np

if __name__=="__main__":
    data = np.array([
        [[85, 78], [67, 82], [92, 88], [75, 70], [60, 64]],
        [[70, 68], [77, 72], [85, 90], [60, 65], [78, 76]],
        [[80, 84], [88, 87], [66, 68], [72, 73], [64, 60]]
    ])

    # problem 1
    _tensor = torch.tensor(data, dtype=float)
    print("===== problem 1 =====")
    print(repr(_tensor.size()))
    
    # problem 2
    permuted_tensor = torch.permute(_tensor, (2, 0, 1))
    print("===== problem 2 =====")
    print(repr(permuted_tensor))
    print(repr(permuted_tensor.size()))

    # problem 3
    sum_permuted_tensor = permuted_tensor.sum(dim=0)
    print("===== problem 3 =====")
    print(repr(sum_permuted_tensor))

    # problem 4
    mean_method1 = sum_permuted_tensor.mean(dim=1)
    print("===== problem 4 =====")
    print(mean_method1)

    # problem 5
    tmp_sum = sum_permuted_tensor.sum(dim=1)
    num_classmates = sum_permuted_tensor.size(dim=1)
    mean_method2 = tmp_sum / num_classmates
    print("===== problem 5 =====")
    print(mean_method2)
