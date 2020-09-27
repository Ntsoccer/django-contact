from django.shortcuts import render,resolve_url 
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages


class Index(TemplateView):
    template_name='contactapp/index.html'

class ContactFormView(FormView):
    template_name='contactapp/contact_form.html'
    form_class=ContactForm
    # success_url=reverse_lazy('contactapp:index')

    def form_valid(self,form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        messages.info(self.request,'お問い合わせは正常に送信されました。')
        return resolve_url('contactapp:index')

