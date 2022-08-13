#!/usr/bin/env python
# coding: utf-8

# Singly Linked List:
# Documentation: https://docs.google.com/presentation/d/1TCTdhhAAisXc1g7O2uh3OwjkUXeYbt18nDR-ba_6WOs/edit#slide=id.p
# 
# 
# Nodes connected by each other, it uses the List [] in python
#     Contains: Data,Next -> Data,Next -> NULL
# 
# Ex: A->B->C->D->E->NULL         End of linked list is null
# 
# BIG O of Linked List:
#                            Array    LinkedList
#      Insertion/Deletion:   O(N)       O(1)
#      Access Elements       O(1)       O(N)
# 
# Need to traverse through whole list for linked list so O(N)
# 
# 
# Appending to a linked List:
#     
#     A| ->  B| ->  C| -> NULL
#     
#     1.Append D to the linked list
#          A| ->  B| ->  C| ->  D| -> NULL
# 
# 

# In[ ]:


#code for signly linked list, INSERTION
"""
IF YOU GET CONFUSED WITH ANY FUNCTION, CALL THE PRINT HELPER
EX: self.print_helper(curr, "Curr")
"""
import random



class Node:
    def __init__ (self, data):
        self.data = data #constructor
        self.next = None
class LinkedList:
    def __init__ (self):
        self.head = None #starting a fresh linked list so head is initially NULL

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)
    
    def print_list(self):
        curr_node = self.head #temp node for traversal
        while curr_node:
            print(curr_node.data, "->",end="")
            curr_node = curr_node.next #move current node to next node
        print("NULL")
    
    def append(self, data): #adding to the end of our linked list
        new_node = Node(data)
        
        if self.head is None: #if the linked list is empty
            self.head = new_node #new_node is first node aka head node
            return
        
        last_node = self.head
        while last_node.next: #while the nodes aren't pointing to null, aka traverse through linked list
            last_node = last_node.next #move pointers to the right 
        last_node.next = new_node #append the node to the end of the list
        
    def prepend(self,data):
        new_node = Node(data) #inistiating a new node

        new_node.next = self.head #pointing the new node to the head, the pointer of new node is now pointing to head.  EX: prepend(5) to this linked list 1->2->3->4->NULL,   5->1->2->3->4->NULL

        self.head = new_node # new_node = head now
           
    def appendPosition(self,prev_node,data): #inserting a specific position, needs the previous node because it's pointer needs to point to the new node
        if not prev_node: #if the previous node doesn't exisist
            print("Previous node not in the list. Enter a real previous node")
            return

        new_node = Node(data)
       
       
        new_node.next =  prev_node.next  #new node pointer will point to the one after the previous node
        prev_node.next = new_node

        
        """
        5->1->2->3->4->NULL

        1. trying to insert 6 at the 2 spot

        2. SO prev_node is 1

        3.  Next the 2 node points to 6 and then the 1 node points to 6. Lodging it in there
                
        """
    def deletNode(self,key): #given a data field delete the node with this field
          
        cur_node = self.head

        if cur_node and cur_node.data == key: #is current node is not null and the current node data is equal to the data passed in
            self.head = cur_node.next    #moving the head node
            cur_node = None #current node aka one deleted is now NULL

        prev_node = None #previous node initialized to NULL
        while cur_node and cur_node.data != key: #iterate through the list while the head node is not none and the data field is not equal to the one were looking for
                prev_node = cur_node
                cur_node = cur_node.next    #move the head pointer along and keeping track of current node.next and previous node
        if cur_node is None:
            print("data not present in linked list")
            return
        
        prev_node.next = cur_node.next
        cur_node = None

    def delet_node_at_pos(self,pos):   #Ex: delete node with position 1

        cur_node = self.head

        if pos==0:      #if position is at index 0, set the node as the head 
            self.head == cur_node.next
            cur_node = None #resets the current node

        prev = None 
        count = 0 
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None: 
            print("position is greater than the one in the Linked list")
            return
        prev.next = cur_node.next
        cur_node = None

    #ITERATIVE SOLUTION. ery similar to our print linked list function, study that and you got length of linked list function
    def length_of_linkedlist(self):
        curr_node = self.head #temp node for traversal
        counter = 0
        while curr_node:
            counter += 1 #counter to keep track everytime we traverse through a node
            curr_node = curr_node.next #move current node to next node  
        return counter
        
    def length_recursive_linkedlist(self,node): #recusive for length of linked list
          if node is None: #base case for recursive call, if list is empty return 0
            return 0
          return 1 + self.length_recursive_linkedlist(node.next) #recursive call decrement to next node every time and iterate through the list
    

    '''
    COME BACK TO THIS AND REVIEW. MAYBE REVISE AND USE HELPER FUNCTIONS
    '''
    #making use of 3 pointers. 2 pointers start at the beginning of each linked list, next compare which is the smaller node data value, next iterate the pointer with the smaller node
    def merge_two_sorted_linkedlist(self, linked_list):
        p = self.head 
        q = linked_list.head
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 
        return new_head


    def moveToFront(self):
        tmp = self.head
        sec_last = None # To maintain the track of
                        # the second last node
  
    # To check whether we have not received 
    # the empty list or list with a single node
        if not tmp or not tmp.next: 
            return
  
        # Iterate till the end to get
        # the last and second last node 
        while tmp and tmp.next :
            sec_last = tmp
            tmp = tmp.next
  
        # point the next of the second
        # last node to None
        sec_last.next = None
  
        # Make the last node as the first Node
        tmp.next = self.head
        self.head = tmp
    
    
      # Function to swap Nodes x and y in linked list by
    # changing links
    def swapNodes(self, x, y):
 
        # Nothing to do if x and y are same
        if x == y:
            return
 
        # Search for x (keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next
 
        # Search for y (keep track of prevY and currY)
        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
 
        # If either x or y is not present, nothing to do
        if currX == None or currY == None:
            return
        # If x is not head of linked list
        if prevX != None:
            prevX.next = currY
        else:  # make y the new head
            self.head = currY
 
        # If y is not head of linked list
        if prevY != None:
            prevY.next = currX
        else:  # make x the new head
            self.head = currX
 
        # Swap next pointers
        temp = currX.next
        currX.next = currY.next
        currY.next = temp
        
  
    def reverseIterative(self):
    # A -> B -> C -> D
    # A <- B <- C <- D   Really just changing the pointer orientation
    # We need to keep track of our current node and the previous node 
    #Time complexity is O(N), Space = O(1). Just using pointers

       
            prev = None 
            cur = self.head
            while cur:
                nxt = cur.next
                cur.next = prev
                
                self.print_helper(prev, "PREV")
                self.print_helper(cur, "CUR")
                self.print_helper(nxt, "NXT")
                print("\n")

                prev = cur 
                cur = nxt 
            self.head = prev


    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
    
    '''
    Given this linked List. Rotate at the "C"
    A -> B -> C -> D- > E

    1. So C is the pivot, and "D" and "E" will now move to the front
        D- > E -> A -> B -> C

    Going to use a 2 pointer approach for this
    '''
    def rotate(self, k):
            p = self.head 
            q = self.head 
            prev = None
            
            count = 0
            
            while p and count < k:
                prev = p
                p = p.next 
                q = q.next 
                count += 1
            p = prev
            while q:
                prev = q 
                q = q.next 
            q = prev 

            q.next = self.head 
            self.head = p.next 
            p.next = None

    


