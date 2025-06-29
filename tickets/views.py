from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()  # Pega todos os tickets do banco
    serializer_class = TicketSerializer  # Usa o serializer que você criou

