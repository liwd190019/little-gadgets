
#! usr/bin/bash

# a small script that can output randomized A, B, C, D, E, F or their binary, decimal 
# numbers.
# this script is intended to help me memorize the decimal form and binary form of A, B, C, D, E, F

if [ $# -eq 0 ]
then 
  # user does not input file path
  # default file path is the current directory
  file="memorize_hex_dec_bin.md"
  echo "Add fist item into file" > $file
  echo "append second item into file" >> $file
elif [ $# -eq 1 ]
then
  file="$1/memorize_hex_dec_bin.md"
  echo "adding first" > $file
  echo "append second" >> $file
else
  echo "error!"
  exit 64
fi

cat $file