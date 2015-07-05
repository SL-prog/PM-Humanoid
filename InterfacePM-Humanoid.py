import serial
from tkinter import *

Servo_tete_x = 90
Servo_tete_y = 90

class Window(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=600, height=400, **kwargs)
        self.master = master

        self.photo = PhotoImage(file="pm.gif")
        self.canvas = Canvas(self,width=550, height=588)
        self.canvas.create_image(275,294, image=self.photo)
        self.canvas.pack()

        self.terminal = Canvas(self, width=350, height=588, bg='black')
        self.terminal.pack()

        self.canvas.grid(column=1,row=1)
        self.terminal.grid(column=2,row=1)

        self.A = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable = Servo_tete_x, command=self.envoi)
        self.A.pack()
        self.A_window = self.canvas.create_window(232, 18, anchor=NW, window=self.A)

        self.B = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable = Servo_tete_y, command=self.envoi)
        self.B.pack()
        self.B_window = self.canvas.create_window(232, 140, anchor=NW, window=self.B)


        #self.LED_state = True
        #self.serial = serial.Serial(port="COM8")

        self.envoi()

    def envoi(self):
        #if self.LED_state:
            #self.serial.write(bytes('a', encoding="utf-8"))
        #else:
            #self.serial.write(bytes('z', encoding="utf-8"))
        #self.LED_state = not self.LED_state

        self.terminal.create_text(60,10,text="A = Servo_tete_x : "+str(Servo_tete_x),fill="white")
        self.terminal.create_text(60,30,text="B = Servo_tete_y : "+str(Servo_tete_y),fill="white")

        self.terminal.create_text(45,573,text='Baud : 9600',fill="white")
        self.terminal.create_text(305,573,text='Port : COM8',fill="white")


if __name__ == '__main__':
    fen = Tk()
    fen.wm_title("Interface PM Humanoid")
    fen.iconbitmap(default='pm.ico')

    w = Window(fen)
    w.pack()

    fen.mainloop()