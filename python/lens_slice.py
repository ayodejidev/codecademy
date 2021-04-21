# Your code below:

'''You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.'''

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)
num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

#print(pizza_and_prices)
pizza_and_prices.sort()

#print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]

#Removing the last item on Pizza and Price list
pizza_and_prices.pop(-1)
#print(pizza_and_prices) to confirm

#Adding peppers to the list
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices) to confirm

three_cheapest = pizza_and_prices[:3]

print("Here is a list of our cheapest pizza!")
print(three_cheapest)
