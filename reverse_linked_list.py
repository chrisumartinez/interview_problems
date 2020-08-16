""" 
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both? """

### do not modify this class
class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
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
  
  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
  def to_array(self):
    array = []
    curr = self.head
    while curr != None:
      array.append(curr.data)
      curr = curr.next
    return array
  
  # implement this method
  def reverse(self):
      # add values to a list:
      nodeList = []
      cur = self.head
      while cur != None:
          nodeList.append(cur.data)
          cur = cur.next
      #Reverse the list:
      nodeList = nodeList[::-1]
      
      #now append it back into the list:
      index = 0
      cur = self.head
      while cur != None:
          cur.data = nodeList[index]
          index += 1
          cur = cur.next

  def printNodes(self):
    cur = self.head
    while cur != None:
        print(cur.data)
        cur = cur.next
        



ll = LinkedList()
ll.extend([1,2,3,4,5,6])
ll.printNodes()
print("")
ll.reverse()
ll.printNodes()