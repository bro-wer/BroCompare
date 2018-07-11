from tkinter import *
import os

class ViewPanel(object):
    """
    ViewPanel is a parent for the following classes:
     - DirViewPanel
     - EmptyViewPanel
     - FileViewPanel

    This class is not meant to be used directly - It should be accessed via the
    subclasses only.
    """

    def __init__(self, analyzePath, master):
        self.analyzePath = analyzePath
        self.frame = None
        self.master = master
        self.__load_images()
        self._prepareFrame()


    def __load_images(self):
        self.greenPlusPhoto=PhotoImage(file=os.path.join("src", "images", "green_plus.png"))

    def _prepareFrame(self):
        self.frame = LabelFrame(self.master,)
        self._prepareFrameTopPart()
        self._prepareFrameBottomPart()

    def _prepareFrameTopPart(self):
        print("ViewPanel: _prepareFrameTopPart()")
        self.frameTopPart = Frame(self.frame)

        self.open_button = Button(self.frameTopPart, text="Open", command=self.openButtonAction)
        self.open_button.config(image=self.greenPlusPhoto,width="30",height="30")
        self.open_button.pack(side=LEFT)

        self.close_button = Button(self.frameTopPart, text="Close", command=self.closeButtonAction)
        self.close_button.pack(side=LEFT)

        self.frameTopPart.pack(side=TOP)

    def _prepareFrameBottomPart(self):
        print("ViewPanel: _prepareFrameBottomPart()")
        self.frameBottomPart = Frame(self.frame, bg="yellow", height=250, width=300)
        self.frameBottomPart.pack(side=BOTTOM)

    def addFrameToMaster(self):
        return self.frame.pack(side=LEFT)

    def openButtonAction(self):
        print("Open button clicked!!")

    def closeButtonAction(self):
        print("Close button clicked!!")
