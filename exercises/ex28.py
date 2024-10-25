the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this kind of for-loop goes through a list

for number in the_count:
  print("This is count " + str(number))

#same as above
for fruit in fruits:
  print("A fruit of type: " + fruit)

#also we can go through mixed lists too
for i in change:
  print("I got " + str(i))

#We can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
  print("Adding", i, "to the list.")
  #append is a function that lists understand
  elements.append(i)

#now we can print them too
for i in elements:
  print("Elements was:", i)