from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .helpers import send_forget_password_mail
import math, random



def index(request):

    global otp
    if request.method == "POST":
        global token
        global user_obj
        otp_sent = False
        otp_matched = False
        respasswd = {
            "otp_sent": otp_sent,
            "otp_matched": otp_matched,
        }
        if "username_submit" in request.POST:
            username = request.POST.get("email")
            digits = [i for i in range(0, 10)]
            otp = ""

            for i in range(6):
                index = math.floor(random.random() * 10)
                otp += str(digits[index])

            token = otp

            ResPasToken(CurrentUser = username, PassToken = token).save()

            resobject = ResPasToken.objects.get(CurrentUser= username)
            send_forget_password_mail(resobject.CurrentUser, token)

            otp_sent = True
            global userplace
            userplace = username
            respasswd.update(
                {"otp_sent": otp_sent, "otp_matched": otp_matched})
            return render(request, "index.html", respasswd)

        if "otp_submit" in request.POST:
            pasobject = ResPasToken.objects.last()
            otp_entered = int(request.POST.get("otp"))
            if int(otp_entered) == int(pasobject.PassToken) :
                otp_sent = False
                otp_matched = True
                respasswd.update(
                    {
                        "otp_sent": otp_sent,
                        "otp_matched": otp_matched,
                    }
                )
                pasobject.delete()
                return render(request, "index.html", respasswd)
            else:
                otp_sent = True
                otp_matched = False
                messages.info(request, "Invalid OTP")
                respasswd.update(
                    {"otp_sent": otp_sent, "otp_matched": otp_matched})
                return render(request, "index.html", respasswd)

    else:
        otp_sent = False
        otp_matched = False
        respasswd = {
            "otp_sent": otp_sent,
            "otp_matched": otp_matched,
        }
        return render(request, "index.html", respasswd)


