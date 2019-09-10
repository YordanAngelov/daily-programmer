# https://www.reddit.com/r/dailyprogrammer/comments/ab9mn7/20181231_challenge_371_easy_n_queens_validator/
if __name__ == '__main__':

    def qcheck(ns: list):
        print("List being checked is %s" % str(ns))
        if len(set(ns)) == len(ns):  # set gives you the unique elems so if the len is same, all elems are unique
            for x in range(len(ns)):  # index of the elem we are looking at
                for x1 in range(len(ns)):  # index of the elem we are comparing
                    if x == x1:
                        pass
                    else:
                        if ns[x] == ns[x1] + (x-x1) or ns[x] == ns[x1] - (x-x1):
                            print("Some of the queens are on the same diagonal")
                            return False
            print("All looks good!")
            return True
        else:
            return False

    print("Challenge:")
    print(str(qcheck([4, 2, 7, 3, 6, 8, 5, 1])) + " => true")
    print(str(qcheck([2, 5, 7, 4, 1, 8, 6, 3])) + " => true")
    print(str(qcheck([5, 3, 1, 4, 2, 8, 6, 3])) + " => false")
    print(str(qcheck([5, 8, 2, 4, 7, 1, 3, 6])) + " => false")
    print(str(qcheck([4, 3, 1, 8, 1, 3, 5, 2])) + " => false")
