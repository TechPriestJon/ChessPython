class State:
    def __init__(self):
    #    alive = True
        self.__labelValue = "Some Words"

    def setLabelValue(self, labelText):
        self.__labelValue = labelText

    def labelValue(self):
        return self.__labelValue