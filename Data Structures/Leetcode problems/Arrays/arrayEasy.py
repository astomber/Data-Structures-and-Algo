"""




Example:
      

Edge Caes:
   


Methadology:
    -This is an Array question because of the wording
   


Lessons Learned: 
    



RUN TIME OF PROGRAM= 
Space Complexity

"""

"""
LeetCode 217: Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
        Input: nums = [1,2,3,1]
        Output: true

        Input: nums = [1,2,3,4]
        Output: false


Edge Caes:
    Could it contain negatives? - NO
    Is all integer values?  - NO


Methadology:
    -This is an Array question because of the wording
    -In python a good data structure to simplify this problem is a SET, it's a unique and unordered collection of elements

    1. Could do 2 pointer approach but it would lead to O(n^2). Brute Force approach. Much better for memmory because no extra needed like set.
    2.Could Sort the array and then the 2 duplicates would be next to each other. But run time is O(nlogn)
    3. Could check if item in set, if not add it. This would lead to O(n). MUCH BETTER



Lessons Learned: 
    -Iterate through the array and check if it's in set or not.
    -Use a set for a problem with unique elements
    -Set operation to append is .add(), TO remove it's .REMOVE()



RUN TIME OF PROGRAM= O(N), just checking one item 
Space Complexity = O(N), Becaue we used an extra memory the hash set
"""


from collections import Counter, defaultdict
import heapq 


def isDuplicate(nums):
    evalarrSet = set()

    for x in range(len(nums)):
        if nums[x] in evalarrSet:
          return True
        else:
          evalarrSet.add(nums[x])
    return False




isDuplicateArr=[1,2,3,4,5]  # No duplicates, False
isDuplicateArrSec = [1,1,2,3,4,5]  # Yes duplicates, True

print("\n Is Duplicate Leet code Problem")
print("First List is: ", isDuplicateArr, ", ", isDuplicate(isDuplicateArr))
print("Second List is: ", isDuplicateArrSec, ", ", isDuplicate(isDuplicateArrSec))





"""
https://leetcode.com/problems/valid-anagram/

LeetCode 242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

    Example:
    Input: s = "anagram", t = "nagaram"
    Output: true
        

    Edge Case:
        So just a-z? Yes

        1.since anagram has to be rearranged: an edge case could be checking it's length
        2. What if it's upper case or lower? Needs to be lower case

   


Methadology:
-This is an Array question because of the wording
    -1.We could first check the length as out first edge case and make this lowercase
     2.Two pointer approach but it would be O(n^2)
     3.Could use a dictiorany and check the key value, becasuse it keeps the amount of times a diffrent letter occurs. Much better but extra space.



Lessons Learned: 
    -Keep it simple use sorted or counter. 
  
Another Implementation, very smart way but idk about using them in a coding interview.

     from collections import Counter
       
        return Counter(s) == Counter(t)

        #Run time =  O(string1 + string2), Space complexity = O(string1 + string2)
       


RUN TIME OF PROGRAM= O(n log n)
Space Complexity = O(n)

This uses time sort. 
"""


def isvalidAnagram(word1,word2):
    
    return sorted(word1) == sorted(word2)
           

s = "anagram" 
t = "nagaram"

print("\nLeetCode 242: Valid Anagram ")
print("Is", s, " and ", t, " valid anagrams ", isvalidAnagram(s,t))



"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Should be downing this in your sleep.




Example:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
      

    Edge Caes:
    -Can it contain negative numbers? No
    -if the length of array is 0, it has to be false

   


Methadology:
    -This is an Array question and basic math because of the wording and the operations.
    -1. Could do 2 for loops like a brute force but run time would be O(n^2)
    2.Could check with a hashmap, it would be O(n)
   


Lessons Learned: 
    understand adding to dictonary
    break down the problem and use enumerate.
    
    Other Approach with O(n^2):

    def twoSumNaive(num_arr, pair_sum):
    # search first element in the array
    for i in range(len(num_arr) - 1):
        # search other element in the array
        for j in range(i + 1, len(num_arr)):
        # if these two elemets sum to pair_sum, print the pair
        if num_arr[i] + num_arr[j] == pair_sum:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",num_arr[j],")")


RUN TIME OF PROGRAM= O(1)
Space Complexity: O(N)

"""


def TwoSum(numArr, target):

   if len(nums) <= 0:
    return False

   dict = {}  #dict for look up of our targetNumber, keeps key and index 

   for index, value in enumerate(numArr):  #enumerate to get index, value
     
    targetNumber = target - value

    if targetNumber in dict:
        return[index, dict[targetNumber]]    #getting the index of our array (value) and index of our target number in dictionary
    else:
        dict[value] = index   #appending to our dictionary, like [1,2] -> {0 = 1}, {0 = 2}  



nums = [2,7,11,15]

print("\nLeetCode 1: Two Sum for list ", nums, " Target Value is 9")
print(TwoSum(nums,9))

print("\n")



"""
49. Group Anagrams, Medium

