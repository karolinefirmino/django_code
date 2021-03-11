from django.contrib import admin
from .models import *
from .models import Cadastro
# Register your models here.
admin.site.register(Cadastro)
admin.site.register(Empresa)
admin.site.register(Tribunal)
admin.site.register(Varas)
#@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
	list_display = ('numero', 'tipoProcesso', 'poloPassivo', 'tribunal', 'vinculoEmpregaticio')
	search_fields = ('numero', 'tipoProcesso', 'poloPassivo', 'tribunal', 'vinculoEmpregaticio')
	list_filter = ('numero', 'tipoProcesso', 'poloPassivo', 'tribunal', 'vinculoEmpregaticio')