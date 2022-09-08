import random 
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
print(classes_per_week,type(classes_per_week))
cost_per_class = (cost_per_week/classes_per_week)
print(cost_per_class, type(cost_per_class))
print("Classes only cost:", cost_per_class)

#Part B
my_list = ("Frank","Kanye","Tyler","Earl","Donald")
rando = random.choice(my_list)
print(rando)