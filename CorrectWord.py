from textblob import TextBlob
a=input("Enter Incorrect Word:")
print("Original Word:"+str(a))
b = TextBlob(a)
print("Corrected Word:"+str(b.correct()))
