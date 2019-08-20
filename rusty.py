import re

# Goes through the list of words in enable1 and spits out all the ones that contain 'rust' into a file
list = []
with open("enable1") as all_words:
    while True:
        word = all_words.readline().strip()
        if not word:
            break
        # code = morsify(word)
        list.append(morsify(word))

list = [x for x in list if x is not None]
f = open("rust-words", "x")
for a in list:
    f.write(a + "\n")
f.close()