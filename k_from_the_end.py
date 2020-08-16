""" 
Write a function that, when given a Singly Linked List and an integer k, 
will return the kth element from the end of the list. """

### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
### you may insert new methods if you like
class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0
    
  def empty(self):
    return self.head == None
    
  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
      self.length += 1
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node
      self.length += 1
      
  def extend(self, array):
    for element in array:
      self.append(element)
  
  # implement this method
  def kth_from_the_end(self, k):
    kth_position = self.length - k
    counter = 0
    cur = self.head
    while counter < kth_position - 1:
      cur = cur.next
      counter += 1
    return cur.data
      


# ll = LinkedList()
# ll.extend([1,2,3,4,5,6])
# print(ll.kth_from_the_end(4))