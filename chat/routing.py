from django.urls import re_path  # Cria caminhos com expressões regulares

# Rota específica do channers
from .consumers import ChatConsumer

# ws -> é o websocket, re-path irá criar uma rota de comunicação da aplicação com o websocket
# ao ser criada toda vez uma nova sala

# ChatConsumer -> Faz a ligação (ponte) entre o navegador e a aplicação

# (?P<nome_sala>\w+/$) -> É uma expressão regular que define o padrão, ao ser criada uma nova sala
websocket_urlpatterns = {
    re_path(r"ws/chat/(?P<nome_sala>\w+/$)", ChatConsumer),
}
