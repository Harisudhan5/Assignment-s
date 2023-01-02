# tupple methods

tp=(8,5,6,78,45,25,3,2,9,54,36,25,25,36,58)
print(tp)

# count()
i=tp.count(25)
print("count method",i)

# index(value) method
print(tp[5])
print("index method ",tp.index(2))


# set methods

st={5,8,6,1,4,7,6,8}
l=[5,8,5,6,8,2,3,8,3,1]
ds=set(l)
print(" set 1 : ",ds)
print("set 2 :",st)

# add(value)

st.add(54)
st.add(1)
print(st)

# discard(value)

st.discard(54)
print("discard method",st)

