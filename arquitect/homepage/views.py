# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from data.forms import ContactForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from data.models import Document, Image, Entry
# Create your views here.

#function called when the index of homepage is opened
def home(request):
    # get the tags from the Image Model filtered the most common images
    # and put this in "pop_tags"
    pop_tags = Image.entry_tag.most_common()
    # get All the Documents as Object's
    # and put this in "pop_docs"
    pop_docs = Document.objects.all()[0:5]

    #if is possible get the main photo
    try:
        main_photo = Image.objects.get(is_mainphoto='SI')
    except Image.DoesNotExist:
        main_photo = ''

    #set the content of the vars for the context in this page
    vars = {
        # Main photo(large) in the homepage.
        'principal': main_photo,
        # Latest 12 Images as Objects (6 for row)
        'ultimas': Image.objects.all()[0:12],
        # The Most Popular tags
        'pop_tags': pop_tags,
        # The Most Popular Docs
        'pop_docs': pop_docs
    }
    # Create the instace for this context page
    contexto = RequestContext(request)
    # Render the page in the homepage/index.html with the vars and context
    # previously set's
    return render_to_response('homepage/index.html', vars, contexto)

#Method called when the user make a search in the site
def search(request):
    # get the tags from the Image Model filtered the most common images
    # and put this in "pop_tags"
    pop_tags = Image.entry_tag.most_common()
    # get All the Documents as Object's
    # and put this in "pop_docs"
    pop_docs = Document.objects.all()[0:5]

    #Search is sended by the POST method, this are "ever"(not really) true...
    if request.method == 'POST':
        res     = request.POST
        buscar  = res.getlist('buscado')
        res     = Image.objects.filter(entry_tag__name__in=buscar)

    vars = {
        # The Most Popular tags
        'pop_tags': pop_tags,
        # The Most Popular Docs
        'pop_docs': pop_docs,
        #the search results if this generate this
        'resultados': res
    }
    # Create the instace for this context page
    contexto = RequestContext(request)
    # Render the page in the homepage/index.html with the vars and context
    # previously set's
    return render_to_response('homepage/search.html', vars, contexto)

#method that get the all Tags in the DB and render this in the website
def all_tags(request):

    #get all the tags from the DB and put this in the "tagsContainer" var
    tagsContainer   = Image.entry_tag.all()

    #get all the images like a objest (all the fields) 
    images        = Image.objects.all()

    # get the tags from the Image Model filtered the most common images
    # and put this in "pop_tags"
    pop_tags = Image.entry_tag.most_common()
    # get All the Documents as Object's
    # and put this in "pop_docs"
    pop_docs = Document.objects.all()[0:5]

    vars = {
        # The Most Popular tags
        'pop_tags': pop_tags,
        # The Most Popular Docs
        'pop_docs': pop_docs,
        #Tags from the DB associated to the images
        'resultados': tagsContainer,
        #Images like a object (all the fields)
        'imagenes': images
    }
    # Create the instace for this context page
    contexto = RequestContext(request)
    # Render the page in the homepage/index.html with the vars and context
    # previously set's
    return render_to_response('homepage/all_tags.html', vars, contexto)

#method that get the all Docs in the DB and render this in the website
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
    pop_docs = Document.objects.all()[0:5]

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
    email   = ''
    titulo  = ''
    cuerpo  = ''
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
