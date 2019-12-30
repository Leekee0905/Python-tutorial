size=50
i=0
while True:
    i+=1
    if i>size :
        break
    print('★'*i,end='')
    print('☆'*(size-(i-1)))