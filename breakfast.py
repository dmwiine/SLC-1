'''print("Get the ingredients")
print("mix the ingredients")
print("pour onto hot pan")
print("using a spatula, scramble the eggs")
print("Serve yummy eggs")
breakfast = "----Eggs are served-----"
print(breakfast)

print("Get the ingredients")
print("mix the ingredients")
print("pour onto hot pan")
print("using a spatula, scramble the eggs")
print("Serve yummy eggs")
breakfast = "----Pancake is served-----"
print(breakfast)'''

def makeBreakfast(name,*ingredients):
	print("Get the ingredients")
	print("Mix the ingredients")
	print("Pour onto hot pan")
	print("Flip to the other side")
	breakfast = ""
	if len(ingredients) != 0:
		breakfast = "----Yummy {} with {}----".format(name, ", ".join(ingredients))
	else:
		breakfast = "----Yummy {}----". format(name)
	return breakfast

print (makeBreakfast("Eggs", "spinach","butter"))
print (makeBreakfast("Pancake", "Syrup"))
print (makeBreakfast("Eggs"))
print (makeBreakfast("Pancake"))



