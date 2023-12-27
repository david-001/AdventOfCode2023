import re

# Specify the file path
file_path = 'day9pt2.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]

# matrix = '''0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45'''

# numbers = [re.findall(r'-?\d+', line) for line in matrix.split('\n')]
numbers = [re.findall(r'-?\d+', line) for line in matrix]
numbers = [[int(num) for num in nums] for nums in numbers]

def diff(arr):
  ans = arr[-1] 
  for i in range(len(arr)):    
    if i < len(arr)-1:      
      ans = arr[len(arr)-2-i] - ans    
  return ans


numbers_2_add = []
for i in range(len(numbers)):    
  differences = numbers[i]   
  new_differences = []
  nums_2_rem = []
  # while zeroes < zeroes_len:
  while len(differences)>1:
    for j in range(len(differences)):
      if j<len(differences)-1:    
        new_differences.append(differences[j+1]-differences[j])        
    differences = new_differences    
    new_differences = []
    nums_2_rem.append(differences[0])
    # print(differences)
    # print(nums_2_rem)    
  numbers_2_add.append(numbers[i][0]-diff(nums_2_rem))  
  # print(diff(nums_2_rem))
  # print('---------------------')
  

sum = sum(numbers_2_add)
print(sum)

# 