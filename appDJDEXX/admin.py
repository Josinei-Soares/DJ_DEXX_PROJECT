from django.contrib import admin
# importar o models Evento, Presskit, FotoGaleria da pasta models
from .models import Evento, Presskit, FotoGaleria
# importa o models ImagemCarrossel, VideoDestaque
from .models import ImagemCarrossel, VideoDestaque

# Registrar a class ImagemCarrossel aqui
@admin.register(ImagemCarrossel)
class ImagemCarrosselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'ordem') # O que aparece na lista
    list_editable = ('ativo', 'ordem')          # Permite editar rápido sem abrir o item
    ordering = ('ordem',)                       # Ordenação padrão no admin

# Registrar a class Presskit aqui
@admin.register(Presskit)
class PresskitAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'arquivo', 'data_upload')

# Registrar a class Evento aqui.
admin.site.register(Evento)


# Registrar a class Galeria aqui
@admin.register(FotoGaleria)
class FotoGaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'foto', 'data_upload')
# adiciona uma filtro de data na lateral do admin
list_filter =('data_upload',)

# Registra a class VideoDestaque
#admin.site.register(VideoDestaque)

@admin.register(VideoDestaque)
class VideoDestaqueAdmin(admin.ModelAdmin):
    # Exibe colunas específicas na listagem do admin
    list_display = ('titulo', 'ativo', 'data_upload') 
    
    # Permite clicar no "Ativo" direto na lista para ligar/desligar
    list_editable = ('ativo',) 
    
    # Adiciona um filtro lateral por data ou status
    list_filter = ('ativo', 'data_upload')

