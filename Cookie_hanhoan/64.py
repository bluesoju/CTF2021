#!/usr/bin/env python3

import base64 as b64

flag = ''
with open('cipher.txt', 'r') as f:
  shouldContinue = True
  candidate = f.read().replace('\n', '').replace(' ', '')
  while shouldContinue:
    candidate = b64.b64decode(candidate)
    if b'Flag{' in candidate:
      flag = candidate.decode()
      shouldContinue = False

print(flag)
