word= input("Enter your word: ")
word= word.lower()
r= len(word)
vowels= 0

for i in range(r):
    if word[i]=="a" or word[i]=="e" or word[i]=="i" or word[i]=="o" or word[i]=="u":
        vowels+=1

if vowels== 1: print( str(vowels) + " vowel")
else: print(str(vowels)+ " vowels")