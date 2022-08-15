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
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

So a string that can be read front and backward is a palindrome.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
      

Edge Caes:
    -If a string is empty, it's a palindome because it's the same fron-back, back-front
    -Can special charchters be used? No. So string all special chars but keep numbers
    -Make sure string is lower case
   


Methadology:
    - with pythons built in functions for string manupulation it can be done with if/else statements. Stripping all it's special chars, spaces
    -We could do a two pointer approach while 
        -So it seems like we could do a pointer to the fron and one in the back. Then we could compare the values. 
          -A point that comes up is it's only a palindrome we could check if theyre odd but if even compare last two.

   


Lessons Learned: 

    Easier "cheating Method"
        use ''.join(filter(str.isalnum, "given string" )) to remove special charchters
        remember[::-1] to print a string backwords

    Two Pointer approach ("advisiable"):
        -use the classic l,r = 0, len(str) -1 and while loops
        -make your own function and for special chars it's the ord thats between A-Z, a-z, 0-9. aka it's the ord between all of those


        



RUN TIME OF PROGRAM= O(logn)
Space Complexity: O(n), using the str[::-1] approach and creating extra memory

"""

#kind of the cheating solution because using built ins
def isPalindrome(word):
    if len(word) == 0:
        print("It's a palindrome")
        return True
    
    

    word =  ''.join(filter(str.isalnum, word)).lower()  #.join combines into one string, filter(str.isalnum,word) removes special chars, ofc .lower() is lower case

    if word == " ":
        print("Is palindrome")
        return True
    elif word[::-1] == word:     #extra memore creating a new reverse string
        print("Is a palindrome")
        return True
    else:
        print("not a palindrome")
        return False





# Own alpha-numeric function. If it contains alpha numbers. just a handwritten approach to str.isalnum. True if it's alpha numbers, false if it isn't
def alphanum(c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


#Big O(n), Memory complexity O(1)
#Two pointer approach, highly advisable to do it this way. NO uses of the built in methods
def isPalin(word):
    l,r = 0, len(word)-1

   

    while(l < r):  #while left and right don't cross each other

        while l < r and not alphanum(word[l]):    #checking left pointer not alpha numberic
            l += 1
        while r > l and not alphanum(word[r]):    #checking left pointer not alpha numberic
            r -= 1
        if(word[l].lower() != word[r].lower()):    #while both strings match and 
            print("Not a palindrome")
            return False
        l += 1   #decrementing to next position
        r -= 1
    print("Is a palindrome")
    return True




palindromeStr =  "race a car"

print("\n Python is this a palindrome with if/else, built in method: ", palindromeStr)
isPalindrome(palindromeStr)
print("\n")

print("\n Python is this a palindrome with left/right pointer and ord: ", palindromeStr)
isPalin(palindromeStr)
print("\n")




"""
167. Two Sum II - Input Array Is Sorted

    Like Two sum bunt alrady sorted. Also it's using 1-indexed arrays
Example:
      Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Edge Caes:
    So we need to return our value by 1 because it's using 1 indexed arrays
    It can contain negatives
    If it's empty return False


Methadology:
    -This is a two pointer approach because we have to add two diffrent numbers. Thinking of doing a left and right pointer.
        -Also, Since it's sorted descending order. We can check if the sum is greater, make the right pointer smaller. If sum is too small, make the left pointer smaller
    
   


Lessons Learned: 
    Great job on this one. But remember to look back at your edge cases like knowing this goes off the 1 index.

    



RUN TIME OF PROGRAM= It would be O(N), were just using one loop and moving them left/right
Space Complexity O(1), no extra space needed

"""   


def twoSum(numArr, target):

   

    #set up out 2 pointers
    l,r = 0, len(numArr) - 1

    #set up while loop
    while(l<r):
        #set up equation, so target = numArr[l] + numArr[r]
       # target = numArr[l] + numArr[r]

        if(numArr[l] + numArr[r] < target ): #if sum is less than target, increment left pointer
            l += 1
        elif(numArr[l] + numArr[r] > target ):  #since already sorted if it's a bigger sum than decrement right pointer
            r -= 1
        else:
            print(l+1,r+1)
            return [numArr[l],numArr[r]]

    print("No sum Found")




numbers = [2,7,11,15] 
target = 9
print("Two sum 2 of array with a target ", target, " " , numbers)
twoSum(numbers,target)


"""
15. 3Sum



Edge Caes:
    No duplicates
    Return three numbers


Methadology:
    -This is a two pointer approach because we have to add two diffrent numbers. Thinking of doing a left and right pointer.
        -gotta make sure to do continue if we get duplicates
        -Also, Since it's sorted descending order. We can check if the sum is greater, make the right pointer smaller. If sum is too small, make the left pointer smaller
    
   


Lessons Learned: 
    Very similar to last two sum questions. Just make sure to watch out for the edge cases

    



RUN TIME OF PROGRAM= It would be O(N^2), 2 loops
Space Complexity O(1), no extra space needed

"""   


def threeSum(nums):
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


