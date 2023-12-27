import re
import math

# Specify the file path
file_path = 'day10pt1.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
  # Read the file lines and store them in a list
  matrix = file.readlines()
  matrix = [line.replace('\n', '') for line in matrix]

# matrix = '''.....
# .S-7.
# .|.|.
# .L-J.
# .....'''

# matrix = '''..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...'''
# matrix = matrix.split('\n')


# Find the position of 'S'
for row_idx, row in enumerate(matrix):
  for col_idx, cell in enumerate(row):
    if cell == 'S':
      S_pos = [row_idx,col_idx]
      print(f"S at position ({row_idx}, {col_idx})")       

def is_valid(x,y):
  if x >=0 and x < len(matrix) and y >=0 and y < len(matrix[0]):  
    return True
  else:
    return False

def move_dir(pos,sym,nxt_sym_pos,nxt_sym):
  new_pos = [-1,-1]
  if sym == '|':
    if ((nxt_sym == 'L' or nxt_sym == 'J') and pos[0] < nxt_sym_pos[0]) or ((nxt_sym == 'F' or nxt_sym == '7') and pos[0] > nxt_sym_pos[0]) or (nxt_sym == '|' and pos[0] != nxt_sym_pos[0]):      
      new_pos[0] = nxt_sym_pos[0]
      new_pos[1] = pos[1]
  if sym == '-':
    if ((nxt_sym == 'J' or nxt_sym == '7') and pos[1] < nxt_sym_pos[1]) or ((nxt_sym == 'L' or nxt_sym == 'F') and pos[1] > nxt_sym_pos[1]) or (nxt_sym == '-' and pos[1] != nxt_sym_pos[1]):
      new_pos[0] = pos[0]
      new_pos[1] = nxt_sym_pos[1]
  if sym == 'L':    
    if ((nxt_sym == '|' or nxt_sym == 'F' or nxt_sym == '7') and pos[0] > nxt_sym_pos[0]):
      new_pos[0] = nxt_sym_pos[0]
      new_pos[1] = pos[1]
    if ((nxt_sym == '-' or nxt_sym == '7' or nxt_sym == 'J') and pos[1] < nxt_sym_pos[1]):
      new_pos[0] = pos[0]
      new_pos[1] = nxt_sym_pos[1]
  if sym == 'J':   
    if ((nxt_sym == '|' or nxt_sym == 'F' or nxt_sym == '7') and pos[0] > nxt_sym_pos[0]):
      new_pos[0] = nxt_sym_pos[0]
      new_pos[1] = pos[1]
    if ((nxt_sym == '-' or nxt_sym == 'F' or nxt_sym == 'L') and pos[1] > nxt_sym_pos[1]):
      new_pos[0] = pos[0]
      new_pos[1] = nxt_sym_pos[1] 
  if sym == '7':
    if ((nxt_sym == '|' or nxt_sym == 'L' or nxt_sym == 'J') and pos[0] < nxt_sym_pos[0]):
      new_pos[0] = nxt_sym_pos[0]
      new_pos[1] = pos[1]
    if ((nxt_sym == '-' or nxt_sym == 'L' or nxt_sym == 'F') and pos[1] > nxt_sym_pos[1]):
      new_pos[0] = pos[0]
      new_pos[1] = nxt_sym_pos[1]
  if sym == 'F':
    if ((nxt_sym == '|' or nxt_sym == 'L' or nxt_sym == 'J') and pos[0] < nxt_sym_pos[0]):
      new_pos[0] = nxt_sym_pos[0]
      new_pos[1] = pos[1]
    if ((nxt_sym == '-' or nxt_sym == '7' or nxt_sym == 'J') and pos[1] < nxt_sym_pos[1]):
      new_pos[0] = pos[0]
      new_pos[1] = nxt_sym_pos[1]

  if not is_valid(new_pos[0],new_pos[1]):
    new_pos = [-1,-1]

  return new_pos
 


count = [0,0,0,0]
pos_start = [S_pos[0],S_pos[1]]

# go up
pos = [pos_start[0]-1,pos_start[1]]
new_pos = [-1,-1]
prev = [-1,-1]
while pos[0]!=-1 and pos[1]!=-1:
  if matrix[pos[0]][pos[1]] == '|' or matrix[pos[0]][pos[1]] == '-' or matrix[pos[0]][pos[1]] == 'L' or matrix[pos[0]][pos[1]] == 'J' or matrix[pos[0]][pos[1]] == '7' or matrix[pos[0]][pos[1]] == 'F':
    count[0] += 1
  tmp = [pos[0],pos[1],matrix[pos[0]][pos[1]]]     
  for i in [-1,0,1]:
    for j in [-1,0,1]:            
      if (i==-1 and j==0) or (i==0 and j==1) or (i==1 and j==0) or (i==0 and j==-1):          
        if is_valid(pos[0]+i,pos[1]+j):          
          if pos[0]+i != prev[0] or pos[1]+j != prev[1]:                       
            pos_tmp = move_dir(pos,matrix[pos[0]][pos[1]],[pos[0]+i,pos[1]+j],matrix[pos[0]+i][pos[1]+j])
            if pos_tmp[0]==-1 and pos_tmp[1]==-1:
              pos[0] = tmp[0]
              pos[1] = tmp[1]
            else:
              new_pos[0] = pos_tmp[0]
              new_pos[1] = pos_tmp[1]  
  prev = [pos[0],pos[1]]                                     
  pos[0] = new_pos[0]
  pos[1] = new_pos[1]  
  new_pos = [-1,-1]
  


