from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from blog.views import recent_article, categories,popular_articles
from blog.forms import ContactForm

form = ContactForm()

context = {'recent_article':recent_article, 'categories':categories, 'popular_articles':popular_articles,"contactform":form}

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html',context)

def cookies_policy(request):
    return render(request, 'core/cookies_policy.html',context)

def disclaimer(request):
    return render(request, 'core/disclaimer.html', context)

def sitemap(request):
    return render(request, 'core/sitemap.html', context)

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        

        if form.is_valid():
            sub = "Blog Contact form"
            name=(form.cleaned_data['name'])
            email=(form.cleaned_data['email'])
            message=(form.cleaned_data['message'])

            details = {'name':name,
                        'email':email,
                        'message': message}
            email_from = settings.EMAIL_HOST_USER
            email_to = settings.DEFAULT_FROM_EMAIL
            html = render_to_string('core/emails/contactform.html',details)
            send_mail(sub,message,email_from,[email_to], html_message=html)
            return redirect('index')

    else:
        form = ContactForm()

    context = {'contactform':form}
    return render(request,'core/contact.html', context)