Given an array of strings find the anagrams and group them together in a list.



Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
      

Edge Caes:
    So only strings? - Yes
    Is it upper case or lower case? lower, so edge case to make them .lower()
    Does length matter? No
    What if it's an empty array? Return an empty list
   


Methadology:
    -This is an Array question because of the wording and working with an "array of strings"
    -Could do a 2 pointer approach but run time would be O(n^2)
    -Could use a dictionary and append them, would be O(N) but uses extra memory so O(N) - better. Dictonary easily search and get key - value pairs.
        -breaking it down even more we can create a helper function that maps a-z
   


Lessons Learned: 
    Can't hash lists so if you're hashing convert it into a tuple. Because tuple are immutable.
    For anagram or getting specific char values use ordinance and ascii mapping with a dict it's helpful
    



RUN TIME OF PROGRAM= O ( m * n) , m amount of strings in arr, n is 26 # of letters
Space Complexity = O(1)

"""


def groupAnagram(arr):

   

    result = defaultdict(list)     #mapping the charchter count of each sting to list of anagram. Removes edge case for no anagram matches

    for string in arr:    #looping through every charchter in our array
        count = [0] * 26 #mapping of a ... z,

        for char in string:
            
            count[ord(char) - ord('a')] += 1 #ascii value of charchter - a, so we can map like A=0, B=1, C=2, D=3 . We iterate to go from 0-26 instead of 0-25
        
        result[tuple(count)].append(string)   #appending count of char 0-26, and each char. Make sure a tuple so we can pass in keys-value pairs

    return result.values()




groupAnag = ["eat","tea","tan","ate","nat","bat"]
print("49. Group Anagrams, Original array: ", groupAnag)
print("All the anagrams grouped: ", groupAnagram(groupAnag))
print("\n")


"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

So with a given array find the numbers that occur the most. Find 2 sets of most frequent numbers. Return their values and amount of

Example:
   Input: nums = [1,1,1,2,2,3], k = 2
   Output: [1,2]   

Edge Caes:
    -can it be negatives? No
    -What if it's one value? Return that one value with a k=1

   


Methadology:
    -Array/max heap. Max heap would be great because we can pop the biggest but its'k O(k log n). very confusing
    -Could use bucket sort, 2 rows - one for index and occurance. kind of trickier
    -Could use a counter, than
   


Lessons Learned: 
    -Use a counter, from collections import Counter
        Counts the amount of occurances in a array
    -heapq data structure learn it more, use nlargest.
    



RUN TIME OF PROGRAM= 
Space Complexity: O(N log k) time

"""

def topkFreq(arr,k):
  # O(1) time 
        if k == len(arr):
            return arr
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(arr)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time

        return heapq.nlargest(k, count.keys(), key=count.get)   #heapq is a heap, nlargest return largest. 2, = 2 largest occurances, 
   
  

nums = [1,1,1,2,2,3]

print("347. Top K Frequent Elements: ")
print("Most frequent of arr: ", topkFreq(nums,2))

"""
        return heapq.nlargest(k,count.keys(), key = count.get)
        Here, k is the number that helps us find out elements which are repeated in a dictionary k times or more than k times.

        count.keys() : This gives you the keys or the elements present in the heap which is created using the collections.counter

            key = count.get() : This is used to print the Keys of the heap. If we skip this; it will print the Values of the dictionary i.e. the number of times the element is occurring in the dictionary.
"""




"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

So all the elements that come after a value must all be multiplied and returned.



Example:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
      

Edge Caes:
    Can it be negative numbers? Yes
    What if the list is empty? return an empty list
   


Methadology:
    -This is an Array question because of the wording
   


Lessons Learned: 
    



RUN TIME OF PROGRAM= 
Space Complexity

"""
























"""
271. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode



Example:

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
      

Edge Caes:
    Can it take special chars? Yes
    What if the list is empty? then return empty/false
    
    
   


Methadology:
    -This is string manipulation
    -We need a delimiter to decode after our encoded.
        like encode "Hi alex" -> "H#i al#ex" 
   


Lessons Learned: 
    



RUN TIME OF PROGRAM= 
Space Complexity

"""


def encode(strs):
    endodedRes = ""

    for s in strs:
        endodedRes += str(len(s)) + "$" + s  #so were doing this sam -> encode of sam = 1$ S , 1$ A 
    return endodedRes

def decode(strs):
    decodedRes = []          #decoded as an list so we can easily parse through
    index = 0    #index starting at 0

    while index < len(strs):  #don't go out of bounds
       
        pointer = index  #pointer to keep track of delimiter

        while strs[pointer] != "$":
            pointer += 1                 #increment after hitting a $ to get the chars out
        length = int(str[index:pointer])
        decodedRes.append(str[pointer + 1 : pointer + 1 + length])
        index = pointer + 1 + length

  


print(encode("Sam"))
print(decode("1$S1$a1$m"))