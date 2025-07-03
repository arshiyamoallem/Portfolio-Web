"""
1
23
456
78910
"""
"""
rows = 4
num = 1

for i in range(1,rows+1):
    print(""*(rows-i) * 2, end = " ")
    for j in range(0,i):
        print(num, end = " ")
        num +=1
    print()
    """

"""
    1
   23
  456
 78910
"""

rows_ = 6
num_ = 1

for i in range(1,rows_+1):
    print(" "*(rows_-i) * 2, end = " ")
    for j in range(0,i):
        print(num_, end = " ")
        num_ +=1
    print()
    
"""
    1
   2 3
  4 5 6
 7 8 9 10

nums, row = 1, 4

for i in range(1,row+1):
    print(" "*(row-i) * 1, end = " ")
    for j in range(0,i):
        print(nums, end = " ")
        nums +=1
    print()
"""