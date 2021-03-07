import webvtt
from collections import defaultdict 

import http.client, urllib.request, urllib.parse, urllib.error, base64
import ast

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'Rwqm8kJI4m23ErDDUETNmrfLIQYQk1mEZQdk3bJ2yGgP'
url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/da1b4bd0-109f-496a-a543-6b734fcca3b7'

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '627c2268f99740fd98c9007b59ad45e2'
}
params = urllib.parse.urlencode({
})
conn = http.client.HTTPSConnection('api.tisane.ai')


def time_to_int(timestr):
    ftr = [3600,60,1]
    return sum([a*b for a,b in zip(ftr, map(float,timestr.split(':')))])

def get_data(text):
    t = '{"content":' + '"' + text + '"' + ',"language":"en", "settings":{"parses":false}}'
    conn.request("POST", "/parse?%s" % params, t, headers)
    response = conn.getresponse()
    data = response.read()
    test_string = str(data, 'utf-8')
    res = ast.literal_eval(test_string)
    data = [None, None, None]
    try: 
        data[0] = res['abuse'][0]['type']
        data[1] = res['abuse'][0]['severity']

    except:
        pass
    try:
        res = ta.tone_chat([{'text': text}]).get_result()
        data[2] = res['utterances_tone'][0]['tones'][0]['tone_id']
    except:
        pass
    return data
person = {
    'total': {'duration': 0, 'count':'0'},
    'speech':{
        # text: (bullying_type, )

    }
}
everyone = defaultdict(lambda:person)

for caption in webvtt.read('97807885687_audio_transcript.vtt'):
    text= caption.text.split(':')
    data = get_data(text[1])
    duration = time_to_int(caption.end) - time_to_int(caption.start)
    everyone[text[0]]['total']['duration'] += duration
    everyone[text[0]]['speech'][text[1]] = data
    print(duration)
    # print(caption.start - caption.end)
everyone = dict(everyone)
print(everyone)
