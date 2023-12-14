from imap_tools import MailBox, AND
from lxml import etree
import re
import datetime

# Version 4 that deals with quirky HTML produced through July 8, 2020

# Get body of all emails from INBOX folder that match the weather report subject
with MailBox('imap.gmail.com').login('kent@querium.com', 'YOUR APP PASSWORD HERE',initial_folder='[Gmail]/All Mail') as mailbox:
    for msg in mailbox.fetch(AND(subject='Daily Summary Email for Lamy Ridge Observatory',sent_date_lt=datetime.date(2020, 7, 9))):
        print(msg.date, msg.subject, len(msg.text or msg.html))
        # if (re.match(r"Daily Summary Email for Lamy Ridge Observatory",msg.subject)):
        # print('Hit')
        # print(msg.html)
        # Find the header table that includes the report date
        span = etree.HTML(msg.html).xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span")
        datetext = str(span[0].text).strip()
        print('{')
        print('"date":"'+datetext+'",')
        print('"html":"'+msg.html+'",')
        # Convert utf-8 html text to plain ascii
        htmlascii = msg.html.encode('ascii', 'backslashreplace')
        # print('htmlascii: ',htmlascii)
        print('"ascii":'+str(htmlascii)+',')
        # Find the table that includes the sensor data
        # target_id = 'allSensorData'
        results = etree.HTML(htmlascii).xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr")
        if results:  # If no results, ignore the table data
            rows = iter(results)
            for row in rows:
                # print('row:',row)
                ix = 0;
                for td in row.iter('td'):
                    # print('td:',td)
                    text = str(td.text).strip()
                    if (ix == 0):
                        text0 = text
                        ix = 1;
                    elif (ix == 1):
                        text1 = text
                        ix = 0
                        print('"'+text0+'":"'+text1+'",')
        print('"end":""')
        print('},')
