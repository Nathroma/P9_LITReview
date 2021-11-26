from django import forms


class RawCreateTicketForm(forms.Form):
    """
    Form Création du ticket
    """
    title = forms.CharField(
        required=True,
        label='Titre',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titre du livre"
            },
        ),
    )
    description = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description de la demande",
            },
        ),
    )
    image = forms.ImageField(
        required=True,
    )


class RawCreateReviewForm(forms.Form):
    """
    Form création de la critique
    """
    CHOICES = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))
    headline = forms.CharField(
        required=True,
        label='Titre',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titre de la critique"
            },
        ),
    )
    rating = forms.MultipleChoiceField(
        required=True,
        label='Note',
        widget=forms.RadioSelect,
        choices=CHOICES,
    )

    body = forms.CharField(
        required=True,
        label='Description',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description de la critique",
            },
        ),
    )
