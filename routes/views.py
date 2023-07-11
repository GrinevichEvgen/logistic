from django.shortcuts import render
from .models import Route


def route_list(request):
    route = Route.objects.all()
    return render(request, 'route_list.html', {'route': route})
