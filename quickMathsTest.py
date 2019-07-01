from threading import Timer
import random
from datetime import datetime 

class quickMathsTest :
    globalFlag = False
    
    def timeRanOut(self):
        ''' 
        Invoked when the timer runs out
        '''
        self.globalFlag = True
        print("\n Timeout Reached. But you can enter answer \t :")
    
    
    ''' Op_sign 
    0 - Addition
    1 - Subtraction
    2 - Multiplication
    3 - Division '''
    op_sign = ["+", "-", "*", "//"]
    questionList = []
    ansList = []
    
    def __init__(self):
        self.questionList=[]
        self.ansList = []
        for i in range(10):
            lOp = random.randint(1, 100)
            sign = random.randint(0,3) 
            rOp = ( random.randint(1,100) if sign < 2 else random.randint(1,10) ) 
            self.questionList.append(str(lOp) + " " + self.op_sign[sign] + " " +str(rOp))
    
    
    
    def runProgram(self):
        ''' Execute the program'''
        for s in self.questionList :
            t = Timer(8, self.timeRanOut)
            t.start()
            k = input(s + "\t:")
            if not self.globalFlag :
                t.cancel()
                self.ansList.append(k)
            else :
                self.ansList.append(k + "Timeout Reached")
                self.globalFlag = False
                
            
    def showAnswer(self):
        ansCompare = []
        score = 0
        for q, a in zip(self.questionList,self.ansList) :
            ansCompare.append((q, eval(q), a))
            score += 1 if str(eval(q)) == a else 0
        
        print( "Your Score : " + str(score))
        with open("scoreRecorder.txt", "a") as myFile :
            myFile.write("\n\n Try at Time " + str(datetime.now())+"\n")
            for q, e, a in ansCompare :
                ansKey = "Question : " + q + " Expected  :" + str(e) + " Actual : "+ a 
                ansKey += ( " Correct \n" if str(e) == a else " Wrong \n" )
                print(ansKey)
                myFile.write(ansKey)
        
            myFile.write("Your Score : " + str(score) )


if __name__ == '__main__': 
    while (True):
        test = quickMathsTest()
        test.runProgram()
        test.showAnswer()
        if str(input("Want to continue [y/n]")) == 'n' :
            break
'''sol = [ (x, eval(x)) for x in questionList]
print(sol)
    
''' 