d={2:2,3:"zthree",4:"aour",1:"one"}

# copy
e=d.copy()
print("copy method",e)

# fromkeys(dict_name,default_value_for_all_keys)
nd=dict.fromkeys(d,"all")
print("fromkeys method",nd)

# get(key)
print("get method :",d.get(2))

# items()
print("items",d.items())

# keys()
print("keys :",d.keys())

#pop(key)
d.pop(2)
print("pop method",d)

# setdefault(key,value)
d.setdefault(2,"Two")
print("setdefault",d)

# update()
d.update({5:"Five"})
print("update",d)

#values
print("values :",d.values())

# sort()
print(sorted(d.items()))
print(sorted(d.items(),key=lambda x:x[1]))

# del 
del d[1]
print("del method ",d)