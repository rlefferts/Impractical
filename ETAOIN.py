import sys
import pprint


TEXT = 'Like the castle in its corner in a medieval game, I foresee terrible \
trouble and I stay here just the same.'

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def count_letters(d, w):

    for l in w:
        l = l.lower()
        if l in ALPHABET:
            if l not in d:
                d[l] = 0
            d[l] += 1

    return(d)


def main():

    d = {}

    print("Counting the letters in:\n", TEXT, '\n')

    for word in TEXT.split():
        count_letters(d, word)

    for (l,x) in sorted(d.items(), key=lambda x:x[1], reverse=True):
            print("%s : %2d : %s" % (l, x, 'X' * x))

if __name__ == "__main__":
    main()
