from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import date
from sys import argv
from constants import Constants


class EmailSender:
    def send(self, content):
        message = Mail(
            from_email=Constants.FROM.value,
            to_emails=Constants.TO.value,
            subject=f'Report for {date.today().strftime(Constants.DATE_FORMAT.value)}',
            html_content=content)
        try:
            sg = SendGridAPIClient(argv[2])
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
