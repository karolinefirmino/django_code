from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
#from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape


# Imaginary function to handle an uploaded file.

#from somewhere import handle_uploaded_file
from django.core.files.storage import FileSystemStorage
from juris.models import *

from .models import  Cadastro, get_mg_string, get_sp_string
from .forms import ProcessoForm


import json 

from django.http import JsonResponse

# Create your views here.
#def load_varas(request):
    #trt = request.GET.get('tribunal')
    #trtVaras = Varas.objects.filter(tribunal_id=tribunal_id).order_by('name')
    #return render(request, 'hr/dropdown_list_varas.html', {'varas': trtVaras})

class MyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'registration/login.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'juris')


class DumpPython(View):
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/autos/">Go back</a>"""
        return HttpResponse(resp)

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        emp = Empresa.objects.all().count()
        arq = Arquivo.objects.all().count()
        tbs = TermoBusca.objects.all().count()
        al = Cadastro.objects.all()
        ctx = {'empresa_count': emp, 'cadastro_list': al, 'arquivos_count': arq, 'busca_count': tbs}
        return render(request, 'juris/cadastro_list.html', ctx)

class EmpresaView(LoginRequiredMixin, View):
    def get(self, request):
        empresa = Empresa.objects.all()
        ctx = {'empresa_list': empresa}
        return render(request, 'juris/empresa_list.html', ctx)

class EmpresaCreate(LoginRequiredMixin, CreateView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class EmpresaUpdate(LoginRequiredMixin, UpdateView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class EmpresaDelete(LoginRequiredMixin, DeleteView):
    model = Empresa
    fields = '__all__'
    success_url = reverse_lazy('juris:all')


class TermoBuscaView(LoginRequiredMixin, View):
    def get(self, request):
        busca = TermoBusca.objects.all()
        ctx = {'busca_list': busca}
        return render(request, 'juris/busca_list.html', ctx)

class TermoBuscaCreate(LoginRequiredMixin, CreateView):
    model = TermoBusca
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class TermoBuscaUpdate(LoginRequiredMixin, UpdateView):
    model = TermoBusca
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class TermoBuscaDelete(LoginRequiredMixin, DeleteView):
    model = TermoBusca
    fields = '__all__'
    success_url = reverse_lazy('juris:all')


class ArquivoView(LoginRequiredMixin, View):
    def get(self, request):
        arquivo = Arquivo.objects.all()
        ctx = {'arquivo_list': arquivo}
        return render(request, 'juris/arquivo_list.html', ctx)

class TermoBuscaCreate(LoginRequiredMixin, CreateView):
    model = Arquivo
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class TermoBuscaUpdate(LoginRequiredMixin, UpdateView):
    model = Arquivo
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class TermoBuscaDelete(LoginRequiredMixin, DeleteView):
    model = Arquivo
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

# We use reverse_lazy() because we are in "constructor attribute" code
# that is run before urls.py is completely loaded]]

class CadastroView(LoginRequiredMixin, View):
    def get(self, request):
        cadastro = Cadastro.objects.all()
        ctx = {'cadastro_list': cadastro}
        return render(request, 'juris/cadastro_list.html', ctx)

class CadastroCreate(CreateView):
    model = Cadastro
    fields = '__all__'
    success_url = reverse_lazy('juris:index')

class CadastroUpdate(LoginRequiredMixin, UpdateView):
    model = Cadastro
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

class CadastroDelete(LoginRequiredMixin, DeleteView):
    model = Cadastro
    fields = '__all__'
    success_url = reverse_lazy('juris:all')

def post_create(request):
    form = ProcessoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commin=False)
        instance.save()
        messages.success(request, "Successfully Created!")
        return HttpResponseRedirect (instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "cadastro_form.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(ProcessoForm, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'Item</a> Saved", extra_tags='html_save')
        return HttpResponseRedirect(instance.get_absolute_url())

        context = {
        "processo" : instance.numero,
        "instance": instance,
        "form": form,
        }

        return render(request, "cadastro_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(ProcessoForm, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted!")
    return redirect("juris:cadastro_list")



#def upload_file(request):
    #if request.method == 'POST':
        #form = Processo(request.POST, request.FILES)
        #if form.is_valid():
            #handle_uploaded_file(request.FILES['docfile'])
            #return HttpResponseRedirect('/success/url/')
    #else:
        #form = Processo()
    #return render(request, 'juris:create', {'form': form})
def index(request):
    context ={}
    cadastro_list = Cadastro.objects.all()
    context['cadastro_list'] = cadastro_list
    return render(request, 'index.html', context)

def Main(request):
    return render(request, 'juris: main.html')

#==========


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'juris/upload.html', context)



