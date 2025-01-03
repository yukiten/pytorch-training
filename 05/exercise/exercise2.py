import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset

class MyDataset(Dataset):
    
    def __init__(self, dataset_dir):
        dir_path = Path(dataset_dir).resolve()
        dir_list = list(dir_path.glob("*"))
        self.file_list = []
        for dir in dir_list:
            file_path_list = list(dir.glob("*"))
            self.file_list += file_path_list
            
    def __len__(self):
        return len(self.file_list)
    
    def __getitem__(self, idx):
        img_path = self.file_list[idx]
        img = Image.open(img_path)
        
        return img
    
if __name__ == "__main__":
    
    my_dataset = MyDataset("./data")
    print("===== problem1.1 =====")
    print(len(my_dataset))
    print("===== problem1.2 =====") 
    print(my_dataset[0].size)
    