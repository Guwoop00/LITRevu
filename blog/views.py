from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Review, Ticket
from django.contrib.auth import get_user_model
from blog.forms import FollowUserForm
from django.http import HttpRequest, HttpResponse
from typing import List, Dict, Union
from django.db.models import Q

User = get_user_model()


@login_required()
def home(request: HttpRequest, feed_type: str = None) -> HttpResponse:
    """
    View function to display the user's feed.

    Args:
        request (HttpRequest): The request object.
        feed_type (str, optional): Type of feed to display. Defaults to None.

    Returns:
        HttpResponse: Response object containing the rendered HTML.
    """
    feed: List[Dict[str, Union[Ticket, Review]]] = []

    # Personalized feed
    if feed_type == 'home':
        user = request.user
        followed_users = user.follows.all()
        tickets = Ticket.objects.filter(Q(user__in=followed_users) | Q(user=user))
        for ticket in tickets:
            reviews = Review.objects.filter(ticket=ticket)
            feed.append({'ticket': ticket, 'reviews': reviews})

    # My posts
    elif feed_type == 'my_posts':
        user = request.user
        user_tickets = Ticket.objects.filter(user=user)
        user_reviews = Review.objects.filter(user=user)

        for ticket in user_tickets:
            ticket_reviews = Review.objects.filter(ticket=ticket)
            feed.append({'ticket': ticket, 'reviews': ticket_reviews})

        for review in user_reviews:
            ticket = review.ticket
            entry_exists = any(item['ticket'] == ticket for item in feed)
            if not entry_exists:
                feed.append({'ticket': ticket, 'reviews': [review]})

    feed = sorted(feed, key=lambda x: x['ticket'].time_created, reverse=True)

    return render(request, 'blog/feed.html', {'feed': feed})




@login_required
def follow_user(request: HttpRequest) -> HttpResponse:
    """
    View function to handle following users.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Response object containing the rendered HTML.
    """
    if request.method == 'POST':
        form = FollowUserForm(request.user, request.POST)
        if form.is_valid():
            following = form.save(commit=False)
            following.user = request.user
            following.save()
            return redirect('follow_user')
    else:
        form = FollowUserForm(request.user)

    followed_users = request.user.follows.all()
    users_to_follow = User.objects.exclude(id=request.user.id).exclude(id__in=followed_users)
    context = {
        'form': form,
        'users_to_follow': users_to_follow,
        'followed_users': followed_users,
        'followers': request.user.followers.all()
    }
    return render(request, 'blog/follow_user.html', context=context)


@login_required
def unfollow_user(request: HttpRequest, username: str) -> HttpResponse:
    """
    View function to handle unfollowing users.

    Args:
        request (HttpRequest): The request object.
        username (str): Username of the user to unfollow.

    Returns:
        HttpResponse: Response object containing the rendered HTML.
    """
    user_to_unfollow = get_object_or_404(User, username=username)

    if request.method == 'POST':
        if user_to_unfollow in request.user.follows.all():
            request.user.follows.remove(user_to_unfollow)
            return redirect('follow_user')

    return render(request, 'blog/unfollow_user.html', {'user_to_unfollow': user_to_unfollow})
