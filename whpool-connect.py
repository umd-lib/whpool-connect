#!/usr/bin/env python3

import os

from imapclient import IMAPClient
from dotenv import load_dotenv

# Establish a simple connection over IMAP. The purpose is to prevent
# Gmail from marking the Less Secure App as disabled due to no connections
# within the last month.
# See https://workspaceupdates.googleblog.com/2019/07/limit-access-LSA.html

# Add any environment variables from .env
load_dotenv('.env')

# Get environment variables
env = {}
for key in ('WHPOOL_IMAP_HOST', 'WHPOOL_IMAP_USERNAME', 'WHPOOL_IMAP_PASSWORD'):
    env[key] = os.environ.get(key)
    if env[key] is None:
        raise RuntimeError(f'Must provide environment variable: {key}')

client = IMAPClient(env['WHPOOL_IMAP_HOST'])
response = client.login(env['WHPOOL_IMAP_USERNAME'], env['WHPOOL_IMAP_PASSWORD'])
print(response)

info = client.select_folder('INBOX')
print('%d messages in INBOX' % info[b'EXISTS'])

client.logout()
