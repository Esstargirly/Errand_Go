import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os
import random

def generate_otp():
    """Generate a random 6-digit OTP code"""
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp_code):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = os.getenv("BREVO_API_KEY")

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": email}],
        sender={"name": "ErrandGo", "email": "estherappolos51@gmail.com"},
        subject="Verify your ErrandGo account",
        text_content=f"""
Hi there,

Welcome to ErrandGo!

Your verification code is:

        {otp_code}

This code expires in 15 minutes.

If you did not create an ErrandGo account, please ignore this email.

The ErrandGo Team
        """
    )

    try:
        api_instance.send_transac_email(send_smtp_email)
        return True
    except ApiException as e:
        print(f"Email sending failed: {e}")
        return False
