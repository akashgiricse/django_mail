from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from .forms import mailForm


def sendMail(request):
    form = mailForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        send_mail(subject, message, 'from@example.com', ['to@example.com'], fail_silently=False)

        return redirect("mail")

    return render(request, "mail.html", {'form': form})
