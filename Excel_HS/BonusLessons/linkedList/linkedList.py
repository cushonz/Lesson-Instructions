class Node:

    value = None
    next = None


    # Creates a new node
    def __init__(self,value):
        self.value = value
        self.next = None

    # Helper function to help traverse
    def hasNext(self):
        if (self.next != None):
            return True
        else:
            return False

    # Append a node to the end of the list
    def addNode(self,val):
        currentNode = self
        while (currentNode.hasNext()):
            currentNode = currentNode.next
        currentNode.next = Node(val)

    # Loop through the linked list and print each value
    def printList(self):
        currentNode = self
        print("Value of linked list:")
        while (currentNode.hasNext()):
            print(currentNode.value, end = "")
            currentNode = currentNode.next

        print(currentNode.value) # print final


# 345 + 321

number1 = Node(2)
number1.addNode(6)
number1.addNode(9)
number1.addNode(7)
number1.addNode(3)


number2 = Node(5)
number2.addNode(3)
number2.addNode(4)
number2.addNode(2)
number2.addNode(8)


currentNode1 = number1
currentNode2 = number2
#Empty resultNode
ResultNode = None
mathNode = None
carry = 0
control = 1
while (currentNode1.hasNext() or control == 0):
    

    # Add the two numbers
    digit = (currentNode1.value) + (currentNode2.value) + carry
    carry = 0
    # If number adds to 10 or higher carry the 1
    if digit >= 10 :
        digit -= 10
        carry = 1

    # If result node is not empty
    if (ResultNode != None):
        ResultNode.addNode(digit+carry)
    else:
        ResultNode = Node(digit+carry)
        


    #Shift both linked lists
    currentNode1 = currentNode1.next
    currentNode2 = currentNode2.next
    
     # Add the two numbers
digit = (currentNode1.value) + (currentNode2.value) + carry
    # If number adds to 10 or higher carry the 1
if digit >= 10 :
    digit -= 10
    carry = 1

# Add final node
ResultNode.addNode(digit+carry)

ResultNode.printList()
#numbTotal += (currentNode1.value) + (currentNode2.value)*placeVal


#print(numbTotal)






