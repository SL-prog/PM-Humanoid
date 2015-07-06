import serial
import sys
import glob
from tkinter import *

class Window(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, width=600, height=400, **kwargs)
        self.serial = serial.Serial(port="COM8",baudrate=9600)

        self.master = master

        self.photo = PhotoImage(file="pm.gif")
        self.canvas = Canvas(self,width=550, height=588, bg='cyan')
        self.canvas.create_image(275,294, image=self.photo)
        self.canvas.pack()
        self.canvas.grid(column=1,row=1)

        self.terminal = Canvas(self, width=198, height=588, bg='black')
        self.terminal.pack()
        self.terminal.grid(column=2,row=1)
        self.terminal.create_text(45,573,text='Baud : 9600',fill="white")
        self.terminal.create_text(160,573,text='Port : COM8',fill="white")
#----------------
        self.tete_x = StringVar()
        self.A = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.tete_x, command=self.MAJA)
        self.A.set(90)
        self.A.pack()
        self.A_window = self.canvas.create_window(232, 18, anchor=NW, window=self.A)

        self.tete_y = StringVar()
        self.B = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.tete_y, command=self.MAJB)
        self.B.set(90)
        self.B.pack()
        self.B_window = self.canvas.create_window(232, 140, anchor=NW, window=self.B)

        self.epauled_x = StringVar()
        self.C = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.epauled_x, command=self.MAJC)
        self.C.set(90)
        self.C.pack()
        self.C_window = self.canvas.create_window(203, 145, anchor=NW, window=self.C)

        self.epauled_y = StringVar()
        self.D = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.epauled_y, command=self.MAJD)
        self.D.set(90)
        self.D.pack()
        self.D_window = self.canvas.create_window(117, 131, anchor=NW, window=self.D)

        self.epauleg_x = StringVar()
        self.E = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.epauleg_x, command=self.MAJE)
        self.E.set(90)
        self.E.pack()
        self.E_window = self.canvas.create_window(317, 145, anchor=NW, window=self.E)

        self.epauleg_y = StringVar()
        self.F = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.epauleg_y, command=self.MAJF)
        self.F.set(90)
        self.F.pack()
        self.F_window = self.canvas.create_window(341, 131, anchor=NW, window=self.F)

        self.couded_y = StringVar()
        self.G = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.couded_y, command=self.MAJG)
        self.G.set(90)
        self.G.pack()
        self.G_window = self.canvas.create_window(60, 90, anchor=NW, window=self.G)

        self.coudeg_y = StringVar()
        self.H = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.coudeg_y, command=self.MAJH)
        self.H.set(90)
        self.H.pack()
        self.H_window = self.canvas.create_window(420, 90, anchor=NW, window=self.H)

        self.hanched_x = StringVar()
        self.I = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.hanched_x, command=self.MAJI)
        self.I.set(90)
        self.I.pack()
        self.I_window = self.canvas.create_window(222, 260, anchor=NW, window=self.I)

        self.hancheg_x = StringVar()
        self.J = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.hancheg_x, command=self.MAJJ)
        self.J.set(90)
        self.J.pack()
        self.J_window = self.canvas.create_window(300, 260, anchor=NW, window=self.J)

        self.hanched_z = StringVar()
        self.K = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.hanched_z, command=self.MAJK)
        self.K.set(90)
        self.K.pack()
        self.K_window = self.canvas.create_window(136, 290, anchor=NW, window=self.K)

        self.hancheg_z = StringVar()
        self.L = Scale(master, from_=0, to=180, orient=HORIZONTAL, length=80, showvalue=0, variable=self.hancheg_z, command=self.MAJL)
        self.L.set(90)
        self.L.pack()
        self.L_window = self.canvas.create_window(322, 290, anchor=NW, window=self.L)

        self.genoud_x = StringVar()
        self.M = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.genoud_x, command=self.MAJM)
        self.M.set(90)
        self.M.pack()
        self.M_window = self.canvas.create_window(228, 382, anchor=NW, window=self.M)

        self.genoug_x = StringVar()
        self.N = Scale(master, from_=0, to=180, orient=VERTICAL, length=80, showvalue=0, variable=self.genoug_x, command=self.MAJN)
        self.N.set(90)
        self.N.pack()
        self.N_window = self.canvas.create_window(288, 382, anchor=NW, window=self.N)

#----
        self.ledd = Button(self, text="O", command=self.MAJO )
        self.ledd.pack()
        self.ledd_window = self.canvas.create_window(258, 30, anchor=NW, window=self.ledd)
        self.etat_ledd = True
        self.MAJO()

        self.ledg = Button(self, text="O", command=self.MAJP )
        self.ledg.pack()
        self.ledg_window = self.canvas.create_window(287, 30, anchor=NW, window=self.ledg)
        self.etat_ledg = True
        self.MAJP()

#-------
    def MAJA(self, valeur):
        self.MAJ("A", valeur)
    def MAJB(self, valeur):
        self.MAJ("B", valeur)
    def MAJC(self, valeur):
        self.MAJ("C", valeur)
    def MAJD(self, valeur):
        self.MAJ("D", valeur)
    def MAJE(self, valeur):
        self.MAJ("E", valeur)
    def MAJF(self, valeur):
        self.MAJ("F", valeur)
    def MAJG(self, valeur):
        self.MAJ("G", valeur)
    def MAJH(self, valeur):
        self.MAJ("H", valeur)
    def MAJI(self, valeur):
        self.MAJ("I", valeur)
    def MAJJ(self, valeur):
        self.MAJ("J", valeur)
    def MAJK(self, valeur):
        self.MAJ("K", valeur)
    def MAJL(self, valeur):
        self.MAJ("L", valeur)
    def MAJM(self, valeur):
        self.MAJ("M", valeur)
    def MAJN(self, valeur):
        self.MAJ("N", valeur)
    def MAJO(self):
        self.MAJ("O", None)
    def MAJP(self):
        self.MAJ("P", None)
    #def MAJQ(self, valeur):
        #self.MAJ("Q", valeur)
