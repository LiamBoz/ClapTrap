

def SumList():
    list = [1,2,3,4,5]
    inc_num = 0
    sum = 0
    while True:
        try:
            sum += list[inc_num]
            inc_num += 1
        except:
            return sum
    
print(SumList())
