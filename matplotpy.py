import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

###### LINE CHART

years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

# plt.plot(years, apples, marker='o', c='m', ls='--', mew=2)
# plt.plot(years, oranges, marker='x', c='r', mew=1, mec='b', ms=4)
# The fmt argument provides a shorthand for specifying the marker shape, line style, and line color. It can be provided as the third argument to plt.plot.

# fmt = '[marker][line][color]'

# plt.figure(figsize=(10,10))

# # plt.plot(years, apples, 's--b')
# plt.plot(years, oranges, 'o-r')
# plt.plot(years, apples, 'sr')

# plt.xlabel("years")
# plt.ylabel("Tons Per Hecter")
# plt.title("production graph")
# plt.legend(["Apples", "Oranges"])
# print(plt.show())





##### seaborn

# sns.set_style("whitegrid")
# plt.plot(years, oranges, 'o-r')
# plt.plot(years, apples, '*--b')

# plt.xlabel("years")
# plt.ylabel("Tons Per Hecter")
# plt.title("production graph")
# plt.legend(["Apples", "Oranges"])
# print(plt.show())


sns.set_style("darkgrid")
# plt.plot(years, oranges, 'o-r')
# plt.plot(years, apples, '*--b')

# plt.xlabel("years")
# plt.ylabel("Tons Per Hecter")
# plt.title("production graph")
# plt.legend(["Apples", "Oranges"])
# print(plt.show())




# ### SCATTERPLOT

# # # Load data into a Pandas dataframe
# # flowers_df = sns.load_dataset("iris") ##pd.read_csv same
# plt.figure(figsize=(10,6))
# # plt.title("Sepal Dimension")
# # # plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
# # # sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width)
# #               ##adding hue
# # sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width,
# #                 hue=flowers_df.species,
# #                 s=150)
     
# ##one liner
# # sns.scatterplot(x="sepal_length", y="sepal_width",
# #                 hue="species",
# #                 s=150,
# #                 data=sns.load_dataset("iris"))
# print(plt.show())


      

#### HISTOGRAM


# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print(flowers_df.sepal_width)
# plt.hist(flowers_df.sepal_width)
# plt.hist(flowers_df.sepal_width, bins=5)
# plt.hist(flowers_df.sepal_width, bins=np.arange(2,4.5, 0.25))
# plt.hist(flowers_df.sepal_width, bins=[2,2.5,4])



setosa_df = flowers_df[flowers_df.species == 'setosa'].sepal_width
versicolor_df = flowers_df[flowers_df.species == 'versicolor'].sepal_width
virginica_df = flowers_df[flowers_df.species == 'virginica'].sepal_width
# plt.hist(versicolor_df, bins=np.arange(2,4.5,0.25))
# plt.hist(setosa_df,alpha=0.5, bins=np.arange(2,4.5,0.25))
# plt.hist(virginica_df,alpha=0.3, bins=np.arange(2,4.5,0.25))

plt.hist([versicolor_df,setosa_df,virginica_df],
             bins=np.arange(2,4.5,0.25),
             stacked=True)

plt.legend(['Versicolor', 'Setosa', 'Virginica']);

print(plt.show())