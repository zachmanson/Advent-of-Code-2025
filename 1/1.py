import os

dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(dir, "input.txt")

with open(file_path, 'r') as f:
    lines = [line.rstrip('\n') for line in f]

dial = 50
password = 0
password_p2 = 0
for line in lines:
    direction = line[0]
    clicks = int(line[1:])
    if direction == 'R':
        loops = (dial + clicks) // 100
        dial = (dial + clicks) % 100
        if dial == 0 and loops > 0:
            loops -= 1 #avoid double counting if end at 0 
    else:  
        if dial == 0: 
            loops = (clicks - 1) // 100 #clicks - 1 because I'm counting ending at 0 separaetly at the end. Starting at 0: [1, 99] -> 0 loops, [100, 199] -> 1 loop, [200, 299] -> 2 loops, etc
        else:
            loops = (clicks - 1 + (100 - dial)) // 100 # extra factor of 100 - dial to convert it to be like dial == 0 case (in terms of loops)
        dial = (dial - clicks) % 100
    
    password_p2 += loops
    if dial == 0:
        password += 1
        password_p2 += 1
        
print(password)
print(password_p2)