
from twilio.rest import Client
account_sid = 'AC83362a0105ba10e6022496ddd9574b12'
auth_token = '60064eb296c19552875ad031bcfa10c9'
client = Client(account_sid, auth_token)
mobile='03218337902'
new_mobile='+92'
newstr = mobile[:0] + mobile[1:]
new_mobile=new_mobile+newstr
# message = client.messages.create(
#                               from_='+12244772647', #(224) 477-2647
#                               body='body',
#                               to=new_mobile
#                           )
#
# print(message.sid)
# import requests
# requests.post('https://textbelt.com/text', {
#   'phone': new_mobile,
#   'message': 'Hello world',
#   'key': '19d1fe5c57553f4c25d2dd174096584f095943ecTVuiFZBMKNGSfmxW857RN6sbY',
# })

import plivo

AUTH_ID = "MANJJLZTG4ZJLJYWVLMD"
AUTH_TOKEN = "ZDc4Y2FjNTZhZmViM2QxOTRjNTg2OTg2NmViYWNk"
api = plivo.RestAPI(AUTH_ID, AUTH_TOKEN)
params = {'src': 'XXXXXXXXXXX', 'dst': 'XXXXXXXXXXX', 'text': 'Hi.. How r u ??',
          'url': "https://api.plivo.com/v1/Account/MAMJJIMWU0NJK1MDZMNT/Message/"}
response = api.send_message(params)
