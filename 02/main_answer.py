import numpy as np

data = np.array([
 [[65, 70], [56, 80], [78, 68], [90, 85], [60, 75]],
 [[70, 75], [54, 88], [82, 64], [88, 83], [58, 78]],
 [[67, 72], [52, 82], [80, 66], [86, 80], [59, 74]]])

print("Data shape:", data.shape)
print(np.mean(data, axis=0))
print("全クラスの番号3番目の学生の中で2科目目の最高得点",np.max(data[:,2, 1]))
print("各科目で一番点数が高い人と低い人の点差", np.max(np.max(data, axis=1), axis=0) - np.min(np.min(data, axis=1), axis=0))
print("各クラスの1科目目が80点以上の人数", np.sum(data[:, :, 0] >= 80, axis=1))
print("2科目の合計得点が135点を超えている人数", np.sum(np.sum(data, axis = 2) > 135))
