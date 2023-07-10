
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import DriverForm
from .models import Driver


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})


def driver_new(request):
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_list')
    else:
        form = DriverForm()
    return render(request, 'drivers/driver_new.html', {'form': form})
