#!/usr/bin/env python2.7

import hashlib, binascii, socket, sys

if len(sys.argv) < 3:
        sys.exit(1)

cn = sys.argv[1]
ticket_salt = sys.argv[2]

ticket = hashlib.pbkdf2_hmac('sha1', cn, ticket_salt, 50000)
print(binascii.hexlify(ticket))