"""
2D Array

It's a collection of items like an array but has rows and columns. As a lists of lists

Ex:             Row
         column [1,3,9,4]  4 items
                [5,0,8,3]  4 items

         Normal List:     1d_grid = [
                            1,2,3,4
                        ]
         Double List:     2d_grid = [
                            [1,2,3],
                            [4,5,6],
                            [7,8,9],
                        ]
        
        The normal list is just a normal 1d array
        The double list is a 2d array with 3 rows and 2 columns

"""


one_Dgrid = [
     1,2,3,4
 ]


two_Dgrid = [

  [1,2],
  [4,5],
  [7,8], 
  [10,11],

   ]

print("\n", "1D Array")
print(one_Dgrid)


print("\n", "2D Array")
print(two_Dgrid)


print("\n", "Prinint the [row][column] of [0][0] ")
print("\n", two_Dgrid[0][0])


print("\n Accesing 2D array with a double for loop: ")

for row in two_Dgrid:
    print(row)

print("\n Accesing each element in the 2d Array")

for row in two_Dgrid:
    for column in row:
        print(column)

print("\n testing len(matrix[0]), getting the column")
print(len(two_Dgrid[0]))
print("\n testing len(matrix). Getting the row size")
print(len(two_Dgrid)-1)
"""
Leet code 74: Search a 2d matrix

Write an efficent algorithm that searches for a value in an m x n matrix. 
    - Integers in each row are sorted from left to right
    - The fins integer of each row is greater the the last integer of the previous integer

      1  3  5  7
     10 11 16 20
     23 30 34 60

Solutions:
    -Brute force solution
        -Could do O(m*n) aka n^2
    -Binary search much better
        -It would be  O(log(n)), could do a binary search of row by row because it's already sorted
    -Even better we could do a binary search to find which row to search since column is sorted.
        - So if the target is 3, we search the column and cut the ones bigger or less than.
        -It would be log m + log n much better
        -Have a left and right pointer at start and end of each row.
"""


def searchMatrix(matrix,target):
    rows = len(matrix)
    column = len(matrix[0])

    topRow = 0
    botRow = rows - 1

    while topRow <= botRow:
        row = (topRow+botRow) / 2  #getting the mid point of row

        if target > matrix[row][-1]:  #is the target greater than the largest value in this row
            topRow = row + 1  #shift down to get larger values
        elif target < matrix[row][-1]:
             botRow = row - 1  #shift up to get smaller values
        else:
            break
    if not (topRow <= botRow): #if we break out of our while and item not found
        print("Target not found")
        return False
    l, r = 0, column-1
    while l<= r:
        m = (l+r) // 2
        if target > matrix[rows][m]:  #if the target in the row is greater than increase our left pointer
            l = m+1
        elif target < matrix[rows][m]: #if target is smaller in the row than decrease our right pointer
            r = m -1
        else:
            return True
    return False