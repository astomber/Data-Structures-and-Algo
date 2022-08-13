"""
Tree in python


                 O              Root, Depth 1
            O         O                Depth 2
        O      O    O   O       Leaves, Depth 3
      
      Every node has at most 2 children, children called left and right child
      Top node = Root
      Nodes at the very bottom are leaves
     

      Complete Binary Tree: Every level is full except maybe the last level aka leaves
      Full Binary Tree: Binary tree where every node has either 0 or 2 children

      If there are a total of 8 elements in tree it takes 3 iterations to search, 8->4->2->1

      log2(8) = 3
      Search Complexity = O(log n)

    two ways to traverse binary tree:

       
       
    Pre-order Traversal: root -> left subtree -> right subtree.

    In-order traversal:: left subtree -> root -> right subtree.

    Post-order traversal: left subtree -> right subtree -> root.

"""



"""
Bare bones binary tree

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.right, self.left = None,None #each node exists independently of each other



node0 = TreeNode(3)
node1 = TreeNode(2)
node2 = TreeNode(4)

root = node0
root.left = node1
root.right = node2

    
"""   

"""
defining a tree, very similar to linked list

        data
    Null     Null

    Fun fact, you do self in python to specify your writing in the class you're in

    https://www.youtube.com/watch?v=DlWxqU3LLpY

    Run time is O(log n) because it's essentialy cutting the amount of work each time by half aka log base

"""


class TreeNode:
    def __init__(self, value) :
        self.left = None
        self.right = None
        self.value = value
    
    '''
    manual way of creating a bst
    tree = TreeNode(5)
    tree.left = TreeNode(2)
    tree.right = TreeNode(7)
    '''

    def insert(self,value): 
        if value < self.value:   #if value is less than root, go to left side of tree
            if self.left is None:
                self.left = TreeNode(value) 
            else:
                self.left.insert(value)  #O(n/2)

        else:    #if value is greater than root, go to right side of tree
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)  #O(n/2)
    
    def inOrder(self):     # Traverse left subtree, Visit the root, Traverse the right subtree. 
        if self.left:    #if left exists
            self.left.inOrder()

        print(self.value, end = " ")

        if self.right: #if right exists
            self.right.inOrder() #recursion

    def preOrder(self): #Visit the root, Traverse the left subtree, Traverse the right subtree
        print(self.value, end = " ")   

        if self.left:    #if left exists
            self.left.inOrder()

        if self.right: #if right exists
            self.right.inOrder() #recursion


    def postOrder(self): #Traverse the left subtree, Traverse the right subtree, visit the root
          if self.left:    #if left exists
            self.left.inOrder()

          if self.right: #if right exists
            self.right.inOrder() #recursion

          print(self.value, end = " ")   

   

    def find(self,value):
        
        if value < self.value: #if value is less than current node branch to left side of tree
            if self.left is None:  #if value not in left side of tree, return false
                return False
            else:
                return self.left.find(value) #recursion and search the left sub tree, then return the location

        elif value > self.value:   #if value greater than current node branch to right side of tree
            if self.right is None:  #if value not in right side of tree, return false
                return False
            else:
                return self.right.find(value)  #recursion and search the right sub tree, then return the location

        else:   #if the value is the same as the current node
            return True
    
    
    def delete_Node(root, key):
        if not root: 
            return root
        # Find the node in the left subtree	if key value is less than root value
        if root.val > key: 
            root.left = delete_Node(root.left, key)
        # Find the node in right subtree if key value is greater than root value, 
        elif root.val < key: 
            root.right= delete_Node(root.right, key)
        # Delete the node if root.value == key
        else: 
        # If there is no right children delete the node and new root would be root.left
            if not root.right:
                return root.left
        # If there is no left children delete the node and new root would be root.right	
            if not root.left:
                return root.right
    # If both left and right children exist in the node replace its value with 
    # the minmimum value in the right subtree. Now delete that minimum node
    # in the right subtree
            temp_val = root.right
            mini_val = temp_val.val
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.val
    # Delete the minimum node in right subtree
            root.right = deleteNode(root.right,root.val)
        return root



tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(1)


print("In order traversal: ")
tree.inOrder()

print("\n\n Post order traversal: ")
tree.postOrder()

print("\n\n Pre Order traversal")
tree.preOrder()

print("\n")


print("\n Trying to find the value 7: ", tree.find(7))

print("\n Trying to find the value 4: ", tree.find(4))
