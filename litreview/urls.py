"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from app_accounts import views as v_acc
from app_reviews import views as v_rev
from app_subs import views as v_subs

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True),
        name='login',
    ),
    path('register/', v_acc.register, name='register'),
    path('logout/', v_acc.disconnect, name='logout'),

    path('subs/', v_subs.home, name='subs'),
    path('unsubscribe/<int:id>', v_subs.unsubscribe),

    path('posts/', v_rev.posts, name='posts'),
    
    path('ticket/create/', v_rev.ticket_create, name='create_ticket'),
    path('ticket/modify/<int:id>', v_rev.ticket_modify, name='modify_ticket'),
    path('ticket/delete/<int:id>', v_rev.ticket_delete),

    path('review/create/', v_rev.review_create, name='create_review'),
    path('review/create/<int:id>', v_rev.review_create_reply),
    path('review/modify/<int:id>', v_rev.review_modify, name='modify_review'),
    path('review/delete/<int:id>', v_rev.review_delete),

    path('', v_rev.feed, name="feed"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
