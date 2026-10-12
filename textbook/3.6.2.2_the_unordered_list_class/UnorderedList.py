class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        # Initially when we construct the list, there are no items
        self.head = None
    

    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()

        return count
    
    def search(self, item):
        current = self.head
        # use a boolean variable to remember wheter we have located the item
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            # when previous is none, it means that you are at the start of your list 
            self.head = current.getNext()
            # the head of list is modified to refer to node after current node
        else:
            # this means the node is somewhere down the linked list
            previous.setNext(current.getNext())

        # One question that often arises is whether the two cases shown here will also handle the situation where the item to be removed is in the last node of the linked list. We leave that for you to consider.

    # how to handle the situation where the item to be removed is in the last node of the linked list?
    
    # append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    def append(self, item):
        current = self.head
        temp = Node(item)
        while current != None:
            # null check is needed
            current = current.getNext()
        
        current.setNext(temp)
    
    # insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = Node(item)

        while current != None and index < pos:
            # null check and index out of bound check
            previous = current
            current = current.getNext()

        if pos == 0:
            temp.setNext(self.head)
            self.head = temp
        else:
            if current == None:
                # null checked
                previous.setNext(temp)
            else: 
                temp.setNext(current)
                previous.setNext(temp)

    # index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
    def index(self, item):
        current = self.head
        found = False # to remind us if we found the varaible
        index = 0

        while current != None and not found:
            if current.getData() != item:
                index += 1
                current = current.getNext()
            else:
                found = True
            
        if found:
            return index
        else:
            return "Not found"

    # pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
    def pop(self):
        current = self.head
        previous = None

        if current == None:
            return "No item in list"
        
        while current.getNext() != None:
            # ensuring we are in fact at the end of the linked list
            previous = current
            current = current.getNext()

        previous.setNext(None)
        return current.getData()
    
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0

        if current == None:
            return "No item in list"
        
        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index += 1

        if current == None:
            return "No item in list"
        else:
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        return current.getData()
    
def main():
    linkedlist = UnorderedList()
    linkedlist.add(1)
    linkedlist.add(11)
    linkedlist.add(111)
    linkedlist.remove(11)
    linkedlist.insert(0,-11)
    print((linkedlist))

main()