#takes marks a input from users
print("Enter marks obtained in 4 subject:")
math=int(input("maths:"))
english=int(input("english:"))
science=int(input("science:"))
hindi=int(input("hindi:"))

#let's calculate the percentage of marks
sum=math+english+science+hindi
print("sum of math,english,hindi and science")

perc=(sum/400)*100
print(end="percentage mark= ")
print(perc)