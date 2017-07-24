def SendEmail(recipient, subject, body):
    import smtplib

    user = "noreply@taylormadetimber.co.uk"

    gmail_user = "no.reply"
    gmail_pwd = "WhatALotOfS4wdust!"
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("mail.taylormadetimber.co.uk", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
