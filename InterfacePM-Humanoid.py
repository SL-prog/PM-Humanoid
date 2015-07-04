import serial
from tkinter import *

class Window(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=870, height=556, **kwargs)
        self.master = master

        self.photo = PhotoImage(file="pm.gif")
        self.canvas = Canvas(self,width=520, height=556)
        self.canvas.create_image(260,278, image=self.photo)
        self.canvas.pack()

        self.terminal = Canvas(self, width=350, height=556, bg='black')
        self.terminal.pack()
        self.terminal.create_text(50,10,text='Servo_tete_x : 80',fill="white")
        self.terminal.create_text(50,30,text='Servo_tete_y : 63',fill="white")

        self.terminal.create_text(45,545,text='Baud : 9600',fill="white")
        self.terminal.create_text(305,545,text='Port : COM8',fill="white")

        self.canvas.grid(column=1,row=1)

        self.terminal.grid(column=2,row=1)


        self.A = Scale(master, from_=0, to=180,showvalue=0, orient=HORIZONTAL,length=80,width=15,activebackground="ivory",command=self.msg)
        self.A.pack()
        self.A_window = self.canvas.create_window(236, 48, window=self.A)

        self.test2 = Scale(master, from_=0, to=180, orient=VERTICAL)
        self.test2.pack()
        self.test2_window = self.canvas.create_window(500, 10, anchor=NW, window=self.test2)

        self.tetex1 = Button(self, text="+", command=self.msg )
        self.tetex1.pack(side="bottom", fill=BOTH)
        self.tetex1_window = self.canvas.create_window(236, 48, anchor=NW, window=self.tetex1)
        self.tetex2 = Button(self, text="-", command=self.msg )
        self.tetex2.pack(side="bottom", fill=BOTH)
        self.tetex2_window = self.canvas.create_window(236, 75, anchor=NW, window=self.tetex2)

        self.tetey1 = Button(self, text="+", command=self.msg )
        self.tetey1.pack(side="bottom", fill=BOTH)
        self.tetey1_window = self.canvas.create_window(295, 85, anchor=NW, window=self.tetey1)
        self.tetey2 = Button(self, text="-", command=self.msg )
        self.tetey2.pack(side="bottom", fill=BOTH)
        self.tetey2_window = self.canvas.create_window(315, 85, anchor=NW, window=self.tetey2)

        self.LED_state = True
        #self.serial = serial.Serial(port="COM8")

    def msg(self):
        if self.LED_state:
            self.serial.write(bytes('a', encoding="utf-8"))
        else:
            self.serial.write(bytes('z', encoding="utf-8"))
        self.LED_state = not self.LED_state

if __name__ == '__main__':
    fen = Tk()

    w = Window(fen)
    w.pack()


    fen.mainloop()