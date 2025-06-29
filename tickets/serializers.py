# tickets/serializers.py
from rest_framework import serializers
from .models import User, Ticket, Status, Comentario


# 👤 Serializer para o usuário
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tipo']


# 🏷️ Serializer para o status
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'nome']


# 🎫 Serializer para o ticket
class TicketSerializer(serializers.ModelSerializer):
    cliente = UserSerializer(read_only=True)
    tecnico = UserSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            'id',
            'titulo',
            'descricao',
            'prioridade',
            'status',
            'cliente',
            'tecnico',
            'criado_em',
            'atualizado_em',
        ]


# 💬 Serializer para comentários
class ComentarioSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'ticket', 'autor', 'texto', 'data_criacao']
