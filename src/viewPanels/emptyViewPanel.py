from .viewPanel import ViewPanel
from tkinter import *
import os

class EmptyViewPanel(ViewPanel):
    """docstring for EmptyViewPanel."""

    def __init__(self, master):
        print("EmptyViewPanel: creating new instance")
        ViewPanel.__init__(self, analyzePath = None, master = master)


    def _prepareFrameBottomPart(self):
        """Overwrite for parent function"""
        print("EmptyViewPanel: _prepareFrameBottomPart()")
        self.frameBottomPart = Frame(self.frame, bg="green", height=250, width=300)

        self.kurdePrzypalPhoto = PhotoImage(file=os.path.join("src", "images", "kurde_przypal.png"))
        self.background_label = Label(self.frameBottomPart, image=self.kurdePrzypalPhoto)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frameBottomPart.pack(side=BOTTOM)
