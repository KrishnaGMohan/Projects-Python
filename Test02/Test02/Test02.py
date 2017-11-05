import numpy as np

x = [3, 6, -5, 8]
np_x = np.array(x)
print(np_x)
print(type(np_x))

np_2d = np.array([[0,1,2,3],[10,4,-12,13]])
print(np_2d[1,3])


print(np_2d.shape)
print(np.mean(np_2d[1,:]))
print(np.median(np_2d[1,:]))
print(np.std(np_2d[1,:]))
print(np.corrcoef(np_2d[0,:], np_2d[1,:]))

print(np.sum(np_2d[:,:]))
print(np.sort(np_2d[1,:]))


height = np.round(np.random.normal(1.75, 0.2, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
print(np_city.shape)

#---------------------------------------------------------------------

import matplotlib.pyplot as plt
year = [1950,1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

#plt.plot(year, pop)
#plt.show()
#plt.clf()

#plt.scatter(year, pop)
#plt.show()
#plt.clf()

#plt.plot(year, pop)
#plt.yscale('log')
#plt.show()
#plt.clf()


#help(plt.hist)
#plt.hist(life_exp1950, bins=15)

#plt.plot(year, pop)
#plt.xlabel('Year')
#plt.ylabel('Popolation')
#plt.title('World Population Projections')
#plt.yticks( [0, 2, 4, 6, 8, 10],
#            [0, '2B', '4B', '6B', '8B', '10B'])
#plt.grid(True)
#plt.text(1550, 71, 'India')
#plt.text(5700, 80, 'China')
#plt.show()
#plt.clf()


#-------------------------------------------


world = {"afganistan":30.55, "albania":2.77, "algeria": 39.21 }

print(world["albania"])
print(world.keys())

t = {"a":3,  "b":4, "a":2}
print(t.keys())
print(t["a"])  # prints all 'a'
del(t["a"]) # deletes all 'a'
print(t)


#---------------------------------------------

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names, 'drives_right':dr, 'cars_per_cap': cpc }

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
	
# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

#AWCustomers = pd.read_csv('D:\Personal\OneDrive\Projects\Projects-R\MPPFinal\MPPFinal\AWCustomers.csv', index_col = 0)
#print(AWCustomers)

#-----------------------------------------
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for k, v in europe.items() :
    print("the capital of " + k + " is " + v)
    
  
for lab, row in cars.iterrows() :
    print(lab + ": "+ str(row["cars_per_cap"]))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()


# Print cars
print(cars)


# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

print(cars)

#---------------------------------------------------
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))