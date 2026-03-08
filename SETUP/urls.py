
from django.contrib import admin
from django.urls import path
# importa a view que criei
from appDJDEXX import views
# importação de config do settings
from django.conf import settings
from django.conf.urls.static import static
# importação de config do logout admin
from django.contrib.auth import views as auth_views



urlpatterns = [
    # Ela "captura" o pedido de logout do admin e o redireciona para a home ('/')
    path('admin/logout/', auth_views.LogoutView.as_view(next_page='/'), name='admin_logout_override'),

    path('admin/', admin.site.urls),
    # quando alquem acessar o raiz (""),
    # use a função 'home' que est em views.py
    path('',views.home, name='home'), 

    # quando a acessar a galeria /galeria/ use a view  galeria
    path('galeria/', views.galeria, name='galeria'),

    # caminho para acessar o video
    path('', views.home, name='home'),
]

# Presskit
# Isso permite que o Django sirva os arquivos de upload (media)
# no modo de desenvolvimento (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Serve arquivos estáticos (css, js, imagens do tema) - Opcional mas recomendado
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)