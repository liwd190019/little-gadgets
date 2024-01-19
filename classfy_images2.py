'''
randomly choose x images from all folders under the path A, then 
transfer them to folders under the path B while keeping folders' names
unchanged
'''
import os, shutil, random
ori_dir = input('please input the current directory\'s path: ')
tar_dir = input('please input the target directory\'s path: ')
num_trans = int(input('please input how many images you want to transfer: '))

if not os.path.isdir(tar_dir):
  os.makedirs(tar_dir)
cur_path_dirs = os.listdir(ori_dir)

for k in cur_path_dirs:
  src_dir_now = os.path.join(ori_dir, k)
  tar_dir_now = os.path.join(tar_dir, k)
  if not os.path.isdir(tar_dir_now):
    os.makedirs(tar_dir_now)
  filenames = random.sample(os.listdir(src_dir_now), num_trans)
  for fname in filenames:
    srcpath = os.path.join(src_dir_now, fname)
    destpath = os.path.join(tar_dir_now, fname)
    shutil.copyfile(srcpath, destpath)
