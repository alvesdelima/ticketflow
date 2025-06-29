from django.contrib import admin
from .models import User, Ticket, Status, Comentario

# Exibindo os modelos no admin
admin.site.register(User)
admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Comentario)

