from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.views.generic.edit import (
    CreateView, UpdateView
)

from quiz.models import QOTD, Result
from about.models import About, Team, Advisors

from django.conf import settings

from .models import Student, User
from .forms import ContactUsForm, CustomUserCreationForm
from .tokens import account_activation_token


def signupview(request):
    """ create new users and inactive them"""
    if request.user.is_authenticated:
        return redirect('users:index')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                """ inactive the user and save it. Send email verification """
                email_address = form.cleaned_data['email']

                new_user = form.save(commit=False)
                new_user.is_active=False
                new_user.save()

                # send email to verify it
                current_site = get_current_site(request)

                email_body = {
                    'user': new_user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                    'token': account_activation_token.make_token(new_user),
                }

                link = reverse('users:activate', kwargs={
                               'uidb64': email_body['uid'], 'token': email_body['token']})
                email_subject = 'Activate your account'
                activate_url = current_site.domain[:-1]+link
                email_body = f'Hi, {new_user.username} Please the link below to activate your account \n{activate_url}'
                

                try:
                    send_mail(
                        email_subject,
                        email_body,
                        settings.EMAIL_HOST_USER,
                        [email_address],
                        fail_silently=False
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                messages.success(request, f'Your account has been created! You may login now!')
                return redirect('login')
        else:
            form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form, 'title':'reqister here'})


def verify_registered_email(request, uidb64, token):
    """ 
    verify email of registered user, but
    still make the user in_active.    
    """
    if request.method == "GET":
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True  # because admin should make the user active manually
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass
    return redirect('login')


def index(request):
    if request.method == 'POST':
        question = QOTD.objects.last()
        user = request.user.id

       
        if question.answer == request.POST.get(question.qotd_statement):
            context={
                'qotd': question,
                'answer': request.POST.get(question.qotd_statement),
                'explanation': question.explanation,
                'correct': 'Correct Answer'
            }

        else:
            context={
                'qotd': question,
                'answer': request.POST.get(question.qotd_statement),
                'explanation': question.explanation,
                'correct': 'Wrong Answer'
            }
        return render(request,'users/index.html', context)

    else:
        template_name = 'users/index.html'
        qotd = QOTD.objects.last()
        student = Student.objects.all()
    
        return render(request, template_name,{'qotd':qotd, 'students':student})


# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            # send email
            response = {}
            response["full_name"] = form.cleaned_data["full_name"]
            response["email"] = form.cleaned_data["email"]
            response["phone_number"] = form.cleaned_data["phone_number"]
            response["message"] = form.cleaned_data["message"]

            try:
                send_mail(
                    'EDUMLT --just received a new message', # subject
                    # email message/body 
                    "A new form has been recorded with following details:"+"\n"+ "\n"+
                    "Full Name: {}".format(response['full_name'])+ "\n" + 
                    "Sender's Email: {}".format(response['email']) + "\n" +
                    "Senders Phone: {}".format(response['phone_number']) + "\n" +
                    "Message: {}".format(response['message']) + "\n" 
                    ,
                    settings.EMAIL_HOST_USER,  # sender
                    ['mcqmlt@gmail.com'], # receiver
                    fail_silently=False,
                )
                messages.success(request, ("Response has been recorded thank you."))
                return redirect("users:index")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        
        else:
            messages.error(request, ("Form submission was failed, please check your inputs."))
            return render(request, 'users/contact.html')

    else:
        form = ContactUsForm()
    return render(request, 'users/contact.html', {'form': form})


def history(request):
    template_name = 'users/history.html'

    user = request.user
    results = Result.objects.filter(user=user.id)

    return render(request, template_name, {'results':results})

def about(request):
    template_name = 'users/about.html'
    about = About.objects.last()
    teams = Team.objects.all()
    advisors = Advisors.objects.all().order_by('-advisor_index')
    return render(request, template_name, {'about': about, 'teams': teams, 'advisors': advisors})


def custom_page_not_found_view(request, exception):
    """ custom 404 page"""
    return render(request, "errors/404.html", {})


def custom_error_view(request):
    """ custom 500 page """
    return render(request, "errors/404.html", {})
     