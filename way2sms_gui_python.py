from Tkinter import *
import ttk

import smtplib
import webbrowser
import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *

def sendmessage():
    try:
        
        username = account.get()
        number = receiver.get()
        passwd = password.get()
        message = msgbody.get()

        message = "+".join(message.split(' '))


        #logging into the sms site
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'


        #For cookies
        cj= cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        
        #Adding header details
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]

        try:
        	usock =opener.open(url, data)
        except IOError:
        	print "error"

        jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
        	sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
        	print "error"
        print "success"

        
        ttk.Label(mainframe, text="Message sent successfully! Enjoy!!!").grid(column=4,row=9,sticky=W)

    except Exception as e:
        ttk.Label(mainframe, text=str(e)).grid(column=4,row=9,sticky=W)


root = Tk()
root.title("Send a Message through Way2SMS")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

account = StringVar()
password = StringVar()
receiver = StringVar()
msgbody = StringVar()


ttk.Label(mainframe, text="Username",foreground="white",background="magenta").grid(column=0, row=1, sticky=W)
account_entry = ttk.Entry(mainframe, width=40, textvariable=account,foreground="green")
account_entry.grid(column=4, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Password: ",foreground="white",background="magenta").grid(column=0, row=2, sticky=W)
password_entry = ttk.Entry(mainframe, show="*", width=40, textvariable=password,foreground="green")
password_entry.grid(column=4, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Recepient's Number: ",foreground="white",background="magenta").grid(column=0, row=3, sticky=W)
receiver_entry = ttk.Entry(mainframe, width=40, textvariable=receiver,foreground="green")
receiver_entry.grid(column=4, row=3, sticky=(W, E))


ttk.Label(mainframe, text="Message: ",foreground="white",background="magenta").grid(column=0, row=4, sticky=W)
msgbody_entry = ttk.Entry(mainframe, width=40,textvariable=msgbody,foreground="green")
msgbody_entry.grid(column=4, row=4, sticky=(W, E))

ttk.Button(mainframe, text="Send Message",command= sendmessage).grid(column=4,row=8,sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

account_entry.focus()

root.mainloop()