def arquivo_list(request):
    arquivos = Cadastro.objects.all()
    return render(request, 'juris/arquivo_list.html', {
        'arquivos': arquivos
        })


#def Upload_Arquivo(request):
        #if request.method == "POST":
            #file = Processo(request.POST, request.FILES)
            #if form.is_valid():
                #form.save()
                #return redirect('arquivo_list')
        #else:
            #file = Processo()
        #return render(request, 'juris/upload_file.html', {
        #'form': form 

       # })

#================= PROJECT TO SELECT =========================


def country_form(request):
    # instead of hardcoding a list you could make a query of a model, as long as
    # it has a __str__() method you should be able to display it.
    tribunal_list = TRIBUNAIS_TRABALHISTAS
    form = FormForm(data_list=tribunal_list)

    return render(request, 'juris/tribunal_list.html', {
        'form': form
    })


#def cadastro_json(request):
    #cadastros = Cadastro.objects.all()
    #data = [cadastro.to_dict_json() for cadastro in cadastros]
    #response={'data':data}
    #return JsonResponse(response)


# References

# https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-editing/#createview

#class OrderListJson(BaseDatatableView):
        # The model we're going to show
    #model = Cadastro

        # define the columns that will be returned
    #columns = ['pesquisa', 'numero', 'poloPassivo', 'tipoProcesso', 'tribunal', 'estado', 'tipoDecisao', 'dataJulgamento', 'vinculoEmpregaticio']


        # define column names that will be used in sorting
        # order is important and should be same as order of columns
        # displayed by datatables. For non sortable columns use empty
        # value like ''
        #order_columns = ['number', 'user', 'state', '', '']

        # set max limit of records returned, this is used to protect our site if someone tries to attack our site
        # and make it return huge amount of data
    #max_display_length = 500

        #def render_column(self, row, column):
            # We want to render user as a custom column
            #if column == 'user':
                # escape HTML for security reasons
                #return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
            #else:
                #return super(OrderListJson, self).render_column(row, column)

    #def filter_queryset(self, qs):
            # use parameters passed in GET request to filter queryset

            # simple example:
        #search = self.request.GET.get('search[value]', None)
        ##if search:
            #qs = qs.filter(number__istartswith=search)

            # more advanced example using extra parameters
        #filter_estado = self.request.GET.get('estado', None)
        #filter_empresa = self.request.GET.get('poloPassivo', None)
        #filter_reconhecimento = self.request.GET.get('vinculoEmpregaticio', None)
        #filter_decisao = self.request.GET.get('tipoDecisao', None)
        #filter_processo = self.request.GET.get('tipoProcesso', None)

            #if filter_customer:
                #customer_parts = filter_customer.split(' ')
               # qs_params = None
                #for part in customer_parts:
                    #q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                    #qs_params = qs_params | q if qs_params else q
                #qs = qs.filter(qs_params)
        #return qs
    #return render('cadastro_list.html')

def cadastroformpage(request):
    context = {}
    #model = Cadastro 
    cadastroform = ProcessoForm()

    context['cadastroform'] = cadastroform

    mg_string = get_mg_string()
    sp_string = get_sp_string()

    json_mg_string = json.dumps(mg_string)
    json_sp_string = json.dumps(sp_string)

    context['json_mg_string'] = json_mg_string
    context['json_sp_string'] = json_sp_string

    return render(request, 'juris/cadastro_form.html', context)



