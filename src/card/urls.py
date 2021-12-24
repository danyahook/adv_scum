from django.urls import path

from card.views import card_view

app_name = "card"

urlpatterns = [
    path('', card_view.card_list, name="card_list"),
]
