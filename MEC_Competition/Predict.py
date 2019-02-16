import autocomplete as aa

class Textpredict:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        aa.load()
    
    
    def result(self):
        result = []
        prelist = aa.predict(self.x,self.y)
        if len(prelist)>3:
            for i in range(3):
                result+= [prelist[i][0]]
        else:
            for ele in prelist:
                result += [ele[0]]
        return result

    

            




