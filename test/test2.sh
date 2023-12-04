#!/bin/bash

# Declare a static Array
arr=("Jayesh" "Shivang" "hello" "rishabh" "Vipul" "Nishtan")

# Count the length of a particular element in the array
element_length=${#arr[2]}
echo "Length of element at index 2: $element_length"
echo "arr[2] = ${arr[2]}"

# Count the length of the entire array
array_length=${#arr[@]}
echo "Length of the array: $array_length"

# Search in the array
search_result=$(echo "${arr[@]}" | grep -c "Jayesh")
echo "Search result for 'Jayesh': $search_result"

# Search and replace in the array
for ((i=0; i<${#arr[@]}; i++)); do
    if [ "${arr[i]}" == "Shivang" ]; then
        new_arr[i]="SHIVANG"
    else
        new_arr[i]=${arr[i]}
    fi
done

echo "Array after search & replace: ${new_arr[@]}"

# another version of Search and replace in the array
# replaced_elements=$(echo "${arr[@]}/Shivang/SHIVANG")
replaced_elements=echo 
echo "Array After Search & replace: ${replaced_elements[@]}"


# Delete an element in the array (index 3)
unset arr[3]

echo "Array after deletion: ${arr[@]}"
