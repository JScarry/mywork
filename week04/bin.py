#https://stackoverflow.com/questions/3528146/convert-decimal-to-binary-in-python

#def decToBin(n):
    #if n==0: return ''
    #else:
        #return decToBin(n/2) + str(n%2)


#https://stackoverflow.com/questions/61659143/how-do-i-divide-a-number-by-two-multiple-times/61659290
num = int(input("Input number: "))    # 1
if num > 100 or num < 1:              # 2
    print("Error!")                   # 3
else:                                 # 4
    times = 0                         # 5
    while num >= 2:                   # 6
        num /= 2                      # 7
        times += 1                    # 8
    print(times)                      # 9
