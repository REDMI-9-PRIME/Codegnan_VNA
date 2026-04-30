'''import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50],color = "yellow")
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("No of cars sold")
plt.show()

import matplotlib.pyplot as plt
sizes = [50, 30, 20]
labels = ["2024", "2025", "2026"]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Toy Sales")
plt.show()

import matplotlib.pyplot as plt
plt.pie([40,15,35],labels=["Python(backend)","Frontend(html,css,js)","flask"])
plt.title("ATM application")
plt.legend(["Sai","Akash","Abdul"])
plt.show()

import matplotlib.pyplot as plt
plt.scatter([1,2,3,4],[200,400,100,500],color="Yellow",s=100)
plt.title("swift car sales")
plt.xlabel("Years")
plt.ylabel("No. of Sales")
plt.show()'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

url = "http://books.toscrape.com/"

try:
    response = requests.get(url)
    response.encoding = 'utf-8'
    response.raise_for_status()

except requests.exceptions.RequestsException as e:
    print("Error Fetching data:",e)
    exit()
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

names = []
prices = []

for book in books:
    name = book.h3.a["title"]

    #Get raw price text
    price_text = book.find("p",class_="price_color").text
    price = float(re.findall(r'\d+\.\d+',price_text)[0])

    names.append(name)
    prices.append(price)

df = pd.DataFrame({
    "Book Name": names,
    "Price": prices
    })

print("\n Table Data:\n")
print(df.head())

#save to csv
df.to_csv("books_data.csv", index=False)
print("\n CSV file 'books_data.csv' created successfully!")

#Data Visualization
plt.figure()
plt.bar(names[:10], prices[:10]) # Top 10 books
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()


