import time

twenty_second_countdown = range(20, 1, -1)

for time_left in twenty_second_countdown:
    print(time_left) 
    time.sleep(1)