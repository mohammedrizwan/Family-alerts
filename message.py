"""
Created on 3 Sep 2015

@author: Mohammed Rizwan
"""

# Import smtplib for the actual sending function
import datetime
import smtplib
import sqlite3
import time
import logging

logging.basicConfig(filename='emaillogs.txt', level=logging.INFO)
createDb = sqlite3.connect('familydatabase.db')
queryCurs = createDb.cursor()


def send_message(email_address, content):
    try:
        mail = smtplib.SMTP('smtp.live.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('khan.mo99@hotmail.co.uk', '12984964MR ')
        mail.sendmail('khan.mo99@hotmail.co.uk', email_address, content)
        mail.close()
        print('emails sent sucessfully %s' % email_address)
        logging.info('email sent to %s', email_address)
    except smtplib.SMTPException:
        print('error sending email to : %s' % email_address)


def check_database(day, month):
    queryCurs.execute('SELECT fname, sname, email FROM people WHERE day = ? AND month = ?', (day, month))
    data = queryCurs.fetchall()
    print data

    if len(data) == 0:
        print('no one has birthday today')
    else:
        people = ""
        for i in data:
            people = people+", "+(i[0])+' '+(i[1])
            subject = 'Happy Birthday'
            text = ('Wishing you a special happy birthday %s, %s, and may ALLAH make all your dreams come true'
                    % ((i[0]), (i[1])))
            content = 'Subject: %s\n\n%s' % (subject, text)
            send_message((i[2]), content)

        queryCurs.execute('SELECT email FROM people WHERE day != ? AND month != ? AND alert != 0',
                          (day, month,))
        emaildata = queryCurs.fetchall()
        print emaildata
        subject = 'Birthday Alert'
        text = ('Today is %s birthday. ' % people)
        content = 'Subject: %s\n\n%s' % (subject, text)
        for i in emaildata:
            send_message(i, content)

def check_broadcast():
    queryCurs.execute('SELECT subject, message, checks FROM emergency WHERE id =1')

    data = queryCurs.fetchall()


    for i in data :
        subject = (i[0])
        message = (i[1])
        check = (i[2])
    emails =" "
    if check == 1:
         queryCurs.execute('SELECT email FROM people')
         emaildata = queryCurs.fetchall()
         for i in emaildata :
            print (i[0])
            emails = emails+";"+(i[0])
            print emails



    else :
        return




if __name__ == "__main__":
    while True:
        check_broadcast()
        '''
        now = datetime.datetime.now()
        if now.hour == 11 & now.minute == 30:
            check_database(now.day, now.month)
        else:
            time.sleep(1)
            #logging.info('this is the time %s', now)
        '''