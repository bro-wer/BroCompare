from .viewPanel import ViewPanel
from tkinter import *
import os

class EmptyViewPanel(ViewPanel):
    """docstring for EmptyViewPanel."""

    def __init__(self, master):
        print("EmptyViewPanel: creating new instance")
        self.currentPath = os.getcwd()
        ViewPanel.__init__(self, analyzePath = None, master = master)


    def _prepareFrameBottomPart(self):
        """Overwrite for parent function"""
        print("EmptyViewPanel: _prepareFrameBottomPart()")
        #self.frameBottomPart = Frame(self.frame, bg="green", height=250, width=300)
        self.frameBottomPart = Frame(self.frame, bg="green")
        self._renderFilesDirsFromCurrentPath()

        # self.kurdePrzypalPhoto = PhotoImage(file=os.path.join("src", "images", "kurde_przypal.png"))
        # self.background_label = Label(self.frameBottomPart, image=self.kurdePrzypalPhoto)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frameBottomPart.pack(side=BOTTOM)

    def _renderFilesDirsFromCurrentPath(self):
        # filesDirsList = self._getFilesDirsFromCurrentPath()
        tmpCounter = 0

        for dirname in self._getDirsFromCurrentPath():
            icon = Button(self.frameBottomPart, text="dirIcon")
            icon.config(image=self.closedDirPhoto,width="30",height="30")
            icon.grid(column = 0, row=tmpCounter)
            Label(self.frameBottomPart, text=dirname, font=30, anchor='w').grid(column = 1, row=tmpCounter)
            tmpCounter += 1

        for filename in self._getFilesFromCurrentPath():
            icon = Button(self.frameBottomPart, text="dirIcon")
            icon.config(image=self.fileIcon,width="30",height="30")
            icon.grid(column = 0, row=tmpCounter)
            Label(self.frameBottomPart, text=filename, font=30, anchor='w').grid(column = 1, row=tmpCounter)
            tmpCounter += 1


    # def _getFilesDirsFromCurrentPath(self):
    #     response = {}
    #     response["dirsList"] = self._getDirsFromCurrentPath()
    #     response["filesList"] = self._getFilesFromCurrentPath()
    #     print('\nresponse["dirsList"]')
    #     for elem in response["dirsList"]:
    #         print(str(elem))
    #     print('\nresponse["filesList"]')
    #     for elem in response["filesList"]:
    #         print(str(elem))
    #     return response

    def _getDirsFromCurrentPath(self):
        dirsList = [f for f in os.listdir(self.currentPath) if not os.path.isfile(f)]
        return dirsList

    def _getFilesFromCurrentPath(self):
        filesList = [f for f in os.listdir(self.currentPath) if os.path.isfile(f)]
        return filesList
