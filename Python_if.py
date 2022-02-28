

num1=12
key=False
if num1 == 12:
    if key:
        print('num1 is equal to 12 and they have the key')
    else:
        print('num1 is equal to 12 and they have no key')
elif num1 < 12:
    print('num1 less than 12') 
else:
    print('num1 is not equal to 12')
    

a=23

if a>10:
    print("you got this")

    

b=33

if b==12:
    print('not gonna happen')
elif b<99:
    print('bengals win')

    
c=25

if c>98:
    print('Superbowl')
elif c==77:
    print('2022')
else:
    print('Euphoria')

d=9876
if d<999999:
    print('beyonce')
    if d==9876:
        print('hello')


e=29

if e>=21:
    print('gone')


i=0
for i in range(10):
    print('{} iteration thruogh the loop'.format(i))
    i += 1

i=0
while i<10:
    print('{}iteration thruogh the loop'.format(i))
    i += 1 
    
for number in range(3):
    print('I love PYTHON')

successful=False
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break
else:    
    print('attempted 3 times and failed')

#Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

count = 0
for number in range(1,10):
    if number %2==0:
        count += 1
        print(number)
print(f'We have{count} even numbers')

        
        

print(type(5))        
    
