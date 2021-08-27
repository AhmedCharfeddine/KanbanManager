from django.http import request
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from KanbanManager.static.KanbanManager.forms import cardForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
    projects = KanbanBoard.objects.all()
    return render(request, 'KanbanManager/index.html', {
        "projects": projects
    })

def board(request, id):
    board = KanbanBoard.objects.get(pk = id)
    cards = KanbanCard.objects.filter(board=board)
    backlog = cards.filter(state = KanbanCard.Card_states.BACKLOG)
    up_next = cards.filter(state = KanbanCard.Card_states.UP_NEXT)
    in_progress = cards.filter(state = KanbanCard.Card_states.IN_PROGRESS)
    on_hold = cards.filter(state = KanbanCard.Card_states.ON_HOLD)
    done = cards.filter(state = KanbanCard.Card_states.DONE)
    return render(request, 'KanbanManager/board.html', {
        'board': board, 
        'up_next': up_next,
        'in_progress': in_progress,
        'backlog': backlog,
        'on_hold': on_hold,
        'done': done,
    })

def new_card(request, id):
    if request.method =="POST":
        form = cardForm(request.POST)
        if form.is_valid():
            new_card = KanbanCard(
                name=form.data['name'],
                pilot = form.data['pilot'],
                description = form.data['description'],
                estimated = form.data['estimated'],
                attached = form.data['attached'],
                card_type = form.data['card_type'],
                board = KanbanBoard.objects.get(pk=id)
            )
            new_card.save()
        if 'another' not in request.POST:    
            return redirect("board", id=id)
        else:
            form = cardForm(initial={'estimated': 0}) 
    else:
        form = cardForm(initial={'estimated': 0})

    return render(request, "KanbanManager/new_card.html", {
        "form": form,
        "id": id,
    })

@csrf_exempt
def update_card(request, cardId, newColumn):
    '''
        updates a card and assigns its new column after drag and drop 
    '''
    if request.method == 'POST':
        card = KanbanCard.objects.get(pk=cardId)
        if newColumn == 0:
            col = KanbanCard.Card_states.BACKLOG
        elif newColumn == 1:
            col = KanbanCard.Card_states.UP_NEXT
        elif newColumn == 2:
            col = KanbanCard.Card_states.IN_PROGRESS
        elif newColumn == 3:
            col = KanbanCard.Card_states.ON_HOLD
        elif newColumn == 4:
            col = KanbanCard.Card_states.DONE

        card.state = col
        card.save()

    return HttpResponse('done')