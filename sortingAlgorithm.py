#zev stravitz
#11/20/14
#Sorting


import random
import time
N=1000 #you can change this number to make the list bigger or smaller

#The goal of this function is to split the big list and create list, "right" and "left"
def mySort(data):
    if len(data) <= 1:
        return data
    
    left = []
    right = []
    integer_middle = (len(data))/2
    for x in range(0,integer_middle):
        left.append(data[x])
    for x in range(integer_middle,(len(data))):
        right.append(data[x])
        
    left = mySort(left)
    right = mySort(right)

    return merge(left,right)

#The goal of this function is to combine the left and right list
def merge(left,right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.remove(left[0])
            else:
                result.append(right[0])
                right.remove(right[0])
        elif len(left) > 0:
            result.append(left[0])
            left.remove(left[0])
        elif len(right) > 0:
            result.append(right[0])
            right.remove(right[0])
    return result

data = []
for i in range(0,N):
    data.append(random.randint(1,N-1))

#time the sorting routine
t1 = time.clock()
copy=mySort(data[:])
t2 = time.clock()

#make sure the list was sorted correctly
data.sort()
try:
    assert(data==copy) 
    #print how long the function took to do the sort
    print 'Your sort took', t2-t1, 'seconds.'
except:
    print 'Your sort did not run correctly'
