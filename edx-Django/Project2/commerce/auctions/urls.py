from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("item/<int:id>", views.item, name="item"),
    path("watchlist/<int:val>", views.watchlist, name="watchlist"),
    path("categories", views.categories, name="categories"),
    path("do_bid/<int:idfb>", views.do_bid, name="do_bid"),
    path("biddings", views.biddings, name="biddings"),
    path("close/<int:cloid>", views.close, name="close")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
