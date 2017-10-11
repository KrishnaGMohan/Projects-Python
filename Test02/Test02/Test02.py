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

plt.plot(year, pop)
plt.show()
plt.clf()

plt.scatter(year, pop)
plt.show()
plt.clf()

plt.plot(year, pop)
plt.yscale('log')
plt.show()
plt.clf()


help(plt.hist)
#plt.hist(life_exp1950, bins=15)
