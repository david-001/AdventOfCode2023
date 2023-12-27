# Specify the file path
file_path = 'day8pt2.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]

directions = matrix[0]
matrix = matrix[2:]

# directions = 'LR'

# matrix = '''11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)'''
# matrix = matrix.split('\n')


results = dict()

for i in range(len(matrix)):
  # Split the string based on '=' and remove spaces
  parts = [part.strip() for part in matrix[i].split('=')]

  # Extract variable names
  parts = [parts[0], *parts[1].replace('(', '').replace(')', '').replace(' ', '').split(',')]

  results[parts[0]] = [parts[1],parts[2]]

# Display the result
# print(results)

states = []
for result in results:  
  if result[-1] == 'A':
    states.append(result)

# count = 0
# counts = []
# for i in range(len(states)):
#   state = states[i] 
#   while state[-1] != 'Z':
#     for j in range(len(directions)):
#       if(directions[j]=="L"):
#         state = results[state][0]
#       else:
#         state = results[state][1]
#       count += 1
#   counts.append(count)
#   count = 0

# ans = max(counts)
# print(ans)

def check_Z(arr):
  for elem in arr:
    if elem[-1] != 'Z':
      return False
  return True


count = 0
counts = []
while not check_Z(states):  
  for j in range(len(directions)):    
    if(directions[j]=="L"):  
      for i in range(len(states)):    
        states[i] = results[states[i]][0]
    else:  
      for i in range(len(states)):     
        states[i] = results[states[i]][1]
    count += 1
    print(states)
    print(count)

print(count)
