
# times = [7,15,30]
# distance = [9,40,200]

times = [44,70,70,80]
distance = [283,1134,1134,1491]

ways=[]
count = 0
for i in range(len(times)):
  for t in range(times[i]+1):
    travel = (times[i]-t)*t    
    if travel > distance[i]:      
      count=count+1     
  ways.append(count)
  count = 0

print(ways)
ans = 1
for w in ways:
  ans = ans*w

print(ans)

# Your puzzle answer was 219849.