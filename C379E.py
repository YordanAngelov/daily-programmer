# https://www.reddit.com/r/dailyprogrammer/comments/cdieag/20190715_challenge_379_easy_progressive_taxation/
print("Challenge 379 (Easy)")

if __name__ == '__main__':
    def tax(i):
        if i < 10000:
            return 0
        elif 10000 <= i < 30000:
            return (i - 10000) * 0.1
        elif 30000 <= i < 100000:
            return 2000 + ((i - 30000) * 0.25)
        elif i >= 100000:
            return 2000 + (70000 * 0.25) + (i - 100000) * 0.4

    def tax_from_file(amount):
        file = open("tax_brackets", "r").readlines()
        # TODO: Merge below with the income_caps and tax_rates bits
        brackets = []
        for line in file:
            l = line.replace("\n", "").split(", ")
            print("l is %s" % str(l))
            brackets.append(line.replace("\n", "").split(", "))  # Splitting the lines in List[bracket, tax %]
        for a in brackets:
            i = brackets.index(a)
            if brackets[i][0] != "---":
                brackets[i] = (int(brackets[i][0]), float(brackets[i][1]))
            else:
                brackets[i] = (str(brackets[i][0]), float(brackets[i][1]))

        income_caps = []
        tax_rates = []
        for bracket in brackets:
            income_caps.append(bracket[0])
            tax_rates.append(bracket[1])

        if amount <= income_caps[0]:
            print("Amount of money taxed is below %d" % income_caps[0])
            return amount * tax_rates[0]
        elif income_caps[0] < amount <= income_caps[1]:
            print("Amount of money taxed is between %d and %d" % (income_caps[0], income_caps[1]))
            return (income_caps[0] * tax_rates[0]) + (amount - income_caps[0]) * tax_rates[1]
        elif income_caps[1] < amount <= income_caps[2]:
            print("Amount of money taxed is between %d and %d" % (income_caps[1], income_caps[2]))
            return (income_caps[0]) * tax_rates[0] + (income_caps[1] - income_caps[0]) * tax_rates[1] + \
                   (amount - income_caps[1]) * tax_rates[2]
        elif income_caps[2] <= amount:
            print("Amount of money taxed is more than %d" % (income_caps[2]))
            return (income_caps[0]) * tax_rates[0] + (income_caps[1] - income_caps[0]) * tax_rates[1] + \
                   (income_caps[2] - income_caps[1]) * tax_rates[2] + (amount - income_caps[2]) * tax_rates[3]

    # while True:
    #     print("The amount of tax is: " + str(tax(int(input("What amount of money do you want to tax? ")))))

    print(str(tax_from_file(10000)) + " should be 0")
    print(str(tax_from_file(20000)) + " should be 1000")
    print(str(tax_from_file(56789)) + " should be 8697")
    print(str(tax_from_file(100000)) + " should be 19500")
    print(str(tax_from_file(1234567)) + " should be 473326")
