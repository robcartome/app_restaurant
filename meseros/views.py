from django.shortcuts import render
from .models import Meseros

# Create your views here.
def meseros_list(request):
    data_context = Meseros.objects.all()
    print(data_context)
    return render(request, 'meseros/meseros_list.html', context={'data': data_context})
