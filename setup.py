import pywhatkit
import datetime

def get_hour_minute():
    now = datetime.datetime.now()
    return now.hour, now.minute

def send_whatsapp_to_group(text_input):
    hour,min = get_hour_minute()
    pywhatkit.sendwhatmsg_to_group('GqyKuUIfdLm6x2SrlFWbFg', text, time_hour=hour, time_min=min+2, tab_close=True, close_time=3)

def main():
    send_whatsapp_to_group('Test')
    
if __name__ == "__main__":
    main()