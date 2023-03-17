from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages


# Create your views here.
def login_user(request):
 return render(request, 'login.html')

def logout_user(request):
  logout(request)
  return redirect('/')



def submit_login(request):
  if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
        messages.error(request, "Usuário ou senha invalidos")
  return redirect('/')
   



@login_required(login_url='/login/')
def event_list(request):
  user = request.user
  event = Event.objects.filter(user=user)
  dados = {'event':event}
  return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def event(request):
  id_event = request.GET.get('id')
  datas = {}
  if id_event:
    datas['event'] = Event.objects.get(id=id_event)
  return render(request, 'event.html', datas)

  

@login_required(login_url='/login/')
def event_submit(resquest):
  if resquest.POST:
    title = resquest.POST.get('title')
    event_date = resquest.POST.get("event_date")
    description = resquest.POST.get("description")
    user = resquest.user
    id_event = resquest.POST.get("id_event")
    if id_event:
      event = Event.objects.get(id=id_event)
      if event.user == user:
        event.title = title
        event.description = description
        event.event_date = event_date
        event.save()
      # Event.objects.filter(id=id_event).update(title=title,
      #                                          event_date=event_date,
      #                                          description = description
      #                                          )
    else:
      Event.objects.create(title=title,
                          event_date=event_date,
                          description = description,
                          user=user )
    return redirect('/')
@login_required(login_url='/login/')
def event_delete(request, id_event):
  user = request.user
  event = Event.objects.get(id=id_event)
  if user == event.user :
    event.delete()
  return redirect('/')