# go right
pos = [pos_start[0],pos_start[1]+1]
new_pos = [-1,-1]
prev = [-1,-1]
while pos[0]!=-1 and pos[1]!=-1:
  if matrix[pos[0]][pos[1]] == '|' or matrix[pos[0]][pos[1]] == '-' or matrix[pos[0]][pos[1]] == 'L' or matrix[pos[0]][pos[1]] == 'J' or matrix[pos[0]][pos[1]] == '7' or matrix[pos[0]][pos[1]] == 'F':
    count[1] += 1
  tmp = [pos[0],pos[1],matrix[pos[0]][pos[1]]]     
  for i in [-1,0,1]:
    for j in [-1,0,1]:            
      if (i==-1 and j==0) or (i==0 and j==1) or (i==1 and j==0) or (i==0 and j==-1):          
        if is_valid(pos[0]+i,pos[1]+j):          
          if pos[0]+i != prev[0] or pos[1]+j != prev[1]:            
            pos_tmp = move_dir(pos,matrix[pos[0]][pos[1]],[pos[0]+i,pos[1]+j],matrix[pos[0]+i][pos[1]+j])
            if pos_tmp[0]==-1 and pos_tmp[1]==-1:
              pos[0] = tmp[0]
              pos[1] = tmp[1]
            else:
              new_pos[0] = pos_tmp[0]
              new_pos[1] = pos_tmp[1]  
  prev = [pos[0],pos[1]]                                     
  pos[0] = new_pos[0]
  pos[1] = new_pos[1]  
  new_pos = [-1,-1]


# go down
pos = [pos_start[0]+1,pos_start[1]]
new_pos = [-1,-1]
prev = [-1,-1]
while pos[0]!=-1 and pos[1]!=-1:
  if matrix[pos[0]][pos[1]] == '|' or matrix[pos[0]][pos[1]] == '-' or matrix[pos[0]][pos[1]] == 'L' or matrix[pos[0]][pos[1]] == 'J' or matrix[pos[0]][pos[1]] == '7' or matrix[pos[0]][pos[1]] == 'F':
    count[2] += 1
  tmp = [pos[0],pos[1],matrix[pos[0]][pos[1]]]     
  for i in [-1,0,1]:
    for j in [-1,0,1]:            
      if (i==-1 and j==0) or (i==0 and j==1) or (i==1 and j==0) or (i==0 and j==-1):          
        if is_valid(pos[0]+i,pos[1]+j):          
          if pos[0]+i != prev[0] or pos[1]+j != prev[1]:            
            pos_tmp = move_dir(pos,matrix[pos[0]][pos[1]],[pos[0]+i,pos[1]+j],matrix[pos[0]+i][pos[1]+j])
            if pos_tmp[0]==-1 and pos_tmp[1]==-1:
              pos[0] = tmp[0]
              pos[1] = tmp[1]
            else:
              new_pos[0] = pos_tmp[0]
              new_pos[1] = pos_tmp[1]  
  prev = [pos[0],pos[1]]                                     
  pos[0] = new_pos[0]
  pos[1] = new_pos[1]  
  new_pos = [-1,-1]


# go left
pos = [pos_start[0],pos_start[1]-1]
new_pos = [-1,-1]
prev = [-1,-1]
while pos[0]!=-1 and pos[1]!=-1:
  if matrix[pos[0]][pos[1]] == '|' or matrix[pos[0]][pos[1]] == '-' or matrix[pos[0]][pos[1]] == 'L' or matrix[pos[0]][pos[1]] == 'J' or matrix[pos[0]][pos[1]] == '7' or matrix[pos[0]][pos[1]] == 'F':
    count[3] += 1
  tmp = [pos[0],pos[1],matrix[pos[0]][pos[1]]]     
  for i in [-1,0,1]:
    for j in [-1,0,1]:            
      if (i==-1 and j==0) or (i==0 and j==1) or (i==1 and j==0) or (i==0 and j==-1):          
        if is_valid(pos[0]+i,pos[1]+j):          
          if pos[0]+i != prev[0] or pos[1]+j != prev[1]:            
            pos_tmp = move_dir(pos,matrix[pos[0]][pos[1]],[pos[0]+i,pos[1]+j],matrix[pos[0]+i][pos[1]+j])
            if pos_tmp[0]==-1 and pos_tmp[1]==-1:
              pos[0] = tmp[0]
              pos[1] = tmp[1]
            else:
              new_pos[0] = pos_tmp[0]
              new_pos[1] = pos_tmp[1]  
  prev = [pos[0],pos[1]]                                     
  pos[0] = new_pos[0]
  pos[1] = new_pos[1]  
  new_pos = [-1,-1]
  
print(count)
print(math.ceil(max(count)/2))

# Your puzzle answer was 6717.