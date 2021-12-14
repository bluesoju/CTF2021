_encode = '6c464b4d514b744817491714487449174b57'.decode('hex')

for x in range(255):
    text = ''

    for l in _encode:
        m = l.encode('hex')
        m = int(m,16)^x
        if 31<m and m<128:
            text += chr(m)

    if len(text)==len(_encode):
        print text
