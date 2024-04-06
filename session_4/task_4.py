import csv
cars = []
with open("C:/Users/ahsan/OneDrive/Desktop/couch_to_coder/session_4/vw.csv", "r") as csvfile:
 print(csvfile)
 reader = csv.reader(csvfile, skipinitialspace=True)
 for row in reader:
     new_car = {}
     new_car["model"] = row[0]
     new_car["year"] = row[1]
     new_car["price"] = row[2]
     new_car["transmission"] = row[3]
     new_car["mileage"] = row[4]
     new_car["fuelType"] = row[5]
     new_car["tax"] = row[6]
     new_car["mpg"] = row[7]
     new_car["engineSize"] = row[8]
     cars.append(new_car)


# What is the most expensive car?
count =0
expensive_car=cars[1]
for car in cars:
   if(count==0):
    count+=1 # For ignoring the first row with the title
   else:
     if(int(car['price'])>int(expensive_car['price'])):
       expensive_car = car

print(f"The most expensive car is{expensive_car['model']} of price {expensive_car['price']}")


# Finding all the VW Golf models and calculating the average price

count=0
vw_golf=[]
total_price_vw_golf=0
for car in cars:
  if(count==0):
    count+=1 # For ignoring the first row with the title
  else:
    if("golf" in car['model'].lower()):
      #print(car)
      total_price_vw_golf+=int(car['price'])
      vw_golf.append(car)

print(f"Average price for VW Golf car is: {total_price_vw_golf/len(vw_golf):.2f}")

# What is the average mileage for VW Polo models registered in 2020?

count=0
vw_polo_total_mileage=0
no_of_polo_cars=0

for car in cars:
  if(count==0):
     count+=1 # For ignoring the first row with the title
  else:
    
    if(("polo" in car['model'].lower().strip()) and (car['year'].strip()=='2020')):
      vw_polo_total_mileage+= int(car['mileage'])
      no_of_polo_cars+=1

print(f"Average mileage for VW Polo car is: {vw_polo_total_mileage/no_of_polo_cars:.2f}")
 								

# Extensions

# A pie chart showing the distribution between fuel types.
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/ahsan/OneDrive/Desktop/couch_to_coder/session_4/vw.csv")
data.head()

number_of_fule_types = data.groupby('fuelType')[['model']].count().sort_values("model",ascending=False).head(10).reset_index()
print(number_of_fule_types)

plt.pie(number_of_fule_types.model,labels=number_of_fule_types.fuelType)
plt.show()

#A bar chart showing the average mileage for each model. 
group_by_avg_mileage= data.groupby('model').mileage.mean().reset_index()
print(group_by_avg_mileage)

plt.bar(group_by_avg_mileage.model,group_by_avg_mileage.mileage,color='green',width=0.2)
plt.xlabel("Model")
plt.ylabel("Mileage")
plt.title("Average mileage by model")
plt.show()