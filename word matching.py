#function to check weather
#first and last character of word match
def match_word(words):
    ctr = 0
    lst = [] 
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("List of word with first and last character same\n" ,lst)         
    return ctr
    
count = match_word(['abc' , 'lbcc' , '1221' , 'mabc'])
print("Number of word having first and last character same:",count) 