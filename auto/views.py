import logging

from django.shortcuts import render

from .models import Auto

logger = logging.getLogger(__name__)


def auto_list(request):
    auto = Auto.object.all()
    return render(request, 'auto_list.html', {'auto': auto})
