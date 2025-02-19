from pytrends.request import TrendReq

import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Set up pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Set keywords and location
keywords = ['dichiarazione', 'redditi']
geo_location = 'IT'

# Get timeframe (last 5 years)
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=5 * 365)

# Convert dates to string format
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')

# Build the payload
pytrends.build_payload(keywords, cat=0, timeframe=f'{start_date_str} {end_date_str}', geo=geo_location, gprop='')

# Get interest over time
interest_over_time_df = pytrends.interest_over_time()

# Resample the data to get monthly values
monthly_interest_df = interest_over_time_df.resample('ME').sum()

# Display the results
print(monthly_interest_df)

# Plot the data
monthly_interest_df.plot()
plt.show()