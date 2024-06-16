import pandas as pd
from datetime import datetime, date, time, timedelta

# def check_overlap_pandas(range1, range2):
#     interval1 = pd.Interval(range1[0], range1[1])
#     interval2 = pd.Interval(range2[0], range2[1])
#     return interval1.overlaps(interval2)

# # Example usage:
# range1 = (datetime(2024, 5, 25, 9, 30), datetime(2024, 5, 25, 11, 30))
# range2 = (datetime(2024, 5, 25, 10, 0), datetime(2024, 5, 25, 12, 0))

# overlap = check_overlap_pandas(range1, range2)
# print(f"Overlap: {overlap}")

year_2017 = pd.Interval(pd.Timestamp('2017-01-01'),pd.Timestamp('2018-01-01'), closed='left')
# print(pd.Timestamp('2017-01-06 00:00') in year_2017)
year_2018 = pd.Interval(pd.Timestamp('2017-01-01'),pd.Timestamp('2019-01-01'), closed='left')
print("2 year is overlap" + str(year_2017.overlaps(year_2018)))
# creating 1st interval 
interval1 = pd.Interval(5, 15) 
print('first interval is :' + str(interval1)) 

# creating 2nd interval 
interval2 = pd.Interval(10, 25) 

# checking whether the intervals overlap 
result = interval1.overlaps(interval2) 
print('second interval is :'+str(interval2)) 
str = 'yes' if result else 'no'

print('do the intervals overlap ? : '+str) 
