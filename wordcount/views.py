from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import operator
from IPython.display import HTML

def home(request):
    return render(request, 'home.html', )

def counter(request):
    
    
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()  # Splitting text
    
    # LOOP to separate each word and count them
    
    worddictionary = {}
    
    for word in wordlist:
        if word in worddictionary:
            # Increase
            worddictionary[word] +=1
        else:
            # add to the dictionary
            worddictionary[word] = 1
    
    # Sorted dictionary
    sortedwords =  sorted(worddictionary.items()
                    , key = operator.itemgetter(1) 
                    , reverse = True)
                               
                     
    
    # build a dictionary
    data =  {   'fulltext'       : fulltext
            ,   'count'          : len(wordlist)
            ,   'sortedwords' : sortedwords #items.()
            }
    
     # Return (Get the functions)
    return render(request , 'counter.html', data)