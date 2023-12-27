import re


# Specify the file path
file_path = 'day18pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  lines = file.readlines()
  lines = [line.replace('\n', '') for line in lines]


# lines = '''R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)'''
# lines = lines.split('\n')

# Define directions for moving (up, down, left, right)
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

length = 1000
terrain = [['.' for _ in range(length)] for _ in range(length)]

# Initialize variables to track the current position and volume of the lagoon
current_position = (int(len(terrain[0])/2), int(len(terrain[0])/2))
lagoon_volume = 0

min_row = 99999999
max_row = -1
min_col = 99999999
max_col = -1
for line in lines:
  # Use a regular expression to extract 'R' and '12'
  match = re.search(r'([A-Z]) (\d+)', line)
  direction = match.group(1)
  distance = int(match.group(2))

  dx, dy = directions[direction]
  for _ in range(distance):
    current_position = (current_position[0] + dx, current_position[1] + dy)
    lagoon_volume += 1
    terrain[current_position[0]][current_position[1]] = '#'
    if current_position[0] < min_row:
      min_row = current_position[0]
    if current_position[0] > max_row:
      max_row = current_position[0]
    if current_position[1] < min_col:
      min_col = current_position[1]
    if current_position[1] > max_col:
      max_col = current_position[1]

# print(min_row)
# print(max_row)
# print(min_col)
# print(max_col)
print(terrain)

dig = False
i=min_row+1
j=min_col
state = True
while state:
  j=min_col
  while min_col<max_col+1: 
    if i<max_row:
      if terrain[i][j]=='#' and terrain[i][j+1]=='.' and dig==False:
        dig=True                              
      elif terrain[i][j]=='.' and dig==True:
        lagoon_volume += 1      
      elif terrain[i][j]=='#' and dig==True:
        dig=False      
        i+=1
        j=min_col
        if terrain[i][j]=='#' and terrain[i][j+1]=='.' and dig==False:
          dig=True   
      # if i>5000:           
      # print(i,j,terrain[i][j],dig,lagoon_volume)  
      j+=1 
    else:
      state = False
      break
    
print('after',lagoon_volume)
  
