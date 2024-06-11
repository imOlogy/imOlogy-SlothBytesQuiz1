def count_vowels():
    word= input("Enter your word: ")
    word= word.lower()
    r= len(word)
    vowels= 0
    for i in range(r):
        if word[i]=="a" or "e" or "i" or "o" or "u":
            vowels+=1

    if vowels== 1: print(str(vowels) + " vowel")
    else: print(str(vowels)+ " vowels")

count_vowels()