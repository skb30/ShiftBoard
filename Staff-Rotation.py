from random import randrange, shuffle
from csv import writer

def create_roster(staff, posts):
    # loop counter

    j = 0

    # initialization
    shuffle(staff)
    shuffle(posts)

    post_assignments = {}
    i = 0;
    j = len(staff)

    while j != 0:
        post_assignments[posts[i]] = staff[i]
        i += 1
        j -= 1

    while i < len(posts):
        post_assignments[posts[i]] = "      "
        i += 1


    return post_assignments

def create_list(filename):
    f = open(filename, "r")
    filelist = []
    if f.mode == 'r':  # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()

        fl = f.readlines()  # readlines reads the individual lines into a list
        for x in fl:
            filelist.append(x.strip('\n'))

    return filelist

def main():

    # build the post list
    posts = create_list("post.txt")


    posts_dict = {
       "Mobiles" : {
           "Paul 1" : "Name here",
           "Paul 2" : "Name here",
           "Paul 3" : "Name here",
           "Paul 4" : "Name here",
           "1" : "ID"
        },
        "Gates" : {
            "Charlie 1": "Name here",
            "Charlie 2": "Name here",
            "Ped 1C":"Name here",
            "Ped 5A": "Name here",
            "Ped 5D": "Name here",
            "Ped 7f": "Name here",
            "2": "ID"
        },
        "Booths": {
            "Wofle 1": "Name here",
            "Wofle 2": "Name here",
            "Wofle 3": "Name here",
            "Tantau 1": "Name here",
            "Tantau 2": "Name here",
            "Tantau 3": "Name here",
            "Paul 5 ": "Name here",
            "4": "ID"
        },
        "Breakers": {
            "Edward 1": "Name here",
            "Edward 2": "Name here",
            "Edward 3": "Name here",
            "Edward 4": "Name here",
            "Edward 5": "Name here",
            "Edward 6": "Name here",
            "Edward 7": "Name here",
            "Edward 8": "Name here",
            "Edward 9": "Name here",
            "Edward 10": "Name here",
            "Edward 11": "Name here",
            "5": "ID"
        }
    }


    staff = create_list("staff.csv")
    sizeOfStaff = len(staff)
    shuffle(staff)

    i = 0
    for group in posts_dict:
        if i < sizeOfStaff:
            for post in posts_dict[group]:
                if posts_dict[group][post] != "ID" and i < sizeOfStaff:
                    posts_dict[group][post] = staff[i]
                    i += 1

    # #print the roaster
    for group in posts_dict:
        print(group)
        for post in posts_dict[group]:
            print("{} - {}".format(post, posts_dict[group][post]))


    if i < sizeOfStaff:
        n = sizeOfStaff - i
        print("{} staff haven't been posted".format(n))
    exit()
    # build the staff list
    staff = create_list("staff.csv")

    roster = create_roster(staff, posts)


    with open('roster.csv', 'w') as f:
        f.write("%s,%s\n" % ("POST","NAME"))
        for key in roster.keys():
            f.write("%s,%s\n" % (key, roster[key]))

    print("done")

if __name__ == "__main__":
  main()

  # "Lobbies": {
  #     "George 1": "Name here",
  #     "George 2": "Name here",
  #     "George 3": "Name here",
  #     "George 4": "Name here",
  #     "George 5": "Name here",
  #     "George 6": "Name here",
  #     "George 7": "Name here",
  #     "George 8": "Name here",
  #     "George 9": "Name here",
  #     "Robert 1": "Name here",
  #     "Robert 2": "Name here",
  #     "Charlie 3": "Name here",
  #     "3": "ID",
  #     "Standing": "yes"
  # },