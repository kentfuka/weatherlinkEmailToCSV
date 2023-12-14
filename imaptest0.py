from imapclient import IMAPClient
server = IMAPClient('imap.gmail.com', use_uid=True)
server.login('kent@querium.com', 'YOUR APP PASSWORD HERE')

# Test program that looks for email from April that is in INBOX.

select_info = server.select_folder('INBOX')
print('%d messages in INBOX' % select_info[b'EXISTS'])

messages = server.search(['FROM', 'aprilwarn@hotmail.com'])
print("%d messages from April" % len(messages))

for msgid, data in server.fetch(messages, ['ENVELOPE']).items():
    envelope = data[b'ENVELOPE']
    print('ID #%d: "%s" received %s' % (msgid, envelope.subject.decode(), envelope.date))

server.logout()
