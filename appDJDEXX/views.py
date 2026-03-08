from django.shortcuts import render
# importar timezone para pegar a data atual
from django.utils import timezone
# importar models do Evento, Presskit, FotoGaleria do models
from .models import Evento, Presskit, FotoGaleria
# importas models da imagemCarrossel, videoDestaque
from .models import ImagemCarrossel, VideoDestaque



# Crie suas views aqui.
#  esta função e responsavel por renderizar a pagina principal
def home(request):
    # pega a data e hora  exata de "agora"
    agora = timezone.now()

    # busque os Eventos que estão no banco e ordena 
    eventos = Evento.objects.filter(
        dia_evento__gte=agora  # filtra: apena eventos futuros ou que acontecem agora
    ).order_by(
        'dia_evento' # ordena: o mais proximo primeiro
    )

    # busca o Presskit mais recente
    # ordena pela data de upload
    presskit_recente = Presskit.objects.order_by('-data_upload').first()

    #esta parte é para carregar imagens no carrosel
    #pega todas as imagens ativas e ordenadas
    slides = ImagemCarrossel.objects.filter(ativo=True).order_by('ordem')
    
    # Lógica do Vídeo (Backend para troca de vídeo)
    # Busca o vídeo marcado como ativo no banco de dados
    video = VideoDestaque.objects.filter(ativo=True).last()

    # cria um( dicionario) para enviar os eventos
    # a chave eventos_contexto sera o nome que vou usar no html
    contexto = {
        'eventos_contexto': eventos,
        'presskit': presskit_recente,
        'slides': slides,
        'video_home': video
    }

    # envie o contexto para o template
    return render(request, 'index.html', contexto)

def galeria(request):
    # Busca TODAS as fotos da galeria no banco, ordenadas
    todas_as_fotos = FotoGaleria.objects.all()

    # Pode adicionar fotos ao contexto aqui
    contexto = { 
        'lista_de_fotos': todas_as_fotos
        }  
    return render(request, 'galeria.html', contexto)


'''
Exemplo: Se você tiver outras páginas, como 'sobre.html':
 
def sobre(request):
     # View para a página "Sobre".
    return render(request, 'sobre.html')
'''
