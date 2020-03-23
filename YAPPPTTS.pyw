import tkinter as tk
from tkinter import ttk
from tkinter import *
import pickle
from queue import Queue
import threading
import os
import random
import winsound

win = tk.Tk()
win.title("YAPPPTTS")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Stop Message')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Streamlabs')
tabControl.pack(expand=1, fill="both")

label_1 = Label(tab2, text="Streamlabs Access Token")
label_1.grid(row=0, column=0, sticky=W)

label_2 = Label(tab2, text="Minimum donation for Sound")
label_2.grid(row=6, column=0, sticky=W)

btn1t2 = ttk.Entry(tab2, show="•")
btn1t2.grid(row=1, column=0, sticky=W)


def savevalue():
    firstminvalue = float(btn2t2.get())
    twodec = ("{:.2f}".format(firstminvalue))
    pickle_out = open("minvalue.pickle", "wb")
    pickle.dump(twodec, pickle_out)
    pickle_out.close()

btn4t2 = Button(tab2, text="Save Minimum Donation Value", command=savevalue)
btn4t2.grid(row=9, sticky=W)

def savekey():
    thekey = btn1t2.get()
    pickle_out = open("savekey.pickle", "wb")
    pickle.dump(thekey, pickle_out)
    pickle_out.close()

try:
    pickle_in = open("savekey.pickle","rb")
    thekey = pickle.load(pickle_in)
    btn1t2.insert(tk.END, thekey)
except EOFError:
    pass
except IOError:
    pass

button1 = Button(tab2, text="Connect", command=savekey)
button1.grid(row=2,column=0, sticky=W)

btn2t2 = ttk.Entry(tab2)
btn2t2.grid(row=7, column=0, sticky=W)

q = Queue()
qname = Queue()
previousid = [0]
for x in previousid:
    def donations():
        global previousid
        threading.Timer(1, donations).start()
        global q
        global qname
        import requests
        try:
            url = "https://streamlabs.com/api/donations"
            querystring = {"access_token": {"" + btn1t2.get() + ""}}
            response = requests.request("GET", url, params=querystring)
            test = str(response.text)
            EndMessage = test.split('{')[-2] + test.split('{')[-1]
        except IndexError:
            pass
        try:
            minvalue = float(btn2t2.get())
            MinMin = EndMessage.split(',')
            MinMin = MinMin[2].split('"')
            MinMin = float(MinMin[3])
            if MinMin >= minvalue:
                text = EndMessage.split(',"')
                currentid = text[0].split(':')
                currentid = int(currentid[1])
                if currentid != previousid:
                    global MessageInsertFixed1
                    global MessageInsertFixed
                    Tester = str(text)
                    Inserter = Tester.split(", '")
                    PrintofMessage = Inserter[7].split('"')
                    MessageInsert = PrintofMessage[2]
                    MessageInsertFixed = MessageInsert.replace("""\\\\/""" """\\\\\\\\""", "Slash")
                    MessageInsertFixed = MessageInsertFixed.replace("*", "")
                    length = len(MessageInsertFixed)
                    previousid = currentid
                    if length <= 5:
                        winsound.PlaySound("lessthan5-" + str(random.randint(1,4)) + ".wav", winsound.SND_ASYNC)
                    if (length > 5) and (length <= 30):
                        winsound.PlaySound("lessthan30-" + str(random.randint(1, 3)) + ".wav", winsound.SND_ASYNC)
                    if (length > 30) and (length <= 60):
                        winsound.PlaySound("lessthan60-" + str(random.randint(1, 4)) + ".wav", winsound.SND_ASYNC)
                    if (length > 60) and (length <= 120):
                        winsound.PlaySound("lessthan120-" + str(random.randint(1, 4)) + ".wav", winsound.SND_ASYNC)
                    if (length > 120) and (length <= 250):
                        winsound.PlaySound("lessthan120-" + str(random.randint(1, 4)) + ".wav", winsound.SND_ASYNC)
                    if length > 250:
                        winsound.PlaySound("lessthan120-" + str(random.randint(1, 4)) + ".wav", winsound.SND_ASYNC)
        except ValueError:
            print(ValueError)

def stopkey():
    winsound.PlaySound(None, winsound.SND_PURGE)

btn3t1 = Button(tab1, text="Stop Message", command=stopkey)
btn3t1.grid(sticky=SW)

donations()

try:
    pickle_in = open("minvalue.pickle", "rb")
    firstminvalue = pickle.load(pickle_in)
    btn2t2.insert(tk.END, firstminvalue)
except EOFError:
    pass
except IOError:
    pass

win.mainloop()