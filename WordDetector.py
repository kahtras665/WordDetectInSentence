# Word detector program in Python

import time  # importing time function for slowing down printing process to give it a cool looking effect

# importing the dictionary which is originally a text file containing words (you could better call it a wordlist)
f= open('Your Wordlist.txt File Location')
text = f.readlines()  # reading all lines of the wordlist
list= []
[list.append(line.rstrip("\n"))for line in text]  # removing the "\n" which was caused while the conversion process where we converted the text to the list
list = [x.casefold() for x in list]  # converting all the items or elements in the list to lowercase items/elements

# Taking input from the user
print("Word Detector program will detect the specific words in the sentence.")
s= input("Enter a Sentence: ")
s= s.lower()  # converting the entered string lowercase
l= len(s)

# Matching the entered string with the list formed using the wordlist/dictionary
res = [ele for ele in list if(ele in s)]  # keeping the matched words in this variable as list

# Printing the result
print()
count=1
print("Words in the entered sentence are: ")
for i in res:
    le = len(i)  # calculating the length of each matched word 
    if le>2:  # if the length of the matched word is greater than two characters, then it will be printed
        print(count,i)
        time.sleep(0.75) # delaying each print by 0.75 seconds
        count+=1 # counting the number of matched words