'''docs:-
   ---> lists are mutable
   ---> collection of same or different elements
''' 


nums = [10, 20, 30, 40, 50]

print(nums[0])

print(nums[2:]) #result will be 2 element till end 

print(nums[-1]) #print last elemnt 

names = ['manisha', 'uma', 'preeti']

values = [1, 10.5, "manisha"] # we can have list having different types

nums.append(78) # result --> [10, 20, 30, 40, 50, 78]
# --> append will insert in the end of the list

nums.insert(2, 100) # result --> [10, 20, 100, 30, 40, 50, 78]
#--> insert will insert at the given index value

nums.remove(10) # result --> [20, 100, 30, 40, 50, 78]
# -->remove will remove the first occurance of that elemnt from the left
# --> remove will throw an error if that element is not present in the list

nums.pop(1) #result -->[20, 30, 40, 50, 78]
# --> pop removes elemnt at that particular index and gives error if greater index is given
# --> if no index value is given then it will remove the last element

del nums[4]

del nums[1:]
#--> in del list indices must be integers or slices

nums.extend([1,2,3])
# --> it will extend the nums list with metioned values

print(min(nums))
# --> minimum value in the list

print(max(nums))
# --> maximum value in the list

print(sum(nums))
# --> do the sum of all the values of the list


print(nums.sort())
# --> will sort the list (by default in ascending order)