#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def count_words(filename):
    nb_mots = {}                        # initialise un dictionnaire
    with open(filename) as fichier:
        for line in fichier:
            mots = line.split()         # divise une chaîne de caractères en une liste ordonnée de sous-chaînes. Par défaut, le séparateur est l'espace
            for m in mots:
                m = m.lower()
                if m in nb_mots.keys():
                    nb_mots[m] = nb_mots[m] + 1
                else:
                    nb_mots[m] = 1
    return nb_mots

def print_words(filename):
    m = count_words(filename)
    tri_m = sorted(m.items(), key=lambda cle_valeur: cle_valeur[0]) #words.item : renvoie parie clé valeur
    for m in tri_m:
        print(str(m[0]) + " " + str(m[1]))
#.items() : renvoie liste de tuple à 2 elements (paire : clé valeur)/ 
#lambda : fonction anonyme (pour éviter créer une fonction) . elle prend en argument "cle_valeur" et trie selon la clé cle_valeur[0]


def print_top(filename):
    m = count_words(filename)
    tri_nb = sorted(m.items(), key=lambda cle_valeur: cle_valeur[1], reverse=True)
    for m in tri_nb[:20]:
        print(str(m[0]) + " " + str(m[1]))
###

#.item : renvoie liste de tuple à 2 elements (paire : clé valeur)/ 
#lambda : fonction anonyme (pour éviter créer une fonction). Elle prend en argument "cle_valeur" et trie selon la clé cle_valeur[0]



###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
