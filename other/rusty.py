import re

# Goes through the list of words in enable1 and spits out all the ones that contain 'rust' into a file
print("This script creates a list of words that contain a regex of your choice.")
usr_input = input("What regex are you looking for? ")
reg = r"%s" % usr_input
print("The regex you provided is %s" % reg)


def rustify(w):
    if re.findall(reg, w):
        return w


words = []
with open("challenges/enable1") as all_words:
    while True:
        word = all_words.readline().strip()
        if not word:
            break
        words.append(rustify(word))

words = [x for x in words if x is not None]
f = open("other/words", "x")
for a in words:
    f.write(a + "\n")
f.close()

print("You're all done! Look in the words file to see your result.")
exit()
