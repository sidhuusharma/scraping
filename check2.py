from bs4 import BeautifulSoup
#from twilio.rest import Client
import datetime
import time
# Your Account SID from twilio.com/console
#account_sid = ""
# Your Auth Token from twilio.com/console
#auth_token  = ""
#client = Client(account_sid, auth_token)
import requests
import  sqlite3
conn = sqlite3.connect('score.db')
c = conn.cursor()
c.execute('''CREATE TABLE cricket(description TEXT, location TEXT, current TEXT)''')
#c.execute('''DROP TABLE criket''')
html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text
soup = BeautifulSoup(html_text, "html.parser")
sect = soup.find_all('div', class_='sp-scr_wrp')
section = sect[0]
description = section.find('span', class_='description').text
location = section.find('span', class_='location').text
current = section.find('div', class_='scr_dt-red').text
c.execute('''INSERT INTO cricket VALUES(?,?,?)''',(description,location,current))
link = "https://sports.ndtv.com/" +\
	section.find('a', class_='scr_ful-sbr-txt').get('href')
conn.commit()
c.execute('''SELECT * FROM cricket''')
results = c.fetchall()[0]
print(results)
#for each in results:
#        to_send = results
 #       message = client.messages.create(
  #          to="whatsapp:+918091759784", #replace zeros with sender's number
   #         from_="whatsapp:+14155238886", #Replace zeros with twilio's number
    #        body=to_send)
     #   time.sleep(2)
      #  print(message)
       # if counter>15:
            #Security check loop , so in case somehow anything make list big enough it don't kill their server
        #    break
    #print("Process Finished","\nTotal messages send = ",counter)
#print(description)

#print(location)

#print(current)
