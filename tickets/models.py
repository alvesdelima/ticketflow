# tickets/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Tipos de usuário
TIPOS_USUARIO = (
    ('cliente', 'Cliente'),
    ('tecnico', 'Técnico'),
)

# Prioridades de ticket
PRIORIDADES = (
    ('baixa', 'Baixa'),
    ('media', 'Média'),
    ('alta', 'Alta'),
)


# 👤 Usuário customizado
class User(AbstractUser):
    tipo = models.CharField(max_length=10, choices=TIPOS_USUARIO)

    def __str__(self):
        return f"{self.username} ({self.tipo})"


# 📌 Status de um ticket (Ex: Novo, Em andamento, Resolvido)
class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


# 🎫 Ticket principal
class Ticket(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default='media')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets_criados')
    tecnico = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_atendidos')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"#{self.id} - {self.titulo}"


# 💬 Comentários feitos em tickets
class Comentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} em #{self.ticket.id}"
