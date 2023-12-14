### Process emails from Kent's weather station to generate a CSV file of weather statistics for processing in Google Sheets

NOTE: You ought to use a venv to run these python3 programs.

* imap2.csv has records from July 9 2020 through Dec 11, 2023.
* imap4.csv has Records from Sep 27 2018 through Jul 08 2020.

* imap2.csv: July 2020 through Dec 11, 2023
* imap2.json: July 2020 through Dec 11, 2023
* imap2.out: July 2020 through Dec 11, 2023
* imap2.py: Produces imap2.csv
* imap3.json: Just HTML records for old emails from 2018 - 2020
* imap3.out: Just HTML records for old emails from 2018 - 2020
* imap3.py: Produces imap3.csv
* imap4.csv: Records from Sep 27 2018 through Jul 08 2020
* imap4.json: Records from Sep 27 2018 through Jul 08 2020
* imap4.out: Records from Sep 27 2018 through Jul 08 2020
* imap4.py: Produces imap4.csv.  Deals with quirky HTML produced through July 8, 2020
* imaptest.py: Test program that searches INBOX rather than 'All Mail'
* imaptest.out: Output of imaptest.py
* imaptest0.py: Test program that looks for email from April that is in INBOX
* jsontocsv.py: Function to convert JSON to CSV (created by ChatGPT)
* parse.py: Test program for using lxml etree to find HTML tags

References:

1. https://gist.github.com/martinrusev/6121028
2. https://support.google.com/accounts/answer/185833
3. https://stackoverflow.com/questions/64391561/macos-python-says-module-not-found-but-its-already-installed
4. https://stackoverflow.com/questions/42413678/retrieve-attribute-names-and-values-with-python-lxml-and-xpath
5. https://stackoverflow.com/questions/2365411/convert-unicode-to-ascii-without-errors-in-python
