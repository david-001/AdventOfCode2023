import re

# Specify the file path
file_path = 'day1pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  lines = file.readlines()

def extract_first_and_last_digits(line):
  # Use a regular expression to find all digits in the line
  digits = re.findall(r'\d', line)

  # Extract the first and last digits
  first_digit = digits[0] if digits else None
  last_digit = digits[-1] if digits else None

  return first_digit, last_digit

# Given strings
strings = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

sum = 0
# Extract first and last digits from each line
for line in lines:
  first_digit, last_digit = extract_first_and_last_digits(line)
  # Combine the first and last digits
  combined_digits = None  
  combined_digits = int(first_digit + last_digit)
  sum += combined_digits

print(sum)

# Your puzzle answer was 56506.
  