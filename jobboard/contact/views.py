from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.views.generic.base import View
from .forms import ContactForm


class ContactView(View):
    """
        Контроллер для вывода страницы с формой обратной связи на сайт,
        и обработка данной формы
    """
    def get(self, request):
        context = {}
        context['form'] = ContactForm()
        return render(request, 'contact/contact.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 'Сообщение успешно отправлено')
            return redirect(reverse("contact:contact"))
