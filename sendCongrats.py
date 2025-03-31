# import required packages
import pandas as pd
import os
import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import time
from dotenv import load_dotenv
import requests
from win10toast import ToastNotifier

# Se Readme for forklaring af krævede værdier

load_dotenv()
toast = ToastNotifier()

# Gør brug af sendGrid mail klienten 
def sendEmail(to, subject, name):
    message = Mail(
        from_email=os.environ.get('FROM_EMAIL'),
		to_emails=to,
		subject=subject,
		html_content='<strong>Stort tillykke med fødselsdagen! Håber at du får en rigtig god dag <3 </strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))

    toast.show_toast("Email Sent!" , 
					f"{name} was sent e-mail",
					threaded = True, 
					icon_path = None,
					duration = 6)

    while toast.notification_active():
	    time.sleep(0.1)

if __name__=="__main__":
	# læser folks fødselsdag fra excel fil
	dataframe = pd.read_excel("birthdays.xlsx") 
	today = datetime.datetime.now().strftime("%d-%m") 
	yearNow = datetime.datetime.now().strftime("%Y")
	
	# liste til at tilføje data til excel fil
	writeInd = []												 

	for index,item in dataframe.iterrows():
		msg = "Stort tillykke med din fødselsdag " + str(item['Name']) 
		bday = item['Birthday'].strftime("%d-%m")	 

		if (today == bday) and yearNow not in str(item['Year']):
			sendEmail(item['Email'], "Happy Birthday", msg, item['Name']) 
			writeInd.append(index)								 

	for i in writeInd:
		yr = dataframe.loc[i,'Year']
		dataframe.loc[i,'Year'] = str(yr) + ',' + str(yearNow)			 

	dataframe.to_excel('birthdays.xlsx', index = False)
