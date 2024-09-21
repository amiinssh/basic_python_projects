import wikipedia
from tkinter import *


def on_press():
    q = get_q.get()
    
    text.delete(1.0, END)
    
    try:
        summary = wikipedia.summary(q)
        text.insert(INSERT, summary)
    except wikipedia.exceptions.DisambiguationError as e:
        text.insert(INSERT, "Disambiguation Error: Multiple entries found for this term.")
    except wikipedia.exceptions.PageError:
        text.insert(INSERT, "Error: No page found for this query.")
    except Exception as e:
        text.insert(INSERT, f"An error occurred: {e}")

root = Tk()
root.title("WIKI Search App")

question = Label(root, text='Enter search term:')
question.pack()

get_q = Entry(root, bd=5)
get_q.pack()

submit = Button(root, text="Search", command=on_press)
submit.pack()

text = Text(root, height=20, width=60)
text.pack()

root.mainloop()
