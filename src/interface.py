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

    def __initRightPanel(self):
        self.rightPanel = EmptyViewPanel(master = self.top)
        self.rightPanel.addFrameToMaster()

    def run(self):
        self.top.mainloop()
