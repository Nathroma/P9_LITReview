from django import forms


class FollowUser(forms.Form):
    followed_user = forms.CharField(
        required=True,
        label='Pseudo',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Pseudo"
            },
        ),
    )
