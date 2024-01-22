'''
1. iterate through all images from my_imags_3000 and my_imgs
2. add prefix: `cifar-10-batches-py/imgs/` to the images
3. find their labels in label.json, then add the label as prefix.
'''
import os, shutil, json
import cv2

ori_dir = input('please input the current directory\'s path: ')
tar_dir = input('please input the target directory\'s path: ')
# json_ori = input('please input the json file name: ')
# ori_dir = "my_imgs_class"
# tar_dir = "my_imgs_class_upsampled"
# json_ori = "label.json"
# json_open = open(json_ori)
# json_file = json.load(json_open)
# class_list = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

if not os.path.isdir(tar_dir):
  os.makedirs(tar_dir)
cur_path_dirs = os.listdir(ori_dir)

for k in cur_path_dirs:
  src_dir_now = os.path.join(ori_dir, k)
  if os.path.isdir(src_dir_now):
    continue
  img = cv2.imread(src_dir_now)
  upscaled_img = cv2.resize(img, (256, 256))
  output_path = os.path.join(tar_dir, k)
  cv2.imwrite(output_path, upscaled_img)
  # break
  # index_name = "cifar-10-batches-py/imgs/"+k
  # k_class_num = json_file[index_name]
  # new_fname = class_list[k_class_num] + '_' + k
  # # srcpath = os.path.join(src_dir_now, k)
  # destpath = os.path.join(tar_dir, new_fname)
  # print(f'destpath is {destpath}')
  # print(f'srcpath is {srcpath}')
  # break
  # # shutil.copyfile(src_dir_now, destpath)
  
