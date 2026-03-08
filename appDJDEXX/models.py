from django.db import models

# Crie as models aqui.

class ImagemCarrossel(models.Model):
    titulo = models.CharField(max_length=100, help_text="Titulo para identificar (opicional) ")
    imagem = models.ImageField(upload_to='carrossel/', verbose_name="Imagem do Slide")
    ativo = models.BooleanField(default=True, help_text="se for marcado, a imagem aparerá no site")
    ordem = models.IntegerField(default=0, help_text="Menor número aparece primeiro")

    class Meta:
        verbose_name = "Imagem do Carrossel"
        verbose_name_plural = "Imagens do carrossel"
        ordering = ['ordem'] # ordena automaticamente pela ordem definida

    def __str__(self):
        return self.titulo
 
class Presskit(models.Model):
    titulo = models.CharField(max_length=100, default="Logo Oficial")
    
    # Este é o campo principal:
    # 'upload_to=' define a subpasta dentro de /media/ onde o arquivo será salvo
    arquivo = models.FileField(upload_to='logos/', verbose_name="Arquivo com Logos")
    
    # 'auto_now=True' significa que este campo é atualizado automaticamente
    # para a data e hora de "agora" toda vez que o objeto é salvo (ou seja, upload).
    data_upload = models.DateTimeField(auto_now=True, verbose_name="Data do Upload")

    # Isso é o que aparece no painel de admin quando você lista os presskits
    def __str__(self):
        return f"{self.titulo} (atualizado em {self.data_upload.strftime('%d/%m/%Y')})"

    # Configurações para o painel de admin (nomes em português)
    class Meta:
        verbose_name = "Download Logo"
        verbose_name_plural = "Downloads Logos"
        # Isso garante que no admin, o mais recente apareça no topo
        ordering = ['-data_upload']

class Evento(models.Model):
    # campos conforme a inf-evento h4
    # dia do evento
    dia_evento = models.CharField(max_length=100, verbose_name='Dia do evento')
    # nome do club onde vai ser o evento
    nome_club = models.CharField(max_length=200, verbose_name='Nome do Club')
    # endereço do evento
    end_evento = models.CharField(
        max_length=255, verbose_name='Local do evento')

    # Opcional, mas útil: Link para os ingressos
    link_ingresso = models.URLField(
        max_length=300, blank=True, null=True, verbose_name='link do ingreço')

    def __str__(self):
        # isso ajuda a identificar o evento no painel de admin
        return f"{self.dia_evento} - {self.nome_club}"

class FotoGaleria(models.Model):
    # Um título/descrição opcional para a foto (pode deixar em branco no admin)
    titulo = models.CharField(max_length=150, blank=True, null=True, verbose_name="Título da Foto")
    
    # O campo de imagem. Pillow é necessário.
    # As fotos serão salvas em 'media/galeria/'
    foto = models.ImageField(upload_to='galeria/', verbose_name="Arquivo de Foto")
    
    data_upload = models.DateTimeField(auto_now_add=True, verbose_name="Data do Upload")

    def __str__(self):
        if self.titulo:
            return self.titulo
        # Se não tiver título, retorna o nome do arquivo
        return f"Foto ({self.foto.name})"

    class Meta:
        verbose_name = "Foto da Galeria"
        verbose_name_plural = "Fotos da Galeria"
        # Ordena pelas mais novas primeiro
        ordering = ['-data_upload']

class VideoDestaque(models.Model):
    # Um título para você identificar o vídeo no painel de admin
    titulo = models.CharField(max_length=100, default="Vídeo de Fundo")
    
    # O campo que permite fazer o upload do arquivo .mp4
    # Os vídeos serão salvos em uma subpasta chamada /media/videos/
    arquivo_video = models.FileField(upload_to='videos/', verbose_name="Arquivo de Vídeo")
    
    # Um campo para você marcar qual vídeo deve aparecer na Home
    ativo = models.BooleanField(default=True, verbose_name="Está ativo?")
    
    # Opcional: data de upload para controle interno
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Facilita a visualização no painel administrativo
        return self.titulo

    class Meta:
        # Define os nomes que aparecem no menu do Django Admin
        verbose_name = "Vídeo de Destaque"
        verbose_name_plural = "Vídeos de Destaque"

# sempre que mudar alguma coisa no models
# execute o comando manage.py makemigrations
# e o comando manage.py migrate