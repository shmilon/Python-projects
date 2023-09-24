import smtplib as smtp

email = "email@gmail.com"

def sendMail(receiver,sub,body):
    try:
        server = smtp.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email,"your app password")

        msg = "Subject: {}\n\n{}".format(sub, body)

        server.sendmail(email,receiver,msg)
        server.quit()
        return "sent successfully"  #return the result without brackets
    except Exception as e:
        return f"Error: {str(e)}"
    

