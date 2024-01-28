def bank(x, y):
    if x > 0 and y > 0:
        count = 0
        while count < y:
            x= x*1.1
            count += 1
        return x    
    elif x <= 0: return 0
    elif y <= 0: return x
    

x = 7000
y = 2
print(bank(x, y))