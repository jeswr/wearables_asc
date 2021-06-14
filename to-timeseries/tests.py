#!/usr/bin/python3

from imapclient import IMAPClient
import pandas as pd
import os

EEG = {}
FFT_WaveBands_Motion = {}
with IMAPClient('outlook.office365.com', port=993) as server:
    server.login(os.environ.get('EMAIL_USERNAME'), os.environ.get('EMAIL_PASSWORD'))
    server.select_folder('INBOX')
    
    messages = server.search(['SUBJECT', 'EEG'])
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        EEG[uid] = str(message_data)

    messages = server.search(['SUBJECT', 'FFT_WaveBands_Motion'])
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        FFT_WaveBands_Motion[uid] = str(message_data)

cleaned = {}
for key, val in EEG.items():
    cleaned[key] = pd.DataFrame([int(x) for x in EEG[key].split('EEG,\\r\\n')[-1].split(',\\r\\n') if not '\\' in x])
    print(cleaned[key])
    # print(len(cleaned[key]))

cleaned = {}
for key, val in FFT_WaveBands_Motion.items():
    cleaned[key] = pd.DataFrame([x.split(',') for x in FFT_WaveBands_Motion[25320].split('Magnitude,\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n')[-1].replace('=\\r\\n','').split('\\r\\n') if ',' in x and ':' in x and not 'a' in x and not 'b' in x], dtype=float)
    # print(cleaned[key].iloc[0])