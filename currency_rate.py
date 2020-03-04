import urllib
import pandas as pd
import numpy as np
import bs4
url = 'https://www.iban.com/exchange-rates'
print("Opening the file connection...")
uh= urllib.request.urlopen(url)
print("HTTP status",uh.getcode())
html =uh.read().decode()
soup=bs.BeautifulSoup(html,'html.parser')
currency=[]
for tag in soup.find_all('td'):
    currency.append(tag.text)
currency=np.array(currency);
currency=np.split(currency,len(currency)/4);
currency=pd.DataFrame(currency,columns=['a', 'b','c','d'])
currency=currency.drop(columns=['d']);
currency['a']=currency['a'].str.replace('\t','');
print(currency)