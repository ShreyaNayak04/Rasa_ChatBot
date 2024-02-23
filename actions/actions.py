from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionSendEmail(Action):
    def name(self) -> Text:
        return "action_email"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Get email details from user input (or slots, if you have a form)
        recipient_email = tracker.latest_message.get('text')
        email_subject = "Your Subject"
        email_message = "Demo of rasa chatbot"

        # Your email and password (or app-specific password)
        sender_email = "shreyunayak24@gmail.com"
        sender_password = "xecy pfii eyiq mztx"

        # Create a MIMEText object for the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = email_subject

        # Attach the message to the email
        msg.attach(MIMEText(email_message, 'plain'))

        # Connect to the SMTP server (for Gmail, use smtp.gmail.com)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create an SMTP session
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())

            # Close the SMTP session
            server.quit()

            # Send a response message to the user
            dispatcher.utter_message("Email sent successfully")
        except Exception as e:
            dispatcher.utter_message("An error occurred while sending the email: {}".format(str(e)))

        return []
