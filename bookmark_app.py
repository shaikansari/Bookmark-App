from tkinter import *
import webbrowser
import tkinter.messagebox

window = Tk()
window.title('Bookmark App')

def youtube_func():
	answer = tkinter.messagebox.askquestion('Alert!!', 'Do you really want to open YouTube in work hours?')
	if answer == 'yes':
		webbrowser.open_new_tab('https://www.youtube.com')

def facebook_func():
	answer = tkinter.messagebox.askquestion('Alert!!', 'Do you really want to open Facebook in work hours?')
	if answer == 'yes':
		webbrowser.open_new_tab('https://www.facebook.com')

def cleverprogrammer_func():
	webbrowser.open_new_tab('https://www.cleverprogrammer.com/library')

def sentdex_func():
	webbrowser.open_new_tab('https://pythonprogramming.net/search/?q=regular+expressions')

def dataschool_func():
	webbrowser.open_new_tab('http://www.dataschool.io/')

def quora_func():
	webbrowser.open_new_tab('https://www.quora.com/')

def im_func():
	webbrowser.open_new_tab('https://flextronics365.sharepoint.com/sites/itgso/sg/team/Matrix/IM%20-%20Coverage%20Matrix.pdf')

def sharepoint_func():
	webbrowser.open_new_tab('https://flextronics365.sharepoint.com/sites/pna_it_warehouse/gbs_support/Shared%20Documents/GMC%20Documentation')

def tp_func():
	webbrowser.open_new_tab('https://www.tutorialspoint.com/python3/index.htm')

def coursera_func():
	webbrowser.open_new_tab('https://www.coursera.org/')

def datacamp_func():
	webbrowser.open_new_tab('https://www.datacamp.com/home')

def hackerearth_func():
	webbrowser.open_new_tab('https://www.hackerearth.com/challenges/')

def hackerrank_func():
	webbrowser.open_new_tab('https://www.hackerrank.com/challenges/write-a-function/problem')

def udemy_func():
	webbrowser.open_new_tab('https://www.udemy.com/home/my-courses/learning/')

def udacity_func():
	webbrowser.open_new_tab('https://in.udacity.com/courses/all')

def freecodecamp_func():
	webbrowser.open_new_tab('https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567')

def thenewboston_func():
	webbrowser.open_new_tab('https://thenewboston.com/videos.php?cat=98')

def stackoverflow_func():
	webbrowser.open_new_tab('https://stackoverflow.com/questions')

def zerotohero_func():
	webbrowser.open_new_tab('https://gitter.im/Pierian-Data-Courses-Community/Lobby')

def donothing1_func():
	pass

def donothing2_func():
	pass

frame = Frame(window, width =300, height = 300)
frame.pack()

button_1 = Button(frame, text = 'Tutorial Point', fg = 'red', bg='white', borderwidth = 1, command = tp_func)
button_1.grid(row = 0 , column = 0)

button_2 = Button(frame, text = 'Incident Manager', fg = 'blue', bg='white', command = im_func)
button_2.grid(row = 0 , column = 1)

button_3 = Button(frame, text = 'Quora Page', fg = 'green', bg='white', command = quora_func)
button_3.grid(row = 0 , column = 2)

button_4 = Button(frame, text = 'Udemy Page', fg = 'red', bg='white', command = udemy_func)
button_4.grid(row = 1 , column = 0)

button_5 = Button(frame, text = 'Coursera Home Page', fg ='blue', bg = 'white', command = coursera_func)
button_5.grid(row = 1 , column = 1)

button_6 = Button(frame, text = 'Udacity Page', fg ='green', bg = 'white', command = udacity_func)
button_6.grid(row = 1 , column = 2)

button_7 = Button(frame, text = 'Hacker Earth', fg ='red', bg = 'white', command = hackerearth_func)
button_7.grid(row = 2 , column = 0)

button_8 = Button(frame, text = 'Hacker Rank Page', fg ='blue', bg = 'white', command = hackerrank_func)
button_8.grid(row = 2 , column = 1)

button_9 = Button(frame, text = 'Data Camp', fg ='green', bg = 'white', command = datacamp_func)
button_9.grid(row = 2 , column = 2)

button_10 = Button(frame, text = 'Programmer', fg ='red', bg = 'white', command = cleverprogrammer_func)
button_10.grid(row = 3 , column = 0)

button_11 = Button(frame, text = 'Sentdex Home Page', fg ='blue', bg = 'white', command = sentdex_func)
button_11.grid(row = 3 , column = 1)

button_12 = Button(frame, text = 'Data School', fg ='green', bg = 'white', command = dataschool_func)
button_12.grid(row = 3 , column = 2)

button_13 = Button(frame, text = 'Freecodecamp', fg = 'red', bg = 'white', command = freecodecamp_func)
button_13.grid(row = 4, column = 0)

button_14 = Button(frame, text = 'Thenewboston', fg = 'blue', bg = 'white', command = thenewboston_func)
button_14.grid(row = 4, column = 1)

button_15 = Button(frame, text = 'Stackoverflow', fg = 'green', bg = 'white', command = stackoverflow_func)
button_15.grid(row = 4, column = 2)

button_16 = Button(frame, text = 'Zero to Hero chat', fg = 'red', bg = 'white', command = zerotohero_func)
button_16.grid(row = 5, column = 0)

button_17 = Button(frame, text = 'donothing1', fg = 'blue', bg = 'white', command = donothing1_func)
button_17.grid(row = 5, column = 1)

button_18 = Button(frame, text = 'donothing2', fg = 'green', bg = 'white', command = donothing2_func)
button_18.grid(row = 5, column = 2)

button_19 = Button(frame, text = 'YouTube', fg='brown', bg='white', command = youtube_func)
button_19.grid(row = 6, column = 0, columnspan = 2)

button_20 = Button(frame, text = 'Facebook', fg='purple', bg='white', command = facebook_func)
button_20.grid(row = 6, column = 1, columnspan = 2)

window.mainloop()
