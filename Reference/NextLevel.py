filename = 'Lemma/OutPut.txt'
mynumbers = []
with open(filename) as f:
    for line in f:
        mynumbers.append([int(n) for n in line.strip().split(',')])
for pair in mynumbers:
    try:
        #x is the file name
        #y is the percent number
        x,y = pair[0],pair[1]
        # Do Something with x and y
    except IndexError:
        print ("A line in the file doesn't have enough entries.")

min_percent = min(y)
min_index = y.index(min_percent)

from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#84BF04')

message = f"Your next book at your reading level is {x[min_index]}"

text_box = Text(
    ws,
    height=12,
    width=40
)
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')

ws.mainloop()