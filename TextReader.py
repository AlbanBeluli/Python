import pyttsx3
book=open(r"book.txt")
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
    
# Create a book.txt file - add text to it and run the app. Enjoy listening.
