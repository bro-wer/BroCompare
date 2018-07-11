from tkinter import *
import os

from src.viewPanels.dirViewPanel import DirViewPanel
from src.viewPanels.emptyViewPanel import EmptyViewPanel
from src.viewPanels.fileViewPanel import FileViewPanel

class Interface(object):
    """docstring for Interface."""
    def __init__(self, settingsDict):
        self.top = Tk()
        self.top.title("{} ver. {}".format(settingsDict["title"], settingsDict["version"]))
        self.__initLeftPanel()
        self.__initRightPanel()

    def __initTopFrame(self, master):
        pass

    def __initLeftPanel(self):
        self.leftPanel = EmptyViewPanel(master = self.top)
        self.leftPanel.addFrameToMaster()
        # self.leftPanel = LabelFrame(self.top, bg="brown", height=500, width=300)
        # topPart = LabelFrame(self.leftPanel, bg="blue", height=250, width=300)
        # bottomPart = LabelFrame(self.leftPanel, bg="yellow", height=250, width=300)

        # self.__initTopFrame(master = topPart)

        # topPart.pack(side=TOP)
        # bottomPart.pack(side=TOP)
        # self.leftPanel.pack(side=LEFT)

    def __initRightPanel(self):
        self.rightPanel = EmptyViewPanel(master = self.top)
        self.rightPanel.addFrameToMaster()
        # rightPanel = LabelFrame(self.top, bg="pink", height=500, width=300)
        # rightPanel.pack(side=RIGHT)

    def run(self):
        self.top.mainloop()
