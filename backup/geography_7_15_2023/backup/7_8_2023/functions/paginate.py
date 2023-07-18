result_count = 440
max_downloads = 100

for i in range(0, result_count, max_downloads):
    min = i
    max = 0

    #Get Min
    if i != 0:
        min = min + 1
    else:
        min = 1

    #Get max
    if i + max_downloads > result_count:
        max = result_count
    else:
        max = i + max_downloads
        
    print(min, max)
