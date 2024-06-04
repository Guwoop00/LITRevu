from django.contrib.auth import get_user_model
from django import forms
from posts.models import Review, Ticket
from typing import Any

User: Any = get_user_model()


class TicketForm(forms.ModelForm):
    """Form for creating or editing a ticket."""
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }
        labels = {
            'title': 'Titre du livre',
        }


class DeleteTicketForm(forms.Form):
    """Form for deleting a ticket."""
    delete_ticket: Any = forms.BooleanField(widget=forms.HiddenInput, required=False)


class ReviewForm(forms.ModelForm):
    """Form for creating or editing a review."""
    class Meta:
        model: Any = Review
        fields: Any = ['headline', 'rating', 'body']
        widgets: Any = {
            'rating': forms.RadioSelect(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')],
                                        attrs={
                                            "style": "display:flex;"
                                            "flex-direction:row;"
                                            "gap:30px;"
                                            "justify-content:space-around;"
                                              }
                                        ),
            'body': forms.Textarea(attrs={'rows': 6}),
        }
        labels: Any = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',

        }


class DeleteReviewForm(forms.Form):
    """Form for deleting a review."""
    delete_review: Any = forms.BooleanField(widget=forms.HiddenInput, required=False)
