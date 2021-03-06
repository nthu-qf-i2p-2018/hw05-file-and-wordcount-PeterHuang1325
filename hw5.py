# -*- coding: utf-8 -*-

import csv    
import json
import pickle

from collections import Counter 


def main(filename):
    file=open(filename)
    # read file into lines
    lines = file.readlines()
    # declare a word list
    all_words = []

    # extract all words from lines
    #for line in open("i_have_a_dream.txt").readlines():
    for line in lines:
        words=line.split()
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]

        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            #word = words.strip()
            
            import string 
            new_word=word.strip(string.punctuation)

             
            
            # check if word is not empty
            #if new_word not in all_words:
                # append the word to "all_words" list
            if new_word:
                all_words.append(new_word)

    # compute word count from all_words
    
    counter = Counter(all_words)
    
    
    
    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
   
            
    with open("wordcount.csv","w",newline='') as csvfile:          
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csvfile)
        # write table head
        writer.writerow(['word', 'count'])
        
        #write all (word, count) pair into the csv writer
        
        for i in set(all_words):
            writer.writerow([i,all_words.count(i)])
      
       
        
        
        
   
 
    # dump to a json file named "wordcount.json"
    with open("wordcount.json","w")as jsonfile:
        json.dump(counter,jsonfile)
       
        
        
        

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    #pickle.dump(counter,open("wordcount.pkl","wb"))
    with open ("wordcount.pkl","wb") as pklfile:
        pickle.dump(counter,pklfile)
    


if __name__ == '__main__': 
    main("i_have_a_dream.txt")
   
