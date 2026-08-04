
fruits = ["Apple", "Banana", "Mango", "Orange"]

print( fruits)


print( fruits[0])
print( fruits[-1])


fruits[1] = "Grapes"
fruits.append("Pineapple")
fruits.remove("Orange")

print( fruits)

print( fruits[:2])
print( fruits[1:3])
print( fruits[::-1])


numbers = [x*x for x in range(6)]
print( numbers)

even = [x for x in range(11) if x % 2 == 0]
print( even)
