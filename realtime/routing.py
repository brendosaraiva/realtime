# routing -> configura as rotas do websocket para a aplicação, fazendo com que ocorra
# a comunicação realtime.

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from chat.routing import websocket_urlpatterns

# o a constante presente no arquivo de settings (ASGI_APPLICATION) irá chamar a variável application
# aplicação aqui, para deixar configurada as rotas do websocket
application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})


