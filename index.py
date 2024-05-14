import os
import resend

resend.api_key = os.environ["RESEND_API_KEY"]

params: resend.Emails.SendParams = {
    "sender": "Acme <onboarding@resend.dev>",
    "to": ["delivered@resend.dev"],
    "subject": "Hello world",
    "html": "<strong>It works!</strong>"
}

email: resend.Email = resend.Emails.send(params)
print(email)
