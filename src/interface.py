from tkinter import *
import os
class Interface(object):
    """docstring for Interface."""
    def __init__(self, settingsDict):
        self.top = Tk()
        self.top.title("{} ver. {}".format(settingsDict["title"], settingsDict["version"]))
        self.__load_images()
        self.__initTopFrame()
        self.__initLeftPanel()
        self.__initRightPanel()

#x1=Button(root)
#photo=PhotoImage(file="Re.png")
#x1.config(image=photo,width="40",height="40",activebackground="black"
#,bg="black", bd=0,command=sil)


    def __load_images(self):
        self.greenPlusPhoto=PhotoImage(file=os.path.join("src", "images", "green_plus.png"))

    def __initTopFrame(self):
        self.topFrame = Frame(self.top)
        self.topFrame.pack(side = TOP)
        greet_button = Button(self.topFrame, text="Greet", command=self.greet)
        greet_button.config(image=self.greenPlusPhoto,width="30",height="30")
        greet_button.pack(side=LEFT)
        greet_button = Button(self.topFrame, text="Greet", command=self.greet)
        greet_button.pack(side=LEFT)
        greet_button = Button(self.topFrame, text="Greet", command=self.greet)
        greet_button.pack(side=LEFT)
        close_button = Button(self.topFrame, text="Close", command=self.top.quit)
        close_button.pack()

    def __initLeftPanel(self):
        leftPanel = LabelFrame(self.top, bg="brown", height=500, width=300)
        leftPanel.pack(side=LEFT)

    def __initRightPanel(self):
        rightPanel = LabelFrame(self.top, bg="blue", height=500, width=300)
        rightPanel.pack(side=RIGHT)

    def run(self):
        self.top.mainloop()

    def greet(self):
        print("Greetings!")
