### 
Author: Eliana Mugar
Date: 2/10/2021 
###

#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
   # print("\nHere are the corpora built into nltk:")
    #for h in os.listdir(nltk.data.find("corpora")):
        #if '.zip' not in h:
            #print(h)
    #print()
    #chosen_corpora = raw_input("Enter corpora name (copy the name EXACTLY as listed): ")
    print("\nHere are the options of corpora from gutenberg: \n")
    for corpus in nltk.corpus.gutenberg.fileids():
        print(str(corpus))
    print()
    text = gutenberg.raw(str(input("Enter text file name (with .txt): ")))
    tokens = nltk.word_tokenize(text)
    tagged_corpora = nltk.pos_tag(tokens)
    update_corpora = ""
        #print(tagged_corpora)
    for i in range(len(tagged_corpora) - 1):
        if 'JJ' in tagged_corpora[i] and 'JJ' in tagged_corpora[i+1] and \
            'such' not in tagged_corpora[i] and 'such' not in tagged_corpora[i+1]:
            for x in range(i - 6, i + 1):
                if x == i:
                    update_corpora += "[" + str(tagged_corpora[x][0]) + " "
                else:
                    update_corpora += str(tagged_corpora[x][0]) + " "
            for j in range(i + 1, i + 7):
                if j == i + 1:
                    update_corpora += str(tagged_corpora[j][0]) + "] "
                else:
                    update_corpora += str(tagged_corpora[j][0]) + " "
            update_corpora += "\n"
            update_corpora += "\n"
            
            #doesn't store consecutive strings, only PAIRINGS
            #ex: if 1 is JJ and 2 is JJ, but 3 is also JJ, it won't save 3
            #need to create a new iterator to check range of tagged_corpora[i -->] b/c
                #but how to skip to new index at end of range?
            #need to deal with punctuation counting as an index? need to tack it on 

    f = open(str(input("Enter filename for which you want the data text to be exported (with .txt): \n")), "w")
    f.write(update_corpora)

while True:
    answer = input("Run the program? (y/n): ")
    if answer not in ('y', 'n'):
        print("Invalid input.")
        break
    if answer == 'y':
        main()
    else:
        print("Goodbye.")
        break

#emma_text = nltk.word_tokenize(emma)
#print(nltk.pos_tag(emma_text))

#text = "I played with the big red ball"
#tokenss = nltk.word_tokenize(text)
#tagged_text = nltk.pos_tag(tokenss)
#print(tagged_text)
#output: [('I', 'PRP'), ('played', 'VBD'), ('with', 'IN'), ('the', 'DT'), ('big', 'JJ'), ('red', 'JJ'), ('ball', 'NN')]
