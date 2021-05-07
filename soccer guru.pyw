import tkinter as tk
import pyautogui as ag
import pygetwindow as gt
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.close = False
        self.x1 = self.y1 = self.x2 = self.y2 = 0

    def create_widgets(self):
        self.msg = tk.Label(text="É hora de coletar sua recompensa")
        self.colect = tk.Button(self, text="coletar agora",command=self.colect, fg='green')
        self.wait = tk.Button(self, text="Agora não",command=self.wait, fg='red')
        self.close = tk.Button(self, text="Fechar",command=self.close)

        self.msg.pack()
        self.colect.pack()
        self.wait.pack()
        self.close.pack()
        
        self.master.after(30000, self.finish_time)

    def which_window(self, window):
        window = gt.getWindowsWithTitle(window)[0]
        window.activate()
        window.maximize()
        if window.bottomright[0] < 1000:
            self.x1 = -1320
            self.y1 = 110

            self.x2 = -1150
            self.y2 = 300
        else:
            self.x1 = 30
            self.y1 = 110

            self.x2 = 120
            self.y2 = 300
        
    def colect(self):
        ag.press('winleft')
        time.sleep(0.5)
        ag.typewrite('discord')
        time.sleep(0.5)
        ag.press('enter')
        time.sleep(3)

        self.which_window('Discord')
        
        ag.moveTo(self.x1, self.y1)
        time.sleep(1)
        ag.click()

        ag.moveTo(self.x2, self.y2)
        time.sleep(1)
        ag.click()

        time.sleep(1)
        ag.typewrite('sg!arena')
        time.sleep(1)
        ag.press('enter')

        time.sleep(2.5)
        ag.typewrite('1')
        time.sleep(0.5)
        ag.press('enter')

        time.sleep(1)
        ag.typewrite('sg!claim')
        time.sleep(1)
        ag.press('enter')

        self.master.destroy()
    
    def wait(self):
        self.master.destroy()
    
    def close(self):
        self.close = True
        self.master.destroy()

    def finish_time(self):
        self.colect()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

while not app.close:
    time.sleep(3600)
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

