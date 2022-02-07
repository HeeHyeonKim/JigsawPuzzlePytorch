import os
import cv2
from tqdm import tqdm

data_dir_path = "D:\\ILSVRC2012"
dst_dir_path = "./new"
dir_list = os.listdir(data_dir_path)

for dir in tqdm(dir_list):
    dir_path = os.path.join(data_dir_path,dir)
    img_list = os.listdir(dir_path)
    for img in img_list:
        img_path = os.path.join(dir_path,img)
        img_arr = cv2.imread(img_path)
        img_save_path = os.path.join(dst_dir_path,img)
        cv2.imwrite(img_save_path,img_arr)