import requests
import schedule
import time
from phone_number import phone_number


class text_message:
    def __init__(self, temperature, humidity):
        self.__init__
        self.temperature = temperature
        self.humidity = humidity
        self.phone_number = phone_number

    def weather():
        print("hello")

    def send_message_monday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Good evening, please vacuum the entire house and conduct the daily evening cleaning tasks',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_tuesday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Clean all the bathrooms, master, guest and spare upstairs',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_wednesday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Dust everything - fans, mantel, tvs, etc.',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_thursday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Mop all floors including bathroom areas',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_friday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Monthly chore, 1st = Wipe basboards and cabinets, 2nd = Clean stove and microwave, 3rd = Clean out fridge and freezer (garage and indoor) 4th = Clean windows inside and out',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_saturday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Conduct the laundry for the week and complete any project you have been wanting to get done',
            'key': 'textbelt',
        })
        print(resp.json())

    def send_message_sunday(self):

        resp = requests.post('https://textbelt.com/text', {
            'phone': phone_number,
            'message': 'Today is the rest day, enjoy the day off',
            'key': 'textbelt',
        })
        print(resp.json())


schedule.every().monday.at("19:00").do(send_message_monday())

schedule.every().tuesday.at("19:00").do(send_message_tuesday())

schedule.every().wednesday.at("19:00").do(send_message_wednesday())

schedule.every().thursday.at("19:00").do(send_message_thursday())

schedule.every().friday.at("19:00").do(send_message_friday())

schedule.every().saturday.at("19:00").do(send_message_saturday())

schedule.every().sunday.at("19:00").do(send_message_sunday())

while True:
    schedule.run_pending()
    time.sleep(0)
