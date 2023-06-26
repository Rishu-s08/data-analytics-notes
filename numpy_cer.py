import numpy as np
kanto = np.array([73, 67, 43])
weights =  np.array([.3,.2,.5])

print(type(kanto))

# Just like lists, Numpy arrays support the indexing notation [].
print(weights[0])


# Operating on Numpy arrays

# We can now compute the dot product of the two vectors using the np.dot function.

np.dot(kanto, weights)
# dot funtion doing same as 
# def crop_yield(region, weights):
    # result = 0
    # for x, w in zip(region, weights):
    #     result += x * w
    # return result

# We can achieve the same result with low-level operations supported by Numpy arrays: performing an element-wise multiplication and calculating the resulting numbers' sum.

(kanto*weights).sum()


climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])
arr3 = np.array([
    [[11, 12, 13], 
     [13, 14, 15]], 
    [[15, 16, 17], 
     [17, 18, 19.5]]])
print(arr3.shape)
print(arr3.dtype)
print(climate_data.dtype)
print(climate_data.shape)

print(np.matmul(climate_data, weights))
print(climate_data @ weights)

# import urllib.request

# urllib.request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
#     'climate.txt')

# climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)

# print(climate_data.shape)

# yields = climate_data @ weights

# print(yields)

# climate_result = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
# print(climate_result)

# np.savetxt('climate_result.txt',
#            climate_result,
#            fmt='%.2f',
#            delimiter=', ',
#            header='temperature,rainfall,humidity,yeild_apples',
#            comments='checking wtf is comments\n')


arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])

arr3 = np.array([[11, 12, 13, 14], 
                 [15, 16, 17, 18], 
                 [19, 11, 12, 13]])

print(arr2+3)
print(arr2%3)
print(arr3 - arr2)
print(arr3 / arr2)
print(arr3 * arr2)


arr4 = np.array([4, 5, 6, 7])

print(arr4+arr2)



arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

print(arr1==arr2)
print(arr1!=arr2)
print(arr1>=arr2)
print(arr1<=arr2)

# Array comparison is frequently used to count the number of equal elements 
# in two arrays using the sum method. Remember that True evaluates to 1 
# and False evaluates to 0 when booleans are used in arithmetic operations.
print((arr1==arr2).sum())




arr3 = np.array([
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 
    
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])

print(arr3.shape)
print(arr3[2,1,2])
print(arr3[1:,:,2:])
print(arr3[0:1,1,2])
print(arr3[2])
print(arr3[2,1])


# All zeros
print(np.zeros((3, 2)))

#all ones
print(np.ones((3,12,2)))

# Identity matrix
print(np.eye(4))

#random vextor
print(np.random.rand(2,2))

#random matrix
print(np.random.randn(2,2))

# Fixed value
np.full([2, 3], 42)

#range with start, end and step
print(np.arange(10, 90, 5))


