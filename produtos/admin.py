from django.contrib import admin
from produtos.models import Produtos

# Register your models here.
class ListaProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'estoque', 'marca', 'descricao')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 10

admin.site.register(Produtos, ListaProdutosAdmin)