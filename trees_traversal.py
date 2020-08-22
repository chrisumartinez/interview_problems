""" 
You're given an implementation for a Node and a Tree.
Implement the level-order, pre-order, in-order and post-order
 traversals for these trees. Return the data of each node in a list 
 representing the requested order.


Given a tree that looks like this:
 
tree = Tree()
tree.root = Node(9)

tree.root.left = Node(5)
tree.root.right = Node(11)

tree.root.left.left = Node(3)
tree.root.left.right = Node(7)



Level Order
 
[9,5,11,3,7]

In-Order
 
[3,5,7,9,11]

Pre-Order
 
[9,5,3,7,11]

Post-Order
 
[3,7,5,11,9] """

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

class Tree:
    def __init__(self):
        self.root = None


    def level_order_traversal(self):
        # return the tree as a list in a level-order sequence
        #start at root
        traversal_list = []
        if not self.root:
            return
        
        queue = [self.root]
        while  queue:
            curr = queue.pop(0)
            traversal_list.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        return traversal_list



    def pre_order_traversal(self):
        # return the tree as a list in a pre-order sequence (dfs)
        
        #print current
        #visit left
        #visit right

        if not self.root:
            return
        
        traversal_list = []
        stack = [self.root]
        while stack:
            curr = stack.pop()
            traversal_list.append(curr.data)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        

        return traversal_list

    def in_order_traversal(self):
        # return the tree as a list in-order (dfs)
        #In Order:
        # visit left
        # print node
        # visit right
        traversal_list = []

        # Lets try this out recursively:
        def in_order(node):
            if node:
                in_order(node.left)
                traversal_list.append(node.data)
                in_order(node.right)


        if not self.root:
            return
        in_order(self.root)
       

    
        return traversal_list
    def post_order_traversal(self):
        # return the tree as a list in a post-order sequence (dfs)

        traversal_list = []

        #lets do this recursively:
        def post_order(node):
            if node:
                post_order(node.left)
                post_order(node.right)
                traversal_list.append(node.data)
        
        if not self.root:
            return
        post_order(self.root)

        return traversal_list


# tree = Tree()
# tree.root = Node(9)

# tree.root.left = Node(5)
# tree.root.right = Node(11)

# tree.root.left.left = Node(3)
# tree.root.left.right = Node(7)

# print(tree.level_order_traversal())
# print(tree.pre_order_traversal())
# print(tree.in_order_traversal())
# print(tree.post_order_traversal())