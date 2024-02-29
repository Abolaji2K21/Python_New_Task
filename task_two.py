tup1 = ("a", "b", "c", "d")
print ("Tuple before update", tup1, "id(): ", id(tup1))

list1 = list(tup1)
list1[2]='F'
list1.append('Z')
list1.sort()
print ("updated list", list1)

tup1 = tuple(list1)
print ("Tuple after update", tup1, "id(): ", id(tup1))

tup1 = (10,20,30, 40, 50, 60)
x, *y, z = tup1
print ("x: ",x, "y: ", y, "z: ", z)

tup1 = (25, 12, 10, -21, 10, 100)
for num in tup1:
   print (num, end = ' ')

   tup1 = (25, 12, 10, -21, 10, 100)
   indices = range(len(tup1))
   for i in indices:
       print("tup1[{}]: ".format(i), tup1[i])