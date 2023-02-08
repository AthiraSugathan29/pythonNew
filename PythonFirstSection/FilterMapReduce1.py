l = [11,34,23,56,78,50,33]
lst = list(filter(lambda x:x%2 == 0,l)) # Return only the elements that satisfy the condition.
print("Filter : ",lst)

l = [11,34,23,56,78,50,33]
lst = list(map(lambda x:x%2 == 0,l)) # Return all elements with condition True or False
print("Map 1 : ",lst)

#Map example - 2
l = [11,34,23,56,78,50,33]
lst = list(map(lambda x:x*2,l))
print("Map 2 : ",lst)

# Reduce
from functools import reduce
l = [1,2,3,4]
lst = reduce(lambda x,y:x*y,l)
print("Reduce : ",lst)