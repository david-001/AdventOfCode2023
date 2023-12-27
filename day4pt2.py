import re
from collections import Counter
import pickle

# Specify the file path
file_path = 'day4pt2.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  text = file.readlines()

# text = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

# Use regular expression to extract numbers on the left and right side of '|'
left_numbers = [re.findall(r'\d+', line.split('|')[0]) for line in text]
right_numbers = [re.findall(r'\d+', line.split('|')[1]) for line in text]

# Convert the strings to integers
left_numbers = [[int(num) for num in nums] for nums in left_numbers]
right_numbers = [[int(num) for num in nums] for nums in right_numbers]

sum = 0
cards = []
for i in range(len(right_numbers)):
    cards.append(1)
    sum += 1


for i in range(len(right_numbers)):    
    # Convert arrays to sets and find the common elements. left numbers drop 1st number because it corresponds to Card number
    # print('left',left_numbers[i])
    common_elements = set(left_numbers[i][1:]) & set(right_numbers[i])    

    # Convert the result back to a list if needed
    common_elements_list = list(common_elements)
    
    tmp = list(range(left_numbers[i][0]+1, left_numbers[i][0]+1 + len(common_elements_list)))       
    
    for j in range(0,cards[i]):    
        for t in tmp:
            # print(t)   
            cards[t-1] += 1
            sum += 1
    
    # print('cards',cards) 
    # print(i+1)

print(sum)  


# Your puzzle answer was 8736438.