# Python for programmers assignemnt 1
# author: Scott Barth
from random import randrange
def create_compound_list(rate, years=20):

    # use list comprehension and create a list of compounded interest for each unit (years)
    return [(1+rate)**i for i in range(1, years+1)]

def print_rates(amount, compound_list):
    year = 1
    po = 0
    for compound in compound_list:
        pn = amount * compound
        print ("year: {} amount: ${:,.2f}".format(year, pn))
        year +=1

    print("You made: ${:,.2f} dollars in interest.".format(pn - amount))


def compression():
    data = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    # data = ""
    count = 1
    cdata = []

    match = data[0]

    for i in range(len(data)):

        # end of data? yes, write the record and return
        if i+1 == len(data):
            cdata.append(str(count))
            cdata.append(match)
            return cdata

        elif match == data[i+1]:
            count += 1
        else:
            cdata.append(str(count))
            cdata.append(match)
            match = data[i + 1]
            count = 1






def main():
    x = randrange(1,3)
    print(x)

    f = open("Shiftboard-Scheduling-Table.csv")

    for i in range(10):
        print("This is line %d\r\n")


    # print("Homework 1 part 1 of 2")
    #
    # # create the compounded list
    # compound_list = create_compound_list(.10)
    #
    # while True:
    #     amount = input("Please enter the amount or q to quit> ")
    #     if amount == 'q' or  amount == 'Q': break
    #
    #     # run and print the calculations
    #     print_rates(int(amount), compound_list)
    #
    # print("Good-bye.")
    #
    # print("Homework 1 part 2 of 2")
    # compressed = compression()
    #
    # # print the compressed string
    # for c in compressed:
    #     print(c, end='')

if __name__ == "__main__":
    main()
