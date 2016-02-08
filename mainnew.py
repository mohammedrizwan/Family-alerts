"""
Created on 1 Sep 2015

@author: Mohammed
"""

# menu for database programme
import sqlite3
import message
import time
import sys

createDb = sqlite3.connect('familydatabase.db')
queryCurs = createDb.cursor()


def create_table():
    queryCurs.execute('''CREATE TABLE IF NOT EXISTS people
    (id INTEGER PRIMARY KEY,fname TEXT,sname TEXT,day INTEGER,month INTEGER,year INTEGER,tel TEXT,email TEXT,
    alert INTEGER,messagesent INTEGER)''')

def create_table_broadcast():
    queryCurs.execute('''CREATE TABLE IF NOT EXISTS emergency (id INTEGER PRIMARY KEY,subject TEXT,message Text,checks INTEGER )''')

def adde_message(e_subject,e_message, checks):
    queryCurs.execute('''UPDATE emergency SET (subject,message, checks)
    VALUES (?,?,?)''', (e_subject,e_message,checks))
'''
    UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;
subject = ? ,message = ? , checks = ? WHERE id = 1
'''

def addperson(fname, sname, day, month, year, tel, email, alert):
    queryCurs.execute('''INSERT INTO people (fname,sname,day,month,year,tel,email,alert)
    VALUES (?,?,?,?,?,?,?,?)''', (fname, sname, day, month, year, tel, email, alert))


def deleteperson(d_fname, d_sname):
    queryCurs.execute('DELETE FROM people WHERE fname=? AND sname =?', (d_fname, d_sname))


def listmenu():
    print' ---------- MENU ---------------'
    print' option 1 = INSERT RECORD'
    print'        2 = SHOW ALL RECORDS'
    print'        3 = DELETE RECORD'
    print'        4 = EMERGENCY MESSAGE TO ALL'
    print'        5 = PROGRAM EXIT'


def option_1():
    print' -------  ADD RECORD  --------'
    fname = raw_input("ENTER FIRST NAME:")
    sname = raw_input("ENTER SURNAME:")
    print' PLEASE ENTER DATE OF BIRTH'
    day = raw_input("ENTER DAY:")
    month = raw_input("ENTER MONTH:")
    year = raw_input("ENTER YEAR:")
    tel = raw_input("ENTER TELEPHONE NUMBER:")
    email = raw_input("ENTER EMAIL ADDRESS:")
    alert = input("SEND ALERTS, (ENTER 1)")
    print fname
    print sname
    print day
    print month
    print year
    print tel
    print email
    print alert
    correct = input('--- ARE THE DETAILS ENTERED CORRECT ? PRESS 1---')
    if correct == 1:
        create_table()
        addperson(fname, sname, day, month, year, tel, email, alert)
        createDb.commit()

    else:
        print ' ---------- DETAILS NOT ADDED -----------------'





def option_2():
    print' -------  SHOW ALL RECORDS  --------'
    if queryCurs.execute('select* from people') != None:
        print '{:<19}'.format('Firstname'),'{:<15}'.format('Surname'),'{:^20}'.format('Date of Birth'), '{:<15}'.format('Tel'), '{:<40}'.format('Email'), '{:<20}'.format('Alert')
        for row in queryCurs:
            print('{row[1]:<20}{row[2]:<20}{row[3]:<5}{row[4]:<5}{row[5]:<5}{row[6]:<15}{row[7]:<40}{row[8]:>8}'.format(row=row))
    else:
        print'------ NO DATA IN DATABASE---------'

def option_3():
    print' -------  DELETE RECORD  --------'
    d_fname = raw_input("Enter first name :")
    d_sname = raw_input("Enter surnasme :")
    queryCurs.execute("SELECT * FROM people WHERE fname= ? AND sname = ?", (d_fname,d_sname))
    result=queryCurs.fetchall()
    if len(result)==0:
        print('Not found')
    else:
        print('Found')
        deleteperson(d_fname, d_sname)
        createDb.commit()

def option_4():
    print' -------  !!! SEND EMERGENCY MESSAGE !!!  --------'
    e_subject = raw_input("please enter subject:")
    e_message = raw_input("please enter message:")

    print e_message
    confirm = input('--- ARE THE DETAILS ENTERED CORRECT ? ENTER PASSCODE---')
    if confirm == 786 :
        checks = 1
        create_table_broadcast()
        adde_message(e_subject,e_message, checks)
        createDb.commit()

    else:
        print ' ---------- !!! INCORRECT PASSCODE !!! -----------------'








def choice():
    option = input("please choose an option :")
    if option == 1:
        option_1()
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    elif option == 5:
        print ('-------------  program closing -------------')
        time.sleep(2)
        sys.exit()
    else:
        print 'option not available'
    return

if __name__ == "__main__":
    while True:
        listmenu()
        choice()
