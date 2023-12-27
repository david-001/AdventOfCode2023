import re

# Specify the file path
file_path = 'day2pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  lines = file.readlines()

# Given strings
input_strings = [
  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def count_color(color_to_count,input_string):
  # Create a regular expression pattern for the color count
  pattern = re.compile(r'(\d+)\s+' + re.escape(color_to_count))

  # Find all matches in the string
  matches = pattern.findall(input_string)

  # Convert matches to integers and find the maximum count
  max_count = max(map(int, matches), default=0)
  return max_count

id = 1
count = 0
for input_string in lines:
  red_count = count_color('red',input_string)
  green_count = count_color('green',input_string)
  blue_count = count_color('blue',input_string)
  # print(red_count,green_count,blue_count)
  if red_count<=12 and green_count<=13 and blue_count<=14:
    # print(id)
    count += id
  id += 1

print(count)

# Your puzzle answer was 1734.