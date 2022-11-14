from django.shortcuts import redirect, render
from django.db.models import Q
from medics.models import Medic
from pacients.models import Pacient
from extra.models import Turns
# from user.models import Avatar

# Create your views here.
def home(request):
    return render(request, template_name='home.html')


def about(request):
    return render(request, 'about.html')



def search(request):
    context_dict = dict()
    if request.GET['medic_search']:
        search_param = request.GET['medic_search']
        query = Q(name__contains=search_param)
        query.add(Q(surname__contains=search_param), Q.OR)
        query.add(Q(medic_type__contains=search_param), Q.OR)
        medics = Medic.objects.filter(query)
        context_dict = {
            'medics': medics
        }
    elif request.GET['pacient_search']:
        search_param = request.GET['pacient_search']
        query = Q(name__contains=search_param)
        query.add(Q(surname__contains=search_param), Q.OR)
        query.add(Q(dni__contains=search_param), Q.OR)
        pacient = Pacient.objects.filter(query)
        context_dict = {
            'pacients': pacient
        }
    elif request.GET['turn_search']:
        search_param = request.GET['turn_search']
        turn = Turns.objects.filter(day__contains=search_param)
        context_dict = {
            'turn': turn
        }

    return render(request, 'home.html', context_dict)

