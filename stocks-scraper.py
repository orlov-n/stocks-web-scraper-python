import pandas as pd
import requests
import ssl
from bs4 import BeautifulSoup
from io import StringIO
import warnings
# Ignore all warnings
#warnings.filterwarnings("ignore", category=FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data  = requests.get(url).text
print('check your data', data)

soup = BeautifulSoup(data, 'html.parser')

netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
print(netflix_data)

# creates a new empty DataFrame in pandas with specified column names. 
#   loop through each row and find all the column values for each row
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    # Ensure that there are enough columns
    if len(col) == 7:  # Adjust based on the number of columns you expect
        date = col[0].text
        open_ = col[1].text
        high = col[2].text
        low = col[3].text
        close = col[4].text
        adj_close = col[5].text
        volume = col[6].text
    
    # append the data of each row to the table
        netflix_data = pd.concat([netflix_data, pd.DataFrame({
            "Date": [date], 
            "Open": [open_], 
            "High": [high], 
            "Low": [low], 
            "Close": [close], 
            "Adj Close": [adj_close], 
            "Volume": [volume]
        })], ignore_index=True)

# Display the first few rows of the DataFrame
print(netflix_data.head())