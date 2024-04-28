class GameElement:
    def __init__(self,X,Y,W,H,IFN): # constructor
        self.__PositionX = X
        self.__PositionY = Y
        self.__Width = W
        self.__Height = H
        self.__ImageFileName = IFN
    
    def GetDetails(self):
        myStr  = ''
        myStr = 'PositionX: ' + str(self.__PositionX) + '\n' + 'PositionY: ' + str(self.__PositionY) + '\n' + 'Width: ' + str(self.__Width) + '\n' + 'Height: ' + str(self.__Height) + '\n' + 'ImageFileName: ' + self.__ImageFileName
        return myStr

class Scenery(GameElement):
    def __init__(self,X,Y,W,H,IFN,CD,DP):
        super().__init__(X,Y,W,H,IFN)
        self.__CauseDamage = CD
        self.__DamagePoints = DP
    
    def GiveDamagePoints(self):
        if self.__CauseDamage:
            return self.__DamagePoints
        else:
            return 0
    
    def GetScenery(self): # returns a string with all the details of the scenery
        myStr = ''
        myStr = super().GetDetails() + '\n' + 'CauseDamage: ' + str(self.__CauseDamage) + '\n' + 'DamagePoints: ' + str(self.__DamagePoints)
        return myStr

# INSTANTIATION OF GiftBox Scenery Object.
GiftBox = Scenery(150, 150, 50, 75, "box.png", True, 50)

print(GiftBox.GetScenery())