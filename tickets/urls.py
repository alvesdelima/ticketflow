from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

router = DefaultRouter()
router.register(r'tickets', TicketViewSet)  # Registra a rota /tickets/

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas do router
]