#-------------
    def MAJ(self, nom, valeur):

        if nom == "A":
            self.terminal.create_rectangle(0, 0, 200, 20, fill="#fb0")
            self.terminal.create_text(100,10,text="A = Servo_tete_x : "+self.tete_x.get(), fill="white")
        if nom == "B":
            self.terminal.create_rectangle(0, 40, 200, 20, fill="#faa")
            self.terminal.create_text(100,30,text="B = Servo_tete_y : "+self.tete_y.get(), fill="white")
        if nom == "C":
            self.terminal.create_rectangle(0, 60, 200, 40, fill="#ab0")
            self.terminal.create_text(100,50,text="C = Servo_epaule_droite_x : "+self.epauled_x.get(), fill="white")
        if nom == "D":
            self.terminal.create_rectangle(0, 80, 200, 60, fill="#cda")
            self.terminal.create_text(100,70,text="D = Servo_epaule_droite_y : "+self.epauled_y.get(), fill="white")
        if nom == "E":
            self.terminal.create_rectangle(0, 100, 200, 80, fill="#370")
            self.terminal.create_text(100,90,text="E = Servo_epaule_gauche_x : "+self.epauleg_x.get(), fill="white")
        if nom == "F":
            self.terminal.create_rectangle(0, 120, 200, 100, fill="#e48")
            self.terminal.create_text(100,110,text="F = Servo_epaule_gauche_y : "+self.epauleg_y.get(), fill="white")
        if nom == "G":
            self.terminal.create_rectangle(0, 140, 200, 120, fill="#b6a")
            self.terminal.create_text(100,130,text="G = Servo_coude_droite_y : "+self.couded_y.get(), fill="white")
        if nom == "H":
            self.terminal.create_rectangle(0, 160, 200, 140, fill="#f9f")
            self.terminal.create_text(100,150,text="H = Servo_coude_gauche_y : "+self.coudeg_y.get(), fill="white")
        if nom == "I":
            self.terminal.create_rectangle(0, 180, 200, 160, fill="#a26")
            self.terminal.create_text(100,170,text="I = Servo_hanche_droite_x : "+self.hanched_x.get(), fill="white")
        if nom == "J":
            self.terminal.create_rectangle(0, 200, 200, 180, fill="#36b")
            self.terminal.create_text(100,190,text="J = Servo_hanche_gauche_x : "+self.hancheg_x.get(), fill="white")
        if nom == "K":
            self.terminal.create_rectangle(0, 220, 200, 200, fill="#0ea")
            self.terminal.create_text(100,210,text="K = Servo_hanche_droite_z : "+self.hanched_z.get(), fill="white")
        if nom == "L":
            self.terminal.create_rectangle(0, 240, 200, 220, fill="#abc")
            self.terminal.create_text(100,230,text="L = Servo_hanche_gauche_z : "+self.hancheg_z.get(), fill="white")
        if nom == "M":
            self.terminal.create_rectangle(0, 260, 200, 240, fill="#6a1")
            self.terminal.create_text(100,250,text="M = Servo_genou_droite_x : "+self.genoud_x.get(), fill="white")
        if nom == "N":
            self.terminal.create_rectangle(0, 280, 200, 260, fill="#4f5")
            self.terminal.create_text(100,270,text="N = Servo_genou_gauche_x : "+self.genoug_x.get(), fill="white")

        if nom == "O":
            self.terminal.create_rectangle(0, 300, 200, 280, fill="#b6d")
            self.terminal.create_text(100,290,text="O = Led_tete_droite : "+str(self.etat_ledd), fill="white")
            self.etat_ledd = not self.etat_ledd
            if self.etat_ledd:
                valeur = 0
            else:
                valeur = 1
        if nom == "P":
            self.terminal.create_rectangle(0, 320, 200, 300, fill="#aa8")
            self.terminal.create_text(100,310,text="P = Led_tete_gauche : "+str(self.etat_ledg), fill="white")
            self.etat_ledg = not self.etat_ledg
            if self.etat_ledg:
                valeur = 0
            else:
                valeur = 1

        #if nom == "Q":
            #self.terminal.create_rectangle(0, 320, 200, 300, fill="#aa8")
            #self.terminal.create_text(100,310,text="Q = Buzzer : "+self.tete_y.get(), fill="white")

        self.envoi(nom,valeur)

    def envoi(self, nom, valeur):
        #print(bytes(nom+str(valeur), encoding="utf-8"))
        self.terminal.create_rectangle(0, 443, 200, 463, fill="white")
        self.terminal.create_text(100,453,text="COM8 : 9600 > "+nom+str(valeur), fill="black")

        self.serial.write(bytes(nom+str(valeur), encoding="utf-8"))

        #try:
        #    if self.LED_state:
        #        self.serial.write(bytes('a', encoding="utf-8"))
        #    else:
        #        self.serial.write(bytes('z', encoding="utf-8"))
        #    self.LED_state = not self.LED_state
        #except:
        #    messagebox.showwarning("Serial port","Mauvais port série !")


if __name__ == '__main__':
    fen = Tk()
    fen.wm_title("Interface PM Humanoid")
    fen.iconbitmap(default='pm.ico')

    w = Window(fen)
    w.pack()

    fen.mainloop()