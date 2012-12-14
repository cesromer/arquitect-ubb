# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from data.forms import ContactForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from data.models import Document, Image, Entry
# Create your views here.


def home(request):
    #i = 0
    #latest = []
    #for d in documentos:
    #    latest.append(d)
    #    i = i + 2

    #i = 0
    #for im in imagenes:
    #    latest.append(im)
    #    i = i + 2

    #tags = Image.entry_tag.all().append(Document.entry_tag.all())
    #tags = Image.entry_tag.most_common()[0:10] for cloud
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()

    vars = {
        'principal': Image.objects.get(is_mainphoto='SI'),
        'ultimas': Image.objects.all()[0:12],
        'pop_tags': pop_tags,
        'pop_docs': pop_docs
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/index.html', vars, contexto)

def search(request):
    if request.method == 'POST':
        res = request.POST
        buscar = res.getlist('buscado')
        res = Image.objects.filter(entry_tag__name__in=buscar)

    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()[0:5]

    vars = {
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'resultados': res
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/search.html', vars, contexto)

def all_tags(request):
    #obj = Image.objects.get(entry_tag=tagg)
    res = Image.entry_tag.all()
    imagenes = Image.objects.all()
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()[0:5]

    vars = {
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'resultados': res,
        'imagenes': imagenes
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/all_tags.html', vars, contexto)

def all_docs(request):
    #obj = Image.objects.get(entry_tag=tagg)
    res = Document.objects.all()
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()[0:5]

    vars = {
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'resultados': res
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/all_docs.html', vars, contexto)

def tagged(request, tagg):
    #obj = Image.objects.get(entry_tag=tagg)
    #obj = Image.objects.filter(entry_tag__name__in=[tagg])[0]
    #res = obj.entry_tag.similar_objects()
    lista = []
    lista.append(tagg)
    res = Image.objects.filter(entry_tag__name__in=lista)
    print(res)
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()[0:5]

    vars = {
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'resultados': res
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/tagged.html', vars, contexto)

def single_doc(request, slug):
    if slug:
        res = Document.objects.get(entry_slug=slug)
        tags = res.entry_tag.all()
    #i = 0
    #latest = []
    #for d in documentos:
    #    latest.append(d)
    #    i = i + 2

    #i = 0
    #for im in imagenes:
    #    latest.append(im)
    #    i = i + 2

    #tags = Image.entry_tag.all().append(Document.entry_tag.all())
    #tags = Image.entry_tag.most_common()[0:10] for cloud
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.objects.all()[0:5]

    vars = {
        'ultimas': Image.objects.all()[0:10],
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'single': res,
        'tags': tags
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/single_doc.html', vars, contexto)

def single_img(request, slug):
    if slug:
        res = Image.objects.get(entry_slug=slug)
        tags = res.entry_tag.all()
    #i = 0
    #latest = []
    #for d in documentos:
    #    latest.append(d)
    #    i = i + 2

    #i = 0
    #for im in imagenes:
    #    latest.append(im)
    #    i = i + 2

    #tags = Image.entry_tag.all().append(Document.entry_tag.all())
    #tags = Image.entry_tag.most_common()[0:10] for cloud
    pop_tags = Image.entry_tag.most_common()
    pop_docs = Document.entry_tag.most_common()[0:5]

    vars = {
        'ultimas': Image.objects.all()[0:10],
        'pop_tags': pop_tags,
        'pop_docs': pop_docs,
        'single': res,
        'tags': tags
    }
    contexto = RequestContext(request)
    return render_to_response('homepage/single_img.html', vars, contexto)

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
