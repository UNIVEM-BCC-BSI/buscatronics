from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from website.models import Produto, Plataforma, Loja

class DetailView(TemplateView):
    template_name = "website/detalhes.html"

    def get(self, request, id, nome):
        stores = Loja.objects.order_by("id")
        # pegar as lojas para adicionar nas categorias

        # produtos serão mostrados em várias repartições por loja (como se fossem várias páginas iniciais)

        # barra de pesquisa... acho que volta para a página inicial e o botão "home" também

        # o texto de preço muda conforme a loja, se não houver loja selecionada, mostra o menor preço, se tiver,
        # mostra o menor preço daquela loja (acho que terão vários anúncios para o mesmo jogo)
        