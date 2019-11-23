#author: Hsuvas Borkakoty
#date: 18.5.2018
#this program creates a tkinter based GUI which can be used to find the lemmas of the Inflected words in a file
#Lemmatization is carried out using a trie structure


import collections
import doctest
from tkinter import *
from tkinter import messagebox
#import sys
#sys.setrecursionlimit(300)
 #-*- encoding: utf-8 -*-

#creation of Trie structure and searching of lemma in trie
a=''
class Trie:
   
    def __init__(self):
        self.child = collections.defaultdict(Trie)
        
#inserting datas into trie
        
    def insert(self, string):
       
        node = self
        for char in string:
            node = node.child[char]
        node = node.child[None]

 #searching in Trie
        
    def contains(self, word):
        test=[]
        trie = self

        for char in word:
            if char in trie.child:
                trie = trie.child[char]
                test.append(char)
                print(test)
                print(''.join(test))
                #a=''.join(test)
            else:
                return test
        #print(a)
        return test


    def __str__(self, depth = 0):
       
        s = []
        for i in self.child:
            s.append( '{}{} {}'.format(
                ' ' * depth, i or '#', '\n' + self.child[i].__str__(depth + 1)))
        return ''.join(s)

if __name__ == '__main__':
    doctest.testmod()
    trie = Trie()
    #k=['তট','তাম','তামোল','তমাল','গম্ভীৰ','কৰুণা','সমীপ','বিষয়']  #set of words to insert in trie (test 1)
    k=open(r'H:\Project code wid GUI\text.txt','r' ,encoding='UTF16') #the file containing lemmas that is to be inserted in Trie
    for word in k:
        trie.insert(word)
    print(trie)

#creating GUI using Tkinter
    
    top = Tk()
    #top.geometry("500x500")
    top.title("Lemmatrix 1.0")
    L1 = Label(top, text="Enter the inflected word")
    L1.grid(row=2,column=1)
    #L1.pack(side = LEFT)
    E1 = Entry(top, bd =5)
    E1.grid(row=2,column=3)
    #E1.pack(side = RIGHT)
    L2 = Label(top, text="The lemma is:")
    L2.grid(row=5,column=1)
    #L2.pack( side = LEFT)
    L3=Label(top,text=" The Sentence is: ")
    L3.grid(row=4,column=1)

    
    #E2=Entry(top,bd=4)
    #E2.grid(row=3,column=3)
    #E2.pack(side = RIGHT)


    #tkinter button click procedure to find the rule based/trie based lemma   
    def btnclick():
        w=E1.get()
        #w2=E2.get()
        a=w.split(" ")
        
   #rule base for the inflected verbs with lemmas that start with different letters than the inflected form    
        if w !=" ":
           
                if w == 'গৈছিলো' or w == 'গলোহেতেন' or w == 'গলাহেতেন' or w == 'গলিহেতেন' or w == 'গৈছে' or w == 'গল' or w == 'গৈছ' or w == 'গৈছা' or w == 'গলো' or w == 'গলি' or w == 'গলা' or w == 'গৈছিল' or w == 'গৈছিলি':
                    #print('verb is: যা')
                    L2.config(text=" The Lemmas are:"+" যা ")
                    msg=messagebox.showinfo("The Lemma is",'যা')
                elif w == 'উপজিব' or w == 'উপজিছে' or w == 'উপজিছিল' or w == 'উপজিলে' or w == 'উপজিলেহেতেন' or w == 'উপজিলো' or w == 'উপজিছো':
                    #print('the verb is: ওপজ')
                    L2.config(text=" The Lemmas are:"+"ওপজ")
                    msg=messagebox.showinfo("The Lemma is",'ওপজ')
                elif w == 'লৈছে' or w == 'লৈছিল':
                    #print('the verb is: ল')
                    L2.config(text=" The Lemmas are:"+"ল")
                    msg=messagebox.showinfo("The Lemma is",'ল')
                elif w == 'থকা':
                    #print('The verb is: থাক')
                    L2.config(text=" The Lemmas are:"+"থাক")
                    msg=messagebox.showinfo("The Lemma is",'থাক')
                elif w == 'ৰুৱা' or w == 'ৰুইছিল' or w == 'ৰুইছ' or w == 'ৰুইছে' or w == 'ৰুব' or w == 'ৰুইছা' or w == 'ৰুবা' or w == 'ৰুবি' or w == 'ৰুলা' or w == 'ৰুলে' or w == 'ৰুলি' or w == 'ৰুইছিলা' or w == 'ৰুইছিলি':
                    #print('The verb is : ৰো')
                    L2.config(text=" The Lemmas are:"+"ৰো")
                    msg=messagebox.showinfo("The Lemma is",'ৰো')
                elif w == 'আহা' or w == 'আহক' or w == 'আহিছা' or w == 'আহিছিলা' or w == 'আহিছিলি' or w == 'আহিছিলে' or w == 'আহিছিল' or w == 'আহিছিলো' or w == 'আহিব' or w == 'আহিবা' or w == 'আহ' or w == 'আহো' or w == 'আহে' or w == 'আহিলোহেতেন' or w == 'আহিলাহেতেন' or w == 'আহিলিহেতেন':
                    #print('The verb is: অহা')
                    L2.config(text=" The Lemmas are:"+"অহা")
                    msg=messagebox.showinfo("The Lemma is",'অহা')
                else:
                    d=[]
                    b=open(r'H:\Project code wid GUI\appendText.txt','w+',encoding='UTF16')
                    w=E1.get()
                    L3.config(text="The sentence is"+w)
                    a=w.split(" ")
                    c=list(w)
                    print(c)
                    #print(a)
                    #c=list(w)
                    #print(a)

                    #strategy for the inflected words with structural change
                    
                    if c[-1]=='য' or c[-1]=='য়' and c[-2]=='্':         
                        del c[1]
                        del c[-2: ]
                        r=[s for s in c if s != 'য']
                        r.append('া')
                        print(r)
                        i=''.join(r)
                        j=trie.contains(i)
                        d.append(''.join(j))
                        #print(d)
                        #b.write(''.join(j)+" ")
                        #c=b.read()
                        L2.config(text=" The Lemmas are:"+str(d)+ " ")
                        msg=messagebox.showinfo("The Lemmas are",d)
                        print(i)
                    
                    
                    else:
                        for p in a:
                            f=[]
                            f=trie.contains(p)      #searching in trie
                            d.append(''.join(f))
                            #print(d)
                            b.write(''.join(f)+" ")
                            #c=b.read()
                            L2.config(text=" The Lemmas are:"+str(d)+ " ")
                            msg=messagebox.showinfo("The Lemmas are",d)#addition of space after the lemma
                            return f

        else:
            msg=messagebox.showerror("Sorry!","Lemma Not found")
       
    def trial():
        msg2=messagebox.showinfo("TRIE",trie)

    B= Button(top,text="Search",command= btnclick)
    B.grid(row=6,column=2)
    B2= Button (top,text="Show Trie",command=trial)
    B2.grid(row=6,column=1)
    #c=btnclick()
    #print(c)
    #E2 = Label(top, text="c")
    #E2.grid(row=4,column=3)    
    

    top.mainloop()

    '''w=input('Enter the word:')
    p=trie.contains(w)
    print(p)
    k.close()'''
