from calendar import monthrange

def main():

    #Simple Get days in a month 
    date_range = monthrange(2011, 2)
    print(date_range[0])
    print(date_range[1])
    print(" ")
    date_range = monthrange(2023, 9)
    print(date_range[0])
    print(date_range[1])
    print(" ")

    loop_over_year(2012)



#loop over any year 
def loop_over_year(year):
    for month in range(1, 13):
        #print("Loop ", year, month)
        date_range = monthrange(year, month)
        print(date_range[1])



if __name__ == "__main__":
    main()

