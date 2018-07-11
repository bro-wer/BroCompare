from .viewPanel import ViewPanel

class FileViewPanel(ViewPanel):
    """docstring for FileViewPanel."""

    def __init__(self, analyzePath, master):
        print("FileViewPanel: creating new instance")
        ViewPanel.__init__(self, analyzePath, master = master)
