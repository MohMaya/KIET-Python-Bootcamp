sentence = input("Enter Your Text : ")
first = sentence.split()
final = first[::-1]
print(final)
final = " ".join(final)
print(final)
