# Specify the file path
file_path = 'day14pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]


# matrix = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''
# matrix = matrix.split('\n')


for i in range(len(matrix)):
  matrix[i] = list(matrix[i])

count = 0
state = True
while state:
  for i in range(len(matrix)-1):
    for j in range(len(matrix[0])):
      if matrix[i][j]=='.' and matrix[i+1][j]=='O':
        matrix[i][j]='O'
        matrix[i+1][j]='.'   
  count += 1
  if(count>len(matrix)):
    state = False

totalload = 0
for i in range(len(matrix)):
  totalload += (len(matrix)-i) * matrix[i].count('O')

# print(matrix)
print(totalload)

# Your puzzle answer was 106186.