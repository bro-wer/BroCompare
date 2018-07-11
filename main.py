from src.interface import Interface
from settings.generalSettings import generalSettingsDict


if __name__ == '__main__':
    myinterface = Interface(generalSettingsDict)
    myinterface.run()
