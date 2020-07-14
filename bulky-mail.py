import smtplib

def send_email(subject, msg):

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('hetymgoofy@gmail.com', 'Goofy@123')
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail('hetymgoofy@gmail.com', 'ssharma88823@gmail.com', message)
        server.quit()
        print("Success: Email sent!")

    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)
