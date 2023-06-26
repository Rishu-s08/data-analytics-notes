import pandas as pd
from urllib.request import urlretrieve
import matplotlib

# urlretrieve('https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'
            # , 'italy_covid_report')

covid_df = pd.read_csv('italy_covid_report')
# print(covid_df)
# print(covid_df.info())
# print(covid_df.describe())
# print(covid_df.columns)
# print(covid_df.shape)


'''Here's a summary of the functions & methods we've looked at so far:

    pd.read_csv - Read data from a CSV file into a Pandas DataFrame object
    .info() - View basic infomation about rows, columns & data types
    .describe() - View statistical information about numeric columns
    .columns - Get the list of column names
    .shape - Get the number of rows & columns as a tuple

'''

# print(type(covid_df)) 
# print(covid_df['new_cases'])
# print(type(covid_df['new_cases']))
# print(covid_df['new_cases'][245])
# print(covid_df.at[245, 'new_cases'])
# print(covid_df.new_cases)
# print(covid_df.new_cases[242])
# print(covid_df[['new_cases','date']])
# print(covid_df.loc[203])
# print(type(covid_df.loc[203]))
# print(covid_df.loc[203:220:2])
# print(covid_df.head(4))
# print(covid_df.tail(4))
# print(covid_df.sample(9))
# print(covid_df.new_tests.first_valid_index())




# print(covid_df.new_cases.sum())
# print(covid_df.new_deaths.sum())
# death_rate =  covid_df.new_deaths.sum()/covid_df.new_cases.sum()
# print("{:.3f} %".format(death_rate*100))

# intial_test = 9893898
# total_test = covid_df.new_tests.sum() + intial_test
# # print(total_test)




# cases_more_thousand = covid_df.new_cases > 1000
# print(cases_more_thousand)
# print(covid_df[cases_more_thousand])

# cases_more_thousand =  covid_df[covid_df.new_cases > 1000]
# print(cases_more_thousand)

# high_ratio = covid_df[covid_df.new_cases/covid_df.new_tests > covid_df.new_cases.sum()/covid_df.new_tests.sum()]
# print(high_ratio)

# covid_df['positive_rate'] = covid_df.new_cases/covid_df.new_tests
# print(covid_df)

# covid_df.drop(columns=['positive_rate'], inplace=True)
# print(covid_df)



# print(covid_df.sort_values(['new_cases'], ascending=False))
# print(covid_df.sort_values(['new_cases']).head(10))
# covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] +covid_df.at[173, 'new_cases'])/2 
# print(covid_df.at[172, 'new_cases'])


# print(covid_df.date)

# covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
# covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
# covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
# covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday

# print(covid_df)

# print(covid_df.groupby('month')[['new_cases', 'new_tests', 'new_deaths']].mean())

# print(covid_df[covid_df.month==5][['new_cases', 'new_tests', 'new_deaths']].sum())


covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()

print(covid_df)


urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')

locations_df = pd.read_csv('locations.csv', delimiter=',')
print(locations_df[locations_df.location == "Italy"])

covid_df['location'] = 'Italy'

merge_df = covid_df.merge(locations_df,on='location')
print(merge_df)


merge_df['cases_per_million'] = merge_df.total_cases * 1e6 / merge_df.population

merge_df['deaths_per_million'] = merge_df.total_deaths * 1e6 / merge_df.population

merge_df['tests_per_million'] = merge_df.total_tests * 1e6 / merge_df.population



result_df = merge_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]

result_df.to_csv('results.csv', index=None)


# print(result_df.new_cases.plot())

death_rate = result_df.total_deaths / result_df.total_cases

death_rate.plot(title='Death Rate')
print(matplotlib.pyplot.show())