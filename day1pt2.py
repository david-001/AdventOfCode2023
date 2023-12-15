import re

# Specify the file path
file_path = 'day1pt2.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  lines = file.readlines()

# Given strings
strings = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

# Specify the lists of words and digits
word_list = ['oneight', 'one', 'twone', 'two', 'threeight', 'three', 'four', 'fiveight', 'five', 'six', 'sevenine', 'seven', 'eighthree', 'eightwo', 'eight', 'nineight', 'nine']

sum = 0
# Find first and last words or digits for each line
for line in lines:
    # Use a regular expression to find words or digits in the line
    words_or_digits = re.findall(r'(?:' + '|'.join(word_list) + r')|\d', line)    

    number = {
      'one':'1',
      'two':'2', 
      'three':'3', 
      'four':'4',
      'five':'5',
      'six':'6',
      'seven':'7',
      'eight':'8',
      'nine':'9'
    }
    
    if words_or_digits[0]=="oneight":
      words_or_digits[0]="one" 
    if words_or_digits[0]=="twone":
      words_or_digits[0]="two"
    if words_or_digits[0]=="threeight":
      words_or_digits[0]="three"  
    if words_or_digits[0]=="fiveight":
      words_or_digits[0]="five"
    if words_or_digits[0]=="sevenine":
      words_or_digits[0]="seven"  
    if words_or_digits[0]=="eighthree":
      words_or_digits[0]="eight"
    if words_or_digits[0]=="eightwo":
      words_or_digits[0]="eight" 
    if words_or_digits[0]=="nineight":
      words_or_digits[0]="nine" 


    if words_or_digits[-1]=="oneight":
      words_or_digits[-1]="eight" 
    if words_or_digits[-1]=="twone":
      words_or_digits[-1]="one"
    if words_or_digits[-1]=="threeight":
      words_or_digits[-1]="eight"  
    if words_or_digits[-1]=="fiveight":
      words_or_digits[-1]="eight"
    if words_or_digits[-1]=="sevenine":
      words_or_digits[-1]="nine"  
    if words_or_digits[-1]=="eighthree":
      words_or_digits[-1]="three"
    if words_or_digits[-1]=="eightwo":
      words_or_digits[-1]="two"  
    if words_or_digits[-1]=="nineight":
      words_or_digits[-1]="eight"   

    # Extract the first and last words or digits if found    
    first_item = words_or_digits[0] if words_or_digits else None
    last_item = words_or_digits[-1] if words_or_digits else None

    if words_or_digits[0] in number:
      first_item = number[words_or_digits[0]]

    if words_or_digits[-1] in number:
      last_item = number[words_or_digits[-1]]

    # Combine the first and last digits
    combined_digits = None  
    combined_digits = int(first_item + last_item)  
    print(combined_digits)

    sum += combined_digits

print(sum)

# Your puzzle answer was 56017.