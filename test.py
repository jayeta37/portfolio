import os
from dotenv import load_dotenv
import smtplib
import time

import test

load_dotenv()

def test_smtp_login():
    try:
        start_time = time.time()
        smtp_server = os.getenv('MAIL_SERVER')
        port = os.getenv('MAIL_PORT')
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.quit()
        print(f"SMTP login successful in {time.time()-start_time} seconds")
        return True
    except Exception as e:
        print(f"SMTP login failed: {e}")
        return False
    

test_smtp_login()