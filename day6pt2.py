time = 44707080
distance = 283113411341491

count = 0
for t in range(time+1):
  travel = (time-t)*t    
  if travel > distance:      
    count=count+1  

print(count)

# Your puzzle answer was 29432455.