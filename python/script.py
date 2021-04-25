# for temp in range(6):

#     print("Hello, World " + str(temp + 1))


# count = 0

# while count <= 10000: print(count); count += 1


# countdown = 10

# while countdown >= 0:

#     print(countdown)

#     countdown -= 1

# print("we have liftoff!")


# ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# length = len(ingredients)

# index = 0


# while index < length:

#     print(ingredients[index])

#     index += 1


# python_topics = ["variables", "control flow", "loops", "modules", "classes"]


# #Your code below: 

# length = len(python_topics)

# index = 0

# while length > index:

#   print("I am learning about " + python_topics[index])

#   index += 1

# # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie
 
# # print("Checking the sale list!
 
# # for item in items_on_sal
  
# #   if item == "knit dress
# #     bre
# # print(ite


# print("End of search!")


# dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]

# dog_breed_I_want = "dalmatian"


# for dog_breed in dog_breeds_available_for_adoption:

#   print(dog_breed)

#   if dog_breed == dog_breed_I_want:

#     print("They have the dog I want!")

#     break



# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

# scoops_sold = 0


# for location in sales_data:
#   print(location)

#   for scoops in location:
#     #print(scoops)

#     scoops_sold += scoops
# print(scoops_sold)


# grades = [90, 88, 62, 76, 74, 89, 48, 57]

# scaled_grades = [grade + 10 for grade in grades]

# print(scaled_grades)


# heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

# can_ride_coaster = [height for height in heights if height > 161]

# print(can_ride_coaster)





def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n); n += 1
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 