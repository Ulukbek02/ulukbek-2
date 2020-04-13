from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import ContactForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError

class ContactView(View):
    '''Отправка формы'''
    def get(self, request):
        form = ContactForm()
        return render(request, 'home.html', context={'form': form})
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            number = form.cleaned_data['number']
            description = form.cleaned_data['description']

            recipients = ['jenishov_ulushka@24mail.ru']
            try:
                send_mail(name, description, 'jenishov_ulushka@24mail.ru', recipients)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')
			#Переходим на другую страницу, если сообщение отправлено
            return render(request, 'home.html')
        else:
		#Заполняем форму
            form = ContactForm()
	          #Отправляем форму на страницу
            return render(request, 'home.html', {'form': form})
