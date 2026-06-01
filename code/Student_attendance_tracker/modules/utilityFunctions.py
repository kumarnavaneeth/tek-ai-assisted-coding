
import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from config.settings import (
    SENDER_EMAIL,
    SENDER_PASSWORD
)


# MAIL TO STUDENTS
def mailstu(li, msg):

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(SENDER_EMAIL, SENDER_PASSWORD)

    for i in range(len(li)):

        to_id = li[i]

        message = MIMEMultipart()

        message['Subject'] = 'Attendance Report'

        message['From'] = SENDER_EMAIL

        message['To'] = to_id

        message.attach(
            MIMEText(msg, 'plain')
        )

        content = message.as_string()

        s.sendmail(
            SENDER_EMAIL,
            to_id,
            content
        )

    s.quit()

    print("Mail sent to students")


# MAIL TO STAFF
def mailstaff(to_id, msg):

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(SENDER_EMAIL, SENDER_PASSWORD)

    message = MIMEMultipart()

    message['Subject'] = 'Attendance Shortage Report'

    message['From'] = SENDER_EMAIL

    message['To'] = to_id

    message.attach(
        MIMEText(msg, 'plain')
    )

    content = message.as_string()

    s.sendmail(
        SENDER_EMAIL,
        to_id,
        content
    )

    s.quit()

    print("Mail sent to staff")