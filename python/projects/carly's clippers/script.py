hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

#add each price to the variable total_price.
for price in prices:
  total_price = total_price + price

#calculate avearage price
average_price = total_price / len(prices)

print("Average Haircut Price: \n" + str(average_price))

#make a list called new_prices, which has each element in prices minus 5
new_prices = [price - 5 for price in prices]

print(new_prices)

#Create a variable called total_revenue and set it to 0.
total_revenue = 0

#Use a for loop to create a variable i that goes from 0 to len(hairstyles)
for i in range(len(hairstyles)):
    #Add the product of prices[i] (the price of the haircut at position i) and 
    # last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: \n" + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: \n" + str(average_daily_revenue))

#create a list of cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]

print("Haircuts under $30: \n" + str(cuts_under_30))


