# Specify the file path
file_path = 'day15pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]

# string = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'

result = 0
for string in matrix:
  items = string.split(',')
  for item in items:
    current_value = 0
    for letter in item:
      ASCII_code = ord(letter)
      current_value += ASCII_code
      current_value = current_value*17
      current_value = current_value%256
    result = result + current_value

print(result)