from django.shortcuts import get_object_or_404
from django.shortcuts import render


from card.models.card_model import Card


def card_list(request):
    cards = Card.objects.all()
    return render(request, 'card/card_list.html', {'cards': cards})
