import urllib.request, urllib.parse, urllib.error
import json, ssl
import sqlite3
import datetime
import time

url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd&include_24hr_change=true'

ctx = ssl.create_default_context()


req = urllib.request.Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
conn = sqlite3.connect('crypto_data.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Prices (id INTEGER PRIMARY KEY, coin TEXT, price REAL, change_24h REAL, timestamp TEXT)')

while True :
    try:
        op = urllib.request.urlopen(req, context=ctx)
        data = op.read().decode()
        info = json.loads(data)
       
        for coin, details in info.items() :
           price = details['usd']
           change_24h = details['usd_24h_change']
           now = str(datetime.datetime.now())
           cur.execute('INSERT INTO Prices (coin, price, change_24h, timestamp) VALUES (?, ?, ?, ?)',(coin, price, change_24h, now))
        conn.commit()

        cur.execute('SELECT coin, price, change_24h, timestamp FROM Prices')
        for row in cur :
           print(row[0],'Price:',row[1],'Change in 24h:',row[2],'Time:',row[3])

        print('--- Average Prices ---')
        cur.execute('SELECT coin, AVG(price) FROM Prices GROUP BY coin')
        for row in cur :
           print(row[0],'Average Price:',round(row[1],2))
        print('-----------------------')

        print('--- Max & Min Prices ---')
        cur.execute('SELECT coin, MAX(price), MIN(price) FROM Prices GROUP BY coin')
        for row in cur :
            print(row[0],'Max:',round(row[1],2),'| Min:',round(row[2],2))
            
        print('Data saved successfully! Waiting 30 seconds...')

    except Exception as e:
       print("Error occurred:",e)

    time.sleep(30)



