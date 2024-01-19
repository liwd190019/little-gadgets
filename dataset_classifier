import os, shutil

from_dir = input('input where your current directory is: ')
# to_dir = input('input where you want to send them to')

print("this script can help you extract files that has the same name and classify \
        them and put them in a same directory")

cur_path_dirs = os.listdir(from_dir)
print(f'cur_path_dirs is \n{cur_path_dirs}')
"""
make directories -> ask name of the directory -> mv files to the directory
split file names, those prefix are the same are classified as one class
then give them a new name, the name that uses their postfix split.
"""
for k in cur_path_dirs:
  pre, post = k.rsplit("_", 1)
  # check if the directory named pre exists
  # cur_dirs = os.listdir(from_dir)
  # if pre in cur_dirs:
  pre = os.path.join(from_dir, pre)
  if not os.path.isdir(pre):
    os.makedirs(pre)
  src_path = os.path.join(from_dir, k)
  shutil.move(f"./{src_path}", f"{pre}/{post}")
  
"""
now write some new name
based on the directories in the current path
"""
# print(f"from_dir is {from_dir}")
# for (root, dirs, files) in os.walk(from_dir):
#   print(f"root is {root}")
#   print(f"dirs is {dirs}")
#   print(f"files is {files}")
#   break

for (root, dirs, files) in os.walk(from_dir):
  num_dirs = len(dirs) # get the number of folders in current path
  for dir in dirs:
    print(f"the name of the current directory is {dir}")
    new_name = input("please enter the new name, if you don't want to change it\
        , just press Enter/Return, write None to skip, write Stop is terminate: ")
    if new_name == "None":
      continue
    if new_name == "Stop":
      break
    src_path = os.path.join(from_dir, dir)
    shutil.move(src_path, f"{from_dir}/{new_name}")
  break
