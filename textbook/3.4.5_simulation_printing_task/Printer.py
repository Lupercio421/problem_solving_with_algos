class Printer:
    def __init__(self,ppm):
        self.papergate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startnext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.papergate