# In[2]:


Link_One = LinkedList()



print("Linked List, appending to the end of linked list")

Link_One.append("A")
Link_One.append("B")
Link_One.append("C")
Link_One.append("D")
Link_One.print_list()

print("\n prepending Z to the front of linked list")
Link_One.prepend("Z")
Link_One.print_list()

print("\n inserting R at the B node position")
Link_One.appendPosition(Link_One.head.next,"R")
Link_One.print_list()

print("\n Deleting B from the linked list")
Link_One.deletNode("B")
Link_One.print_list()

print("\n\n Length of Linked List with iterative function: ",Link_One.length_of_linkedlist())
print("\n Length of Linked List with recursive function: ",Link_One.length_recursive_linkedlist(Link_One.head)) #passing in the head because it's the starting node


# In[ ]:


'''
#populating our linked list with random numbers
for x in range(11):
    integer_list_one.append(int(random.uniform(1,6))) #random number between 1,6 use random.uniform, also did integer casting
    integer_list_two.append(int(random.uniform(6,11)))
'''


integer_list_one = LinkedList()
integer_list_two = LinkedList()

integer_list_one.append(1)
integer_list_one.append(5)
integer_list_one.append(7)
integer_list_one.append(9)
integer_list_one.append(10)

integer_list_two.append(2)
integer_list_two.append(3)
integer_list_two.append(4)
integer_list_two.append(6)
integer_list_two.append(8)

    
print("\n\n\n Merging these two Sorted Lists, Before: ")
print("\n List one")
integer_list_one.print_list()
print("\n List Two")  
integer_list_two.print_list()

print("\n After:")
integer_list_one.merge_two_sorted_linkedlist(integer_list_two)
integer_list_one.print_list()


# In[4]:



print("\n\n\n Before moving the tail to the head ")
Link_One.print_list()

print("\n After moving the tail to the head ")
Link_One.moveToFront()
Link_One.print_list()

print("\n\n\n Swapping A and R ")
Link_One.swapNodes("A","R")
Link_One.print_list()




# In[5]:


reverse_link = LinkedList()
reverse_link.append("A")
reverse_link.append("B")
reverse_link.append("C")
reverse_link.append("D")
reverse_link.append("E")

print("\n\n\n Original Linked List")
reverse_link.print_list()

'''
print("\nAfter reversing the linked List itertively:")
reverse_link.reverseIterative()
reverse_link.print_list()
'''
print("\nAfter reversing the linked List Recursievly:")
reverse_link.reverse_recursive
reverse_link.print_list()



rotate_link = LinkedList()
rotate_link.append(1)
rotate_link.append(2)
rotate_link.append(3)
rotate_link.append(4)
rotate_link.append(5)

print("\n\n\n Original List, Goign to rotate at the 3 element: ")
rotate_link.print_list()

print("\n After Rotation at the 3 element")
rotate_link.rotate(3)
rotate_link.print_list()

# In[ ]:









