"""
hashmap is storing a data/key. Dict

-No duplicate key

-BIG O of a add, get, delet is O(1). Extrememly fast and cosntant time operation

Called a dict in python.

1.Fist allocates a set size
2. Then maps the data to a specifc index
3. Uses a hash fucntion to do this to insert and remove

my_dict = {1: "Apple", 2: "Orange"}   -> key = 1,2   value = Apple, Orange



hash function- math function to convert key into an array index
    -Diffrent ways to implement a hash function but a good one is using ascii values.
        -like "march" m = 109 a = 97 ... get each leetters ascii value and then
            -Next take the total ascii value march-> 609 , next mod it by the size of array-> len(arr) = 10
                - 609 % 10 = index of the data

Example:

    

    key = Date , value = price
    stockpriceHashMap =  {
        key: Value

        "Dec 10" : 105.50
        "Sep 15" : 106.10
        "Nov 12" : 150.40



    }
   
   THIS IS NOT HANDING COLLISIONS

"""

class HashTable:  #hand implementation of a dictionary
    def __init__(self):
        self.MAX = 10 #construction initialization on the size of array
        self.arr = [None for i in range(self.MAX)]  #value of each array initialized to null
  
    #hashing fucntion
    def get_hash(self,key):
        hash = 0                  #starting ascii is 0
        for char in key:        #getting each char from the key
            hash += ord(char)      #getting the acii value and adding it 
        return hash % self.MAX          #taking the mod of the total letter ascii by % array size

    #could do __setitem__  to do the normal dictionary operation of []
    def add(self,key,val):
        hash = self.get_hash(key)  #calling get hash to retrieve loaction, storing that in our hash
        self.arr[hash] = val       #inserting the value into our index

    #could do __getitem__ to do normal dict operation of  []
    def get(self,key):
        hash = self.get_hash(key)   #getting the hash value of the key
        return self.arr[hash]       #returning the index of the key

    def deleteItem(self,key):
        hash = self.get_hash(key)  #getting the hash value of the key
        self.arr[hash] = None     #setting the index of the key to null aka finding the loaction of that key and setting it to null




newTable = HashTable()


#add data to the hash table
newTable.add("Dec 10",105.50)
newTable.add("Sep 15",106.10)
newTable.add("Nov 12",150.40)


print(newTable.arr)

print("\n", newTable.get("Dec 10"))    #retrieving the data from the hash table based on key
print("\n", newTable.get_hash("Dec 10")) #retrieving the hash value of the key

newTable.deleteItem("Dec 10") #deleting the data from the hash table based on key
print("\n New table after deletion of Dec 10, 105.50", newTable.arr) #printing the array after deleting the data



"""
Dealing with collisons in Hash Table

If a collision occurs it normally rewrites over the old data

Hash Collsion: A match that occurs when a hashing algorithm produces the same hash value for two distinct pieces of data.


Separate Chaining:
    -When a hash collision occurs in the same index, the data is stored in a linked list on the same index. So it can grow. If this happens the BIG O will be O(n)
    -Chaining is simpler to implement, Never fills up, less sensetive to hash function, used for unkown hash map size paramaters. Can be a wastage of space
Open Afressing:
   - Linear Probing
        - If we run into a collsion, we move to the next slot, the one after, next one.... (Hash(x)+1) % len(hashtable).

   - Quadratic Probing
         -If we run into a collsion, we move to the next slot by powers of 2. So 1^2->2^2
   - Double Hashing
         - 
"""


