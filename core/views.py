from django.shortcuts import render
from core.models import Event

# Create your views here.


def event_list(request):
  event = Event.objects.all()
  dados = {'event':event}
  return render(request, 'agenda.html', dados)