result_count = 440

for i in range(0, result_count, 100):
    min = i
    max = 0

    #Get Min
    if i != 0:
        min = min + 1
    else:
        min = 1

    #Get max
    if i + 100 > result_count:
        max = result_count
    else:
        max = i + 100
        
    print(min, max)