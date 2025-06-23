Amount =int(input("please enter amount of withdraw:"))

#calculating the number of notes of different domination
note_1= Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("notes of 100 ruppes",note_1)
print("notes of 50 ruppes",note_2)
print("notes of 10 ruppes",note_3)