"""convert a string into pig latin"""
import sys


VOWELS='aeiouAEIOU'

def pigify(s):
    """Convert a word into its pig latin replacement"""
    if len(s) == 0:
        raise ValueError("Empty String")
    
    s = str.strip(s)
    starting_letter = s[0]

    if starting_letter not in VOWELS:

        if len(s) > 1:
            if starting_letter.isupper():
                newstr = s[1].upper() + s[2:] + starting_letter.lower() + 'ay'
            else:
                newstr = s[1:] + starting_letter + 'ay'
        else:
            newstr = starting_letter + 'ay'

    else:
        newstr = s + 'way'

    return(newstr)

def main():
    s = input("\nEnter a word to pigify: ")

    while s:
        print(pigify(s))
        print("\n")
        s = input("\nEnter a word to pigify: ")

    print('thank you\n')
    

if __name__ == "__main__":
    main()
