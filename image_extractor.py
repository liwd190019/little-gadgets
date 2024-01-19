'''
randomly select x images from one folder and transfer them to another.
'''
import os, shutil, random, sys
print('this script can extract images from folders and change its name format to <class>_<index>.jpg')
# print('press y/n to continue')
# while True:
#   key = keyboard.wait()
#   if key == 'y':
#     break
#   elif key == 'n':
#     sys.exit()
#   else:
#     print('wrong input. input y/n')
ori_dir = input('please input the current directory\'s path: ')
tar_dir = input('please input the target directory\'s path: ')

print("each my_domain* has 340 images, so I decided to extract 50 pages from each of them. Since there are 6 classes, I will have 300 images. So in cifar-10, I want to extract 300 images")
print("also, my resized domain net dataset has 340 pages. I will extract 300 pages from it")

num_trans = int(input('please input how many images you want to transfer: '))

if not os.path.isdir(tar_dir):
  os.makedirs(tar_dir)
cur_path_dirs = os.listdir(ori_dir)

# for k in cur_path_dirs:
# src_dir_now = os.path.join(ori_dir, k)
src_dir_now = ori_dir
tar_dir_now = tar_dir
# if os.path.isdir(src_dir_now):
  # continue
# old_filenames = random.sample(os.listdir(src_dir_now), num_trans)
old_filenames = random.sample([items for items in os.listdir(src_dir_now) if not os.path.isdir(os.path.join(src_dir_now, items))], num_trans)
for fname in old_filenames:
  srcpath = os.path.join(src_dir_now, fname)
  destpath = os.path.join(tar_dir_now, fname)
  shutil.copyfile(srcpath, destpath)
# for fname in old_filenames:
# add file name adjustment
# _, sub_fname = fname.rsplit("_", 1)
# new_fname = k + '_' + sub_fname
# srcpath = os.path.join(src_dir_now, fname)
# destpath = os.path.join(tar_dir_now, new_fname)
# shutil.copyfile(srcpath, destpath)
