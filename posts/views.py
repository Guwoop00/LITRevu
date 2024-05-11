from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (DeleteReviewForm, DeleteTicketForm, ReviewForm,
                    TicketForm)
from .models import Review, Ticket


def ticket_response(request: HttpRequest, id: int) -> HttpResponse:
    """View for responding to a ticket."""
    ticket = get_object_or_404(Ticket, id=id)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')

    context = {
        'form': form,
        'ticket': ticket
    }
    return render(request, 'posts/ticket_response.html', context=context)


@login_required
def create_review_and_ticket(request: HttpRequest) -> HttpResponse:
    """View for creating a review and a ticket."""
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        ticket_form = TicketForm(request.POST, request.FILES)
        if all([review_form.is_valid(), ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    else:
        review_form = ReviewForm()
        ticket_form = TicketForm()

    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'posts/create_review_and_ticket.html', context=context)


@login_required
def create_ticket(request: HttpRequest) -> HttpResponse:
    """View for creating a ticket."""
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')

    return render(request, 'posts/create_ticket.html', {'form': form})


@login_required
def edit_ticket(request: HttpRequest, id: int) -> HttpResponse:
    """View for editing a ticket."""
    ticket = get_object_or_404(Ticket, id=id)
    form = TicketForm(instance=ticket)
    delete_form = DeleteTicketForm()

    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            form = TicketForm(request.POST, request.FILES, instance=ticket)
            if form.is_valid():
                form.save()
                return redirect('home')
        elif 'delete_ticket' in request.POST:
            delete_form = DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'form': form,
        'delete_form': delete_form,
        'ticket': ticket,
    }
    return render(request, 'posts/edit_ticket.html', context=context)


@login_required
def edit_review(request: HttpRequest, id: int) -> HttpResponse:
    """View for editing a review."""
    review = get_object_or_404(Review, id=id)
    ticket = review.ticket
    review_form = ReviewForm(instance=review)
    ticket_form = TicketForm(instance=ticket)
    delete_form = DeleteReviewForm()

    if request.method == 'POST':
        if 'edit_review' in request.POST:
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            ticket_form = TicketForm(request.POST, request.FILES, instance=ticket)
            if all([review_form.is_valid(), ticket_form.is_valid()]):
                review_form.save()
                ticket_form.save()
                return redirect('home')
        elif 'delete_review' in request.POST:
            delete_form = DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                ticket.delete()
                return redirect('home')
    context = {
        'review_form': review_form,
        'ticket_form': ticket_form,
        'delete_form': delete_form,
        'review': review,
        'ticket': ticket
    }
    return render(request, 'posts/edit_review.html', context=context)
