# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
print("Challenge 379 (Easy)")

if __name__ == '__main__':
    # This is the hardcoded solution
    # def tax(i):
    #     if i < 10000:
    #         return 0
    #     elif 10000 <= i < 30000:
    #         return (i - 10000) * 0.1
    #     elif 30000 <= i < 100000:
    #         return 2000 + ((i - 30000) * 0.25)
    #     elif i >= 100000:
    #         return 2000 + (70000 * 0.25) + (i - 100000) * 0.4

    # This is the solution for reading tax brackets from a file which works whenever the brackets are updated.
    # This assumes that the pair of income cap and tax rate will be defined as per the spec in the exercise.
    def tax_from_file(amt: int):
        print("Checking tax for an amount of " + str(amt))
        if amt > 0:
            file = open("tax_brackets", "r").readlines()  # Reading file
            ics = []  # Income caps
            trs = []  # Tax rates
            for line in file:
                l = line.replace("\n", "").split(", ")
                try:
                    ics.append(int(l[0]))
                except ValueError:
                    # Giving a default max value of 1 trillion. Using float("inf") messes it up.
                    ics.append(1000000000000)
                trs.append(float(l[1]))

            tax = float(0)
            # Formula for calculating is (had to write it out on paper first - was very helpful):
            # tax = (ic[0] - 0)*tr[0] + (ic[1] - ic[0])*tr[1] + ... + (amt - ic[n-1])*tr[n]
            for ic in ics:
                if amt > ic:
                    if ics.index(ic) == 0:  # This assumes that the first cap will always be tax-free
                        pass
                    else:
                        tax = tax + (ic - ics[ics.index(ic) - 1]) * trs[ics.index(ic)]
                else:  # if amt is bigger than the last income cap specified in the file
                    tax = tax + (amt - ics[ics.index(ic) - 1]) * trs[ics.index(ic)]
                    break
                    # if the loop is not broken, it will lead to wrong results for amount which are smaller
                    # than at least 1 income cap as it will run this step more than 1 time

            return int(tax) # returns a rounded up number

        else:
            raise ValueError("You need to provide an amount higher than zero.")


    print(str(tax_from_file(10000)) + " should be 0")
    print(str(tax_from_file(20000)) + " should be 1000")
    print(str(tax_from_file(56789)) + " should be 8697")
    print(str(tax_from_file(100000)) + " should be 19500")
    print(str(tax_from_file(1234567)) + " should be 473326")
