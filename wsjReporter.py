import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen("https://www.wsj.com/market-data/bonds").read()
soup = bs.BeautifulSoup(sauce, "lxml") #turns parsed info into soup object in order to interact with data

rates = []
ratesList = []
for line in soup.find_all('td', class_ = 'WSJTables--table__cell--2dzGiO7q'):
    sentence = line.text #stores as list
    rates.append(sentence)

ratesList.append(rates[1])
ratesList.append(rates[6])
ratesList.append(rates[11])
ratesList.append(rates[16])
ratesList.append(rates[21])
ratesList.append(rates[26])
ratesList.append(rates[31])
print(ratesList)
data = [ratesList]
df = pd.DataFrame(data, columns = ["Overnight", "1 Week", "1 Month", "2 Month", "3 Month", "6 Month", "1 Year"])
df.to_excel("WSJ Reporter.xls")