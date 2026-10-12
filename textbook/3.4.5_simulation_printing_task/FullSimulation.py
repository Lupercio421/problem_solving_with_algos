from Printer import Printer
from Task import Task
import random
import queue

def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = queue.Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.put(task)

        if (not labprinter.busy()) and (not printQueue.empty()):
            next_task = printQueue.get()
            waitingtimes.append(next_task.waitTime(currentSecond))
            labprinter.startnext(next_task)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.qsize()))

def newPrintTask():
    num = random.randrange(1,181)
    #num = 180
    if num == 180:
        return True
    else:
        return False

for i in range(2):
    simulation(3600,5)