"""
URL configuration for boardapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin  # 管理者用のページを作成するためのモジュール
from django.urls import include, path
from . import settings
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('', include('comments.urls')),
    #path('admin/', admin.site.urls),   # 管理者用のページを作成するためのモジュール
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), # staticファイルを配信するための設定
    re_path(r'^files/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}), # mediaファイルを配信するための設定
]


# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns.append(path("", include(debug_toolbar.urls)))