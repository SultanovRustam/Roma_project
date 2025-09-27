from django.shortcuts import render, get_object_or_404
from .models import Era, EraPage

def era_detail(request, slug):
    era = get_object_or_404(Era, slug=slug)
    era_page = get_object_or_404(EraPage, era=era)
    return render(request, 'eras/era_detail.html', {
        'era': era,
        'era_page': era_page
    })

def about(request):
    team_members = [
        {'name': 'Рома', 'role': 'Книги-свитки, Иван Фёдоров'},
        {'name': 'Дима', 'role': 'Пергамент, Рукописные книги'},
        {'name': 'Арсений', 'role': 'Восковые таблички, Берестяные грамоты'},
        {'name': 'Папа', 'role': 'Технический помощник'}
    ]
    return render(request, 'eras/about.html', {'team_members': team_members})