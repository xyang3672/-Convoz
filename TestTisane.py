#!/usr/bin/env python3

import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '627c2268f99740fd98c9007b59ad45e2'
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.tisane.ai')
    conn.request("POST", "/parse?%s" % params, '{"content":"i hate u","language":"en"}', headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
