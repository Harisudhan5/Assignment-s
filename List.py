a=[95,64,7,46,85,84,85,90,62,90]

# append 
a.append(25)
print("append method",a)

# copy
b=a.copy()
print("copy method",b)

# count
cnt=a.count(90)
print("count method",cnt)

# extend 
b.extend(a)
print(b)

# index(value)
print("index method",a.index(90))

# insert(index.,value)
a.insert(0,100)
print("insert method ",a)

# pop(index)
a.pop(0)
print("pop method ",a)

# remove(value)
a.remove(90)
print("remove method ",a)

# reverse( )
a.reverse()
print("reverse method",a)

# sort()
a.sort()
print("sort method",a)

# sum()
print("sum",sum(a))

# sort(reverse=True)
a.sort(reverse=True)
print(a)

# zip() function
t=[1,2,3]
v=['a','b','c']
cb=list(zip(t,v))
print("zip function",cb)

# most common item in list
games = ['heads', 'heads', 'tails', 'heads', 'tails']
items = set(games)
print(max(items, key = games.count))

# clear
a.clear()
print("clear method ",a)