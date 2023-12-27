import re

# Specify the file path
file_path = 'day4pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  lines = file.readlines()

# text = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# text = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

# # Use regular expression to extract numbers on the left side of '|'
# left_numbers = [re.findall(r'\d+', line.split('|')[0]) for line in text.split('\n')]
# right_numbers = [re.findall(r'\d+', line.split('|')[1]) for line in text.split('\n')]
# print('right: ',right_numbers)

left_numbers = [re.findall(r'\d+', line.split('|')[0]) for line in lines]
right_numbers = [re.findall(r'\d+', line.split('|')[1]) for line in lines]

# Convert the strings to integers
left_numbers = [[int(num) for num in nums] for nums in left_numbers]
right_numbers = [[int(num) for num in nums] for nums in right_numbers]


total_pts = 0
# Print the result
for i,j in enumerate(right_numbers):    
    # Convert arrays to sets and find the common elements. left numbers drop 1st number because it corresponds to Card number
    common_elements = set(left_numbers[i][1:]) & set(right_numbers[i])

    # Convert the result back to a list if needed
    common_elements_list = list(common_elements)

    # Print the common elements
    # print("Common elements:", common_elements_list)

    if len(common_elements_list) > 0:
      pt = 2 ** (len(common_elements_list)-1)      
    else:
      pt = 0  
    # print(pt)
    total_pts += pt

print(total_pts)

# Your puzzle answer was 24542.