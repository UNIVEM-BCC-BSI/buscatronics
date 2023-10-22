from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from website.models import Produto, Plataforma, Loja


class IndexView(TemplateView):
    template_name = "website/index.html"

    def get(self, request, id=None):
        categories = Plataforma.objects.order_by("id")
        stores = Loja.objects.order_by("nome")
        filter = request.GET.get("q", "") # get q or empty string
        if filter != "":
            title = f"Resultados para '{filter}'"
            products = Produto.objects.filter(nome__icontains=filter).order_by("precoTotal")
        elif id is None:
            title = "Todos os produtos"
            products = Produto.objects.order_by("precoTotal")
        else:
            title = next(c.nome for c in categories if c.id == id)
            products = Produto.objects.filter(plataforma_id=id).order_by("precoTotal")
        
        context = {
            "filter": filter,
            "categories": [{"id": c.id, "nome": c.nome} for c in categories],
            "title": title,
            "products": [{
                "id": p.id,
                "nome": p.nome,
                "precoTotal": p.precoTotal,
                "precoDesconto": p.precoDesconto,
                "loja": p.loja,
                "midia": p.midia,
                "link": p.link
            } for p in products]
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))