import requests
import schedule
import time

phone_number = '8324506404'

#function to send a specific message on the specific day at an explicit time

def send_message_monday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Good evening, please vacuum the entire house and conduct the daily evening cleaning tasks',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())

def send_message_tuesday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Clean all the bathrooms, master, guest and spare upstairs',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())

def send_message_wednesday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Dust everything - fans, mantel, tvs, etc.',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())


def send_message_thursday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Mop all floors including bathroom areas',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())


def send_message_friday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Monthly chore, 1st = Wipe basboards and cabinets, 2nd = Clean stove and microwave, 3rd = Clean out fridge and freezer (garage and indoor) 4th = Clean windows inside and out',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())


def send_message_saturday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Conduct the laundry for the week and complete any project you have been wanting to get done',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())


def send_message_sunday():
    
    resp = requests.post('https://textbelt.com/text', { 
        'phone': phone_number,
        'message': 'Today is the rest day, enjoy the day off',
        'key': '271584dd4e6c4ae10499e6935b92b6cec7b81636wLKx2XL72qUrRid82P8l01KYv',
    })
    print(resp.json())

schedule.every().monday.at("19:00").do(send_message_monday)

schedule.every().tuesday.at("19:00").do(send_message_tuesday)

schedule.every().wednesday.at("19:00").do(send_message_wednesday)

schedule.every().thursday.at("19:00").do(send_message_thursday)

schedule.every().friday.at("19:00").do(send_message_friday)

schedule.every().saturday.at("19:00").do(send_message_saturday)

schedule.every().sunday.at("19:00").do(send_message_sunday)

while True:
    schedule.run_pending()
    time.sleep(0)

#just comment out for now 
#schedule.every(10).seconds.do(send_message)

#while True:
    #schedule.run_pending()
    #time.sleep(1)