# Wikipedia application

from tkinter import *
import wikipedia

app = Tk()
app.title('MyWikiApp')
app.geometry('1600x1080')


def wikisearch():
    user_response = entryTopic.get()
    result = wikipedia.summary(user_response, sentences=10)
    labelWiki.config(text=result)

def reset():
    entryTopic.delete(0, END)
    labelWiki.config(text='')

#print ('My Wiki App')

entryTopic = Entry(app, width=50)
entryTopic.place(x=100,y=45)

buttonGetWiki = Button(app, text='Get Wiki', font='Arial, 16', width=10, command=wikisearch)
buttonGetWiki.place(x=100, y=70)

buttonReset = Button(app, text='Reset', font='Arial, 16', width=10, command=reset)
buttonReset.place(x=300, y=70)

buttonQuit = Button(app, text='Quit', font='Arial, 16', width=10, command=quit)
buttonQuit.place(x=500, y=70)


labelWiki = Label(app, font='Arial, 10', borderwidth=3, relief='groove', height=30, width=80, anchor='n', wraplength=1000, justify='center')
labelWiki.place(x=100,y=120)

#print ('Complete!')


app.mainloop()
