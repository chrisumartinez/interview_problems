""" 
Add a method to a linked list to insert a node at the given position.
 Pass in two arguments, node value and insert position.

For example:

ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])

ll.insert(4,2)

The list would then have nodes ordered like this: 1,2,4,3,4,5,6

For the above example, it would be valid to insert an item at index 6. Inserting an 
item at an index equal to the list's length is the same as appending a new item to the list.
 Additionally, it is valid to insert an item at index 0, which puts that item at the head
  of the list. Make sure to account for these edge cases in your code. """


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self) -> bool:
        return self.head == None

    def extend(self, array):
        for element in array:
            self.append(element)

    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node

 # used in test cases to verify solutions
  # if you want to test your code without submitting, consider using this function
    def get(self, index):
        curr = self.head
        count = index
        while count > 0:
            curr = curr.next
            count -= 1
        return curr.data
        
    def printNodes(self):
        cur = self.head
        while (cur != None):
            print(cur.data)
            cur = cur.next
    def insert(self, data, position):

        #We can insert at top, middle, and end of the list:

        # Insert into an empty List:
        if self.empty():
            new_node = LinkedNode(data)
            self.head = new_node
            self.tail = new_node
            return
        
        #inserting at the head:
        if position == 0:
            new_node = LinkedNode(data)
            new_node.next = self.head
            self.head = new_node
            return

        
        #insert anywhere within an already insantiated list:
        counter = 1
        new_node = LinkedNode(data)
        #set a pointer to the top:
        cur = self.head
        while counter <= position:

            # check if we are approaching null:
            if cur.next == None:
                #append our new Node to the end of the list:
                cur.next = new_node
                #and return out once were done:
                return
            else:
                if counter == position:
                    print("Cur: ", cur.data)
                    #insert here:
                    new_node.next = cur.next
                    cur.next = new_node
                    return
                else:
                    #traverse through our LinkedList, increment counter to 1
                    cur = cur.next
                    counter += 1
        
# ll = LinkedList()
# ll.extend([1, 2, 3, 4, 5, 6])
# ll.insert(4,2)
# ll.printNodes()
            


    
