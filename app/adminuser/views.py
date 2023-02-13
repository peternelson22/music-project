from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AdminUser
from .models import MessageAdmin


def admin_user(request):
    admin = AdminUser.objects.all().first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        msg = MessageAdmin.objects.create(
            admin=admin, name=name, email=email, subject=subject, body=body)
        messages.success(request, 'Message sent successfully')
        return redirect('adminuser')

    return render(request, 'admin/contact.html', {'admin': admin})
