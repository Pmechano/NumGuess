from random import randint

class GuessProgram:
    def __init__(self):
        self.ans = randint(1, 100)
    
    def rules(self):
        return"""
        我会生成一个1~100的整数，你要猜中他。
        每次输入数字，我会告诉你和答案相比，过大还是过小，直到你猜中为止！
        点击确认以开始！🐦‍⬛
        """
    
    def tryGuess(self,num):
        if num==self.ans:
            return [0,"你胜了"]
        elif num>self.ans:
            return [1,"过大了"]
        elif num<self.ans:
            return [2,"过小了"]