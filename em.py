import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='deepikashakthi123@gmail.com'
receiver='deepthianivala@gmail.com'
msg="hii"
s.login(sender,'deepika123')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()