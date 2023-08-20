
a='''paste your html element here'''


import pandas as pd
from bs4 import BeautifulSoup
from collections import Counter
soup = BeautifulSoup(a, 'html.parser')

# Find all the <p> elements with the specified class for company names
company_elements = soup.find_all('p', class_='MuiTypography-root MuiTypography-body2 css-kn20q1')

# Find all the <span> elements with the specified class for application status
status_elements = soup.find_all('span', class_='MuiChip-label MuiChip-labelSmall css-1pjtbja')

# Create a dictionary to store company names and statuses
company_status_dict = {}

# Iterate through the company and status elements and populate the dictionary
for company_element, status_element in zip(company_elements, status_elements):
    company_name = company_element.text
    status = status_element.text
    company_status_dict[company_name] = status

# Count the occurrences of different statuses
status_counter = Counter(company_status_dict.values())



for company, status in company_status_dict.items():
    print("Company Name:", company)
    print("Status:", status)
    print("------")



# Print the status count
for status, count in status_counter.items():
    print("Status:", status)
    print("Count:", count)
    print("------")

df = pd.DataFrame(company_status_dict, index=["Company","Status"]).T

# Save the DataFrame to a CSV file
csv_filename = "company_statuses.csv"
df.to_csv(csv_filename)

print(f"CSV file '{csv_filename}' created and saved successfully.")
