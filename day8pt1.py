# Specify the file path
file_path = 'day8pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]

directions = matrix[0]
matrix = matrix[2:]

# directions = 'LLR'

# matrix = '''AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)'''
# matrix = matrix.split('\n')


result = dict()

for i in range(len(matrix)):
  # Split the string based on '=' and remove spaces
  parts = [part.strip() for part in matrix[i].split('=')]

  # Extract variable names
  parts = [parts[0], *parts[1].replace('(', '').replace(')', '').replace(' ', '').split(',')]

  result[parts[0]] = [parts[1],parts[2]]

# Display the result
# print(result)

state = 'AAA'
count = 0
while state != 'ZZZ':
  for i in range(len(directions)):
    if(directions[i]=="L"):
      state = result[state][0]
    else:
      state = result[state][1]
    count += 1

print(count)

