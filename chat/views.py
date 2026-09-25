from django.views.generic import TemplateView
# safestring -> String segura
from django.utils.safestring import mark_safe  # mark_safe -> remove qualquer insegurança nas strings
import json


# OBS: as salas serão criadas dinamicamente e corre o risco de certo usuários, criarem nome de salas
# que não são seguras. Então o mark_safe irá balizar e tirar inseguranças contidas na string.

class IndexView(TemplateView):
    template_name = "index.html"


class SalaView(TemplateView):
    template_name = "sala.html"

    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        # Pega um arquivo de texto comum e transformará em json e o salvará
        context["nome_sala_json"] = mark_safe(
            json.dumps(self.kwargs["nome_sala"])
        )
        return context
