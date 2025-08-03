from twilio.rest import Client
from datetime import datetime,timedelta
import time

account_sid = 'AC612d57e02e2a94f4d07d0fe94091a95e'
auth_token = '121062cf08565a7e149d5104b68624db'

Client = Client(account_sid, auth_token)

def sent_whatapp_message(recipient_number, message_body,):
    try:
        message = Client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

name = input('Enter the recipient name =')
recipient_number = input('Enter the recipient whatsapp number with country code (e.g, +12345):')
message_body = input('enter the message you want to send to {name}:')

date_str = input('enter the date to send the message (YYYY-MM-DD):')
time_str = input('enter the time to send the message (HH:MM in 24hour format):')

schedule_datetime = datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime = datetime.now()

time_difference = schedule_datetime - current_datetime
delay_second = time_difference.total_seconds()

if delay_second <= 0:
    print('The specified time is in the past. Please enter a future date and time:')
else:
    print(f'message schedule to be sent to {name} at {schedule_datetime}.')

    time.sleep(delay_second)

    sent_whatapp_message(recipient_number, message_body)
