tp = (10, 'mahi', 'soft')
print(tp.count(10))

print(type(tp))

# tp.append('xyz')    ---> Error

"""Because Tuple is immutable....
        ---> remove()
        ---> append()
        ---> insert()
  these are not possible....

"""

tp2 = (10, 20, 30, 40)
# tp2.remove(10)     ---->Error....because immutable

print(tp2.count(10))

