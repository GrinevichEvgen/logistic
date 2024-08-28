from django.shortcuts import render
from .models import Route
import logging

logger = logging.getLogger(__name__)


def route_list(request):
    logger.info('Listing routes')
    trips = Route.objects.all()
    return render(request, 'route_list.html', {'trips': trips})
