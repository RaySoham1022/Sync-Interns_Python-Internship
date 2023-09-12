from django.core.mail import send_mail
from OTPVerification.settings import EMAIL_HOST_USER


def send_forget_password_mail(email, token):
    subject = "OTP to Reset Password at InterviewMitra"
    message = f"Your one time password (OTP) is -- {token}. Use it to reset your password."
    email_from = EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
