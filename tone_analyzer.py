#Authenticate
apikey = 'Rwqm8kJI4m23ErDDUETNmrfLIQYQk1mEZQdk3bJ2yGgP'
url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/da1b4bd0-109f-496a-a543-6b734fcca3b7'

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(url)
chat = [
    {'text': 'I am feeling amazing',
     'user': 'ABC'},
    {'text': 'You suck',
     'user': 'DEF'},
    {'text': 'You are dumb',
         'user': 'DEF'}
]
res = ta.tone('I am feeling amazing').get_result()
output = ta.tone_chat(chat).get_result()
print(output)

# load transcript
# for each line, store them into a dictionary with user and text
# ta.tone_chat(chat).get_result()




# email(json)


# {user: 'name'
# assessment: 0 to 100
# bully: 0 or 1
# emotion: anger, impolite, joy (most used emotions)

# }



# html

# php and flask
