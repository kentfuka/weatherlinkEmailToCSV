from imapclient import IMAPClient
import email
from lxml import etree                                  
import re
server = IMAPClient('imap.gmail.com', use_uid=True, ssl=True)
server.login('kent@querium.com', 'YOUR APP PASSWORD HERE')

# Test program that searches INBOX rather than 'All Mail'

inboxInfo = server.select_folder('INBOX')
# inboxInfo = server.select_folder('[Gmail]/All Mail')
# messages = server.search(['FROM', 'aprilwarn@hotmail.com'])
messages = server.search(['FROM', 'noreply@weatherlink.com'])
response = server.fetch(messages, ['RFC822', 'BODY[TEXT]'])

for msgid, data in response.items():
        parsedEmail = email.message_from_string(data['RFC822'])
        body = email.message_from_string(data['BODY[TEXT]'])
        parsedBody = parsedEmail.get_payload(0)
        # print(parsedBody)
        span = etree.HTML(parsedBody).xpath("//table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span")                                                  
        datetext = str(span[0].text).strip() 
        print('{')                                                                                                                                                                              
        print('"date":"'+datetext+'",') 
        target_id = 'allSensorData'                                                                                                                                                     
        results = etree.HTML(s).xpath("//table[@id = '%s']/tbody/tr" % target_id)                                                                                               
        if not results:                                                                                                                                                 
            raise Exception("target_id does not exist")                                                                                                         
                                                                                                                                                        
        rows = iter(results)                                                                                                                    
        for row in rows:                                                                                                                
            for tr in row.iter('tr'):                                                                                           
                text0 = str(tr[0].text).strip()                                                                                 
                text1 = str(tr[1].text).strip()                                                                                         
                print('"'+text0+'":"'+text1+'",')                                                                                               
        print('"end":""')                                                                                                                               
        print('},')
        ###
        
        server.logout()
        
