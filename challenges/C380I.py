import re
# https://www.reddit.com/r/dailyprogrammer/comments/cn6gz5/20190807_challenge_380_intermediate_smooshed/
morse = {
        'A': '.-',         'B': '-...',        'C': '-.-.',       'D': '-..',
        'E': '.',          'F': '..-.',        'G': '--.',        'H': '....',
        'I': '..',         'J': '.---',        'K': '-.-',        'L': '.-..',
        'M': '--',         'N': '-.',          'O': '---',        'P': '.--.',
        'Q': '--.-',       'R': '.-.',         'S': '...',        'T': '-',
        'U': '..-',        'V': '...-',        'W': '.--',        'X': '-..-',
        'Y': '-.--',       'Z': '--..'
    }

MORSE_CHAR = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
              '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']


def morsify(s):
    # My solution:
    # word_in_morse = ""
    # for a in s:
    #     word_in_morse = "%s%s" % (word_in_morse, morse.get(a.capitalize()))
    # return word_in_morse
    # Some dude on Reddit (much faster):
    morse_code = []
    for char in s:
        morse_code.append(MORSE_CHAR[abs(ord('a') - ord(char))])
    return ''.join(morse_code)


if __name__ == '__main__':
    print("This is the Challenge 380 (Easy)")
    word = input("Enter a word: ")
    print("The word that you entered is %s" % word)
    morse_word = morsify(word)
    print("The word in morse code is: %s" % morse_word)

    opt = input("Do you want to run Optional challenge 1? (Y/N)")
    # 1) The sequence -...-....-.--. is the code for four different words (needing, nervate, niding, tiling).
    # Find the only sequence that's the code for 13 different words.
    if opt.lower() == 'y':
        # My solution:
        # f = open("enable1", "r")                # Opens the file
        # cont = f.read()                         # Reads the file
        # spaces = r"\s+"                         # Regex for spaces
        # all_words = re.split(spaces, cont)      # Splits the file into words
        #
        # all_morse_words = []                    # Instantiating an empty list
        # for a in all_words:
        #     all_morse_words.append(morsify(a))  # Creating a list of all the words in morse
        #
        # occurrences = {}
        # # occurrences = []
        # for a in all_morse_words:
        #     # if a not in occurrences:  # seems to be faster without the if
        #     # occurrences.append((a, all_morse_words.count(a)))
        #     occurrences[a] = all_morse_words.count(a)
        # print(occurrences)

        # Some dude on Reddit (much faster):
        occ = {}
        with open("enable1") as all_words:
            while True:
                word = all_words.readline().strip()
                if not word:
                    break
                code = morsify(word)
                occ[code] = occ.get(code, 0) + 1

        for morse_code, count in occ.items():
            if count == 13:
                print("The morse code which occurs 13 times is: " + morse_code)
            if re.findall(r"[-]{15}", morse_code):
                print("The morse code that has 15 consecutive dashes is: " + morse_code)

        # Challenge 3
        twenty_one = []
        with open("enable1") as all_words:
            while True:
                word = all_words.readline().strip()
                if not word:
                    break
                elif len(word) == 21:
                    twenty_one.append(word)
        for word in twenty_one:
            mw = morsify(word)
            dashes = 0
            dots = 0
            for char in mw:
                if char == '-':
                    dashes = dashes + 1
                if char == '.':
                    dots = dots + 1
            if dashes == dots:
                print("This word (" + word + ") is PERFECTLY balanced... Like all things should be!")

        # Challenge 4
        print("Challenge 4:")
        thirteen = []
        with open("enable1") as all_words:
            while True:
                word = all_words.readline().strip()
                if not word:
                    break
                elif len(word) == 13:
                    thirteen.append(morsify(word))

        for word in thirteen:
            if word == ''.join(reversed(word)):
                print(word + " is a palindrome.")

        # Challenge 5 - that is NOT an actual solution
        print("Challenge 5:")
        words = []
        unique_words = []
        with open("enable1") as all_words:
            while True:
                word = all_words.readline().strip()
                if not word:
                    break
                elif len(word) < 13:
                    m = morsify(word)
                    if len(m) == 13:
                        words.append(m)

        for word in words:
            if words.count(word) == 1:
                unique_words.append(word)
        print("The 13-character words that do not appear anywhere else are:")
        print(unique_words)

    else:
        print("Bye!")
        exit()
