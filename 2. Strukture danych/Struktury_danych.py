tuple = (10, -3, 4, 9, 12, -6, 0)

def large(arr): 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_

def minimum(arr): 
    max_ = arr[0]
    for ele in arr:
        if ele < max_:
           max_ = ele
    return max_

print(large(tuple))
print(minimum(tuple))