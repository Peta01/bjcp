from django.shortcuts import render, get_object_or_404
from .models import BeerStyle

from django.shortcuts import render, HttpResponse
from django.template.loader import get_template

def beer_style_list(request):
    # Načtení všech záznamů z databáze
    styles = BeerStyle.objects.all()
    return render(request, 'beer_styles/beer_style_list.html', {'styles': styles})

def beer_style_detail(request, pk):
    style = get_object_or_404(BeerStyle, pk=pk)
    
    # Získání ID prvního a posledního záznamu
    first_style = BeerStyle.objects.first()
    last_style = BeerStyle.objects.last()
    
    # Získání předchozího a následujícího záznamu
    previous_style = BeerStyle.objects.filter(pk__lt=pk).order_by('-pk').first()
    next_style = BeerStyle.objects.filter(pk__gt=pk).order_by('pk').first()

    return render(request, 'beer_styles/beer_style_detail.html', {
        'style': style,
        'first_style': first_style,
        'last_style': last_style,
        'previous_style': previous_style,
        'next_style': next_style
    })