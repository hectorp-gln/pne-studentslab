temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

#The temperature on Wednesday (index 2)

print("Wednesday:", temperatures[2])

#The maximum temperature

max = 0
for temp in temperatures:
    if temp > max:
        max = temp
print("Max:", max)


#The minimum temperature

min = 100
for temp in temperatures:
    if temp < min:
        min = temp
print("Min:", min)

#The average temperature (rounded to 1 decimal)

total = 0
n = 0
for temp in temperatures:
    n += 1
    total += temp
print("Average:", round(total/n,1))


#The number of days above 17 degrees

over = 0
for temp in temperatures:
    if temp > 17:
        over += 1
print("Days above 17:", over)

#The list sorted from lowest to highest

temperatures.sort()
print("Sorted:",temperatures)
