'''
--> these are set of key value pairs
--> key should be unique and immutable

'''


data = {"manisha": "engineer", "uma": "lawyer", "preeti": "CA"}

print(data["manisha"]) # result-->"enginer

#it will return error if key is not present in the dictionary

data.get('xyz') #result --> None

#it will return None if key is not present in the dict

data.get('xyz', 'Not found')

# it will return the msg Not found if key is not present in the dict


#creating a dictionary using two tuples

tup1 = ('manisha', 'preeti', 'uma')

tup2 = ('python', 'java', 'javascript')

data = dict(zip(tup1, tup2)) #both tup1 and tup2 should be of same size

#adding more values to the dict

data['monika'] = 'c++'

#deleting the value from dict

del data['manisha']





