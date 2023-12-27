## ----------------------------------------------------------------------
import re

# Specify the file path
file_path = 'day3pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]


# # Split the string into a list of strings using newline characters
# matrix = lines.split('\n')

# # Remove any empty strings from the list
# matrix = list(filter(None, matrix))  

class PartNumber:
  def __init__(self, number,start,end):
    self.number = number
    self.start = start
    self.end = end

# matrix = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
# matrix = matrix.split('\n')

# matrix = """46+-.114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
# matrix = matrix.split('\n')


# matrix = [
#     "467.114...",
#     "...*..#..",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598.."
# ]

part_numbers = []

def get_indices_of_numbers(matrix):
    indices = []

    for row_idx, row in enumerate(matrix):
        for match in re.finditer(r'\d+', row):
            start, end = match.span()
            number = int(match.group())
            indices.append(((row_idx, start), (row_idx, end - 1), number))

    return indices

# Call the function to get indices of whole numbers from the matrix
number_indices = get_indices_of_numbers(matrix)

# Print the result
for start, end, number in number_indices:
    # print(f"Number {number} starts at {start} and ends at {end}")
    part_number = PartNumber(number,start,end)
    part_numbers.append(part_number)

def find_adjacent_indices(matrix, row, col):
  adjacent_indices = []
  for i in range(max(0, row - 1), min(len(matrix), row + 2)):
    for j in range(max(0, col - 1), min(len(matrix[0]), col + 2)):
      if (i, j) != (row, col) and matrix[i][j].isdigit():
        # adjacent_indices.append(int(matrix[i][j]))
        adjacent_indices.append((i,j))
  return adjacent_indices

adjacent_numbers = []
# Find the position of symbols
for row_idx, row in enumerate(matrix):
  for col_idx, cell in enumerate(row):
    if cell == '*' or cell == '$' or cell == '+' or cell == '-' or cell == '#' or cell == '@' or cell == '%' or cell == '&' or cell == '=' or cell == '/':
      # Call the function to find adjacent numbers
      numbers_adjacent_to_symbol = find_adjacent_indices(matrix, row_idx, col_idx)
      adjacent_numbers.append(numbers_adjacent_to_symbol)      
      # print(f"Numbers adjacent to symbol at position ({row_idx}, {col_idx}): {numbers_adjacent_to_symbol}")    


numbers_2_add = []
# for part_number in part_numbers:
#    for i in range(len(adjacent_numbers)): 
#     for elem in adjacent_numbers[i]:        
#         if part_number.start[0] <= elem[0] <= part_number.end[0] and part_number.start[1] <= elem[1] <= part_number.end[1]:          
#           if part_number.number not in numbers_2_add:
#             numbers_2_add.append(part_number.number)

checked = False
for part_number in part_numbers:  
  for i in range(len(adjacent_numbers)):     
    for elem in adjacent_numbers[i]:        
      if part_number.start[0] <= elem[0] <= part_number.end[0] and part_number.start[1] <= elem[1] <= part_number.end[1]:          
        if not checked:  
          # print(part_number.number)          
          numbers_2_add.append(part_number.number)
          checked = True
    checked = False

print(sum(numbers_2_add))
# Your puzzle answer was 554003.