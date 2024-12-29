import smtplib

sender_email = input("Enter your email: ")
receiver_email = input("Enter receiver email: ")
subject = input("Enter subject: ")
body = input("Enter email body: ")
password = input("Enter your email password: ")

message = f"Subject: {subject}\n\n{body}"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

print("Email sent successfully!")
