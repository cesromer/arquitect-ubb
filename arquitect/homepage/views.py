# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from data.forms import ContactForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from data.models import Document, Image, Entry
# Create your views here.


def home(request):
    documentos = Document.objects.all()
    imagenes   = Image.objects.all()
    i = 0
    latest = []
    for d in documentos:
        latest.append(d)
        i = i + 2

    i = 0
    for im in imagenes:
        latest.append(im)
        i = i + 2

    #tags = Image.entry_tag.all().append(Document.entry_tag.all())
    tags = Image.entry_tag.most_common()

    vars = {
        'docs': latest[0:12],
        'imgs': imagenes,
        'cloud': tags
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/index.html', vars, contexto)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    enviado = False
    contexto = RequestContext(request)
    #seteado de campos del formulario
    email = ''
    titulo = ''
    cuerpo = ''
    if request.method == 'POST':
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            cuerpo = formulario.cleaned_data['Cuerpo']

            #envio de msj vía GMAIL
            toAdmin = 'cesromer@gmail.com'  # admin email
            htmlContent = 'Información recibida:<br><br> \
                <b>Título:</b><br>%s<br><b>Mensaje:</b><br>%s' %(titulo, cuerpo)

            msg = EmailMultiAlternatives('Correo Contacto', htmlContent,
                                         'from@server.com', toAdmin, '')
            msg.atach_alternative(htmlContent, 'text/html')
            msg.send() #Enviamos el mail
    else:
        formulario = ContactForm()

    vars = {
        'form': formulario,
        'email': email,
        'titulo': titulo,
        'cuerpo': cuerpo,
        'enviado': enviado
    }
    return render_to_response('homepage/contacto.html', vars, contexto)
