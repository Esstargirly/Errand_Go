import resend
import os
import random

resend.api_key = os.getenv("RESEND_API_KEY")

def generate_otp():
    """Generate a random 6-digit OTP code"""
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp_code):
    """Send OTP verification email to user"""
    try:
        resend.Emails.send({
            "from": "ErrandGo <onboarding@resend.dev>",
            "to": [email],
            "subject": "Verify your ErrandGo account",
            "text": f"""
Hi there,

Welcome to ErrandGo!

Your verification code is:

        {otp_code}

This code expires in 15 minutes.

If you did not create an ErrandGo account, please ignore this email.

The ErrandGo Team
            """
        })
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False