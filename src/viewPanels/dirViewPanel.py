from .viewPanel import ViewPanel

class DirViewPanel(ViewPanel):
    """docstring for DirViewPanel."""

    def __init__(self, analyzePath, master):
        print("DirViewPanel: creating new instance")
        ViewPanel.__init__(self, analyzePath, master = master)
