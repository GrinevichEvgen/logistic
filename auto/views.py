from django.shortcuts import render

from .models import Auto


def auto_list(request):
    auto = Auto.objects.all()
    return render(request, 'auto_list.html', {'auto': auto})
