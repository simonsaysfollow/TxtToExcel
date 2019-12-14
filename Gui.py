import tkinter as tk
import Decoder



def createGUI():
    root = tk.Tk() 
    root.title('Excel Parser') 
    canvas1 = tk.Canvas(root, width = 300, height = 300) 
    canvas1.configure(bg='blue') 
    canvas1.pack()
    button1 = tk.Button(root, text='RUN', width=25, highlightbackground='#3E4149', command=readThePage)
    canvas1.create_window(150, 150, window=button1)   
    root.mainloop()


def readThePage():
    Decoder.decode("test.txt")
    

def clearTheTxtPage():
     open("test.txt","w")


def main() :
    createGUI() 
    # clearTheTxtPage()

if __name__ == '__main__':

    main()
    
