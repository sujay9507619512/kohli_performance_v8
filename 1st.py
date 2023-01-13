a=5
print("value: ",a)
print("type:",type)

elements = []
for i in range(10):#this is called identation  single line comment then use #
    elements.append(i)
    print(elements)
"""
this is multi line comment

hgj
"""
first_name = input("enter ur first name: ")
last_name = input("enter ur last name:")
print(first_name+" "+last_name)
print(type(first_name))
print(type(last_name))

val = "adarsh"
print(type(val))
for i in range(len(val)):
    print(val[i], type(val[i]))


elem = [8, 9, "thor", "ironman"]
print(len(elem))
print(elem[-2])
avengerList = ["ironman", "thor"]
ratingList = [10,8]
ratedAvenger =[]
for i in range (len(avengerList)):
    ratedAvenger.append(avengerList[i])
    ratedAvenger.append(ratingList[i])
print(ratedAvenger)
#list is also a data types
#tuples--->tuple is immutable it means we cannot change the value  ;; in list we can change the value after appending also
avengerList[3] = ["aa", "sgdhjs", "dshj"]

#dictionry---->it is also a data type
avengerDict = {
    "ironman": 10,
    "thor":8
}
print(avengerDict)
print(type(avengerDict))
print("rating of ironman: ",avengerDict["ironman"])