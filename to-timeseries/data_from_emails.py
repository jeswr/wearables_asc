#!/usr/bin/python3

import argparse
import smtplib

from mailer import Mailer

mail = Mailer(email='someone@outlook.com', password='your_password')
mail.settings(provider=mail.MICROSOFT)
mail.send(receiver='someone@example.com', subject='TEST', message='From Python!')


parser = argparse.ArgumentParser(description="Collect emailed timeseries data")


parser.add_argument('--server', nargs=1, default='smtp.office365.com:587',
                    help="""Send emails using a different server.
        SERVER = server:port""")

args = parser.parse_args()



with IMAPClient(self.host) as server:
    server.login(self.username, self.password)
    server.select_folder('INBOX')
    messages = server.search(['UNSEEN', ])  # in your case: ['FROM', 'email@outlook.example']

    # for each unseen email in the inbox
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_message = mailparser.parse_from_string(message_data[b'RFC822'])

# serverURL, port = args.server.split(":")
# server = smtplib.SMTP(serverURL, port)
