from imapclient import IMAPClient
import email
server = IMAPClient('imap.gmail.com', use_uid=True, ssl=True)
server.login('kent@querium.com', 'YOUR APP PASSWORD HERE')

folders = server.list_folders(directory='', pattern='*')
# print('Folders: ',folders)

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])
# select_info = server.select_folder('[Gmail]/All Mail')
# print('%d messages in [Gmail]/All Mail' % select_info[b'EXISTS'])

messages = server.search(['FROM', 'aprilwarn@hotmail.com'])
print("%d messages from April" % len(messages))
# messages = server.search(['FROM', 'noreply@weatherlink.com'])
# print("%d messages from noreply@weatherlink.com" % len(messages))

response = server.fetch(messages, ['ENVELOPE','RFC822','BODY[TEXT]'])

for msgid, data in response.iteritems():
    envelope = data[b'ENVELOPE']
    parsedEmail = email.message_from_string(data['RFC822'])
    body = email.message_from_string(data['BODY[TEXT]'])
    parsedBody = parsedEmail.get_payload(0)
    print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))
    print('ID #%d: ', parsedBody)
    exit()

server.logout()
