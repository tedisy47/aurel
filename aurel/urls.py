
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from image_description import views as image_description


url_image = [
	url(r'^$',image_description.index),
    url(r'^upload_image/$',image_description.upload_image),
    url(r'^kamus/$',image_description.kamus),
    url(r'^kamus_insert/$',image_description.kamus_insert),    
    url(r'^kamus_delete/(?P<id>\d+)$', image_description.kamus_delete),
]
urlpatterns = [
    url('admin/', admin.site.urls),
    # url(r'^home/', views.welcome),
    url(r'^$', views.index),
    url(r'^login_', views.welcome, name="login"),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout, name = "logout"),
    url(r'^home/', include(url_image)),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
