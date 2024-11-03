
class circle:
    def __init__(self, id,widthPosition,heigthPosition):
        self.id=id
        self.widthPosition=widthPosition
        self.heigthPosition=heigthPosition


    def getId(self):
        return self.id
    
    def setId(self, value):
        self.id = value

    def getWidthPosition(self):
        return self.widthPosition

    def setWidthPosition(self, value):
        self.widthPosition = value

    def getHeigthPosition(self):
        return self.heigthPosition

    def setHeigthPosition(self, value):
        self.heigthPosition = value