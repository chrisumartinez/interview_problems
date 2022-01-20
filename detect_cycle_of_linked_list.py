""" 
Write a function that takes a Linked List and returns True if the list contains a "cycle" - eg, the list contains no node pointing to None.

For example:




Ensure your code can be called like this:
ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])

## now imagine if, in another file, there has been some malicious function inserted
## that creates a cycle in this linked list
cause_havoc(ll) 


## thankfully, if your code works, you can detect this!
ll.has_cycle() # returns True

"""

#Build a Circular Linked List:

### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than has_cycle()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      
  def extend(self, array):
    for element in array:
      self.append(element)

  def printNodes(self):
      cur = self.head
      while cur != None:
          print(cur.data)
          cur = cur.next
  
  # used in test cases to create cycles in the linked list
  # if you want to test your code without submitting, consider using this function
  def get_reference(self, index):
    curr = self.head
    count = index
    while count > 0:
      curr = curr.next
      count -= 1
    return curr
      
  # implement this method
  # return true if there is a cycle in this linked list
  def has_cycle(self) -> bool:
      # #O(n²) algorithm:
      # #Let cur = top of the LinkedList:
      # top = self.head
      # cur = top.next
      
      # while top != None:
      #     cur = top.next
      #     #while cur != None:
      #     while cur != None:
      #       print("Top: ", top.data, "Cur: ", cur.data)
      #       #iterate through the list, check if the pointer is the same value:
      #       if cur.data == top.data:
      #           return True
      #       else:
      #           cur = cur.next
        
      #       #once we finish iterating, top will become the next node in the list:
      #     top  = top.next
      #   #If we finish the iteration without returning True, then there is no cycle:

      # Hashing Addresses Method:

      list_addresses = {}

      #initiate cur to top:
      cur = self.head

      while cur != None:
        #Check if Cur is in addresses dict:
        if cur.data in list_addresses:
          return True
        else:
          #Add into the addresses and values:
          list_addresses[cur.data] = 1
          cur = cur.next

      print(list_addresses)
        
      return False


ll = LinkedList()
ll.extend([1, 2, 3, 4, 5, 6])
#print(ll.printNodes())
print(ll.has_cycle())

