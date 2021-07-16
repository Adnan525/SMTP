import smtplib


def sendMail(receiver, fromHeader, subject, body):
    msg = f'From: {fromHeader}\nSubject: {subject}\n\n{body}'
    smtp.sendmail(email, receiver, msg)

#contact manger
gmailSmtpserver = "smtp.gmail.com"
with smtplib.SMTP(gmailSmtpserver, 587) as smtp:
    smtp.ehlo()
    #encrypt
    smtp.starttls()
    smtp.ehlo()

    email = "emailAddress"
    password = "Password"

    smtp.login(email, password)

    rec = "adnaan525@gmail.com"
    sendMail(rec, "", "", "")