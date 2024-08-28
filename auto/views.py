import logging

from django.shortcuts import render

from .models import Auto

logger = logging.getLogger(__name__)


def auto_list(request):
    logger.info('Listing auto')
    autos = Auto.objects.all()
    return render(request, 'auto_list.html', {'autos': autos})
