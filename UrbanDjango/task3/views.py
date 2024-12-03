from django.shortcuts import render
from django.views.generic import TemplateView


class Platform(TemplateView):
    template_name = "third_task/platform.html"


def games(request):
    games_list = ['Atomic Heart', 'Cyberpunk2077', 'PayDay2']
    context = {'games_list': games_list}
    return render(request, 'third_task/games.html', context=context, )

def cart(request):
    return render(request, 'third_task/cart.html')

