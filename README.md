This script tracks and send greetings to emails/people that you have defined in an excel file. 

It uses the sendGrip mail klient to send the emails. 
If only the basic types of validation is used for the email in your email klient, the mails you send, might end up in the spam folder of the recipients. 
If you use another mail klient, follow their connection requirements, as some uses more than just an api key. 

The following is required:
env variables:
  FROM_EMAIL
  <MAIL_CLIENT>_API_KEY
An excel file with the following headers
NAME, EMAIL, BIRTHDAY, YEAR
