import os 
import random
import twilio.rest import TwilioRestClient
import subprocess
import sys
from time import strftime

#checking for usernames with my sessions. Exit if no sessions are found.
output = subprocess.check_output('who')
if 'my_username' not in output:
	sys.exit()

twilio_id = os.environ.get('twilioid')
twilio_auth_token = os.environ.get('twilio auth token')

#store the phone number in two variables so that we can access it later

myNumber = '+jks'
herNUmber = 'zyd'

reasons = ['Working really hard',
'Gotta deploy this',
'Will get back real quick']


client = TwilioRestClient(TWILIO_SID,TWILIO_AUTH )

client.messages.create(
to=herNUmber
from_=myNumber
body="Late at work."+ random.choice(reasons)
	)
print("Message sent at " + strftime("%a, %d %b %Y %H:%M:%S"))


