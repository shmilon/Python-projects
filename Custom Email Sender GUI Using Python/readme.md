# Python Email Sender using Google SMTP Server

![Alt text](https://github.com/shmilon/Python-projects/blob/main/mail_server/Screenshot.jpg "web preview")

## Python Library Reference:

```python
import os
import smtplib as smtp
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, callback, dash_table, dcc, html
```

## Main Configuration --------------------------------

```Python
import smtplib as smtp
email = "test@gmail.com"
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
```
