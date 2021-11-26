from .models import UserFollows
from .forms import FollowUser
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError


def home(request):

    if request.user.is_authenticated is False:
        return redirect('login')
    else:
        if request.method == 'POST':
            form = FollowUser(request.POST)
            if form.is_valid:
                try:
                    follow_user = User.objects.get(
                        username=request.POST['followed_user']
                    )

                    if request.user == follow_user:
                        messages.error(
                            request,
                            'Vous ne pouvez pas vous ajouter vous même.',
                        )
                    else:
                        try:
                            UserFollows.objects.create(
                                user=request.user,
                                followed_user=follow_user,
                            )
                        except IntegrityError:
                            messages.error(
                                request,
                                'Vous avez déjà ajouter cet utilisateur.',
                            )
                except User.DoesNotExist:
                    messages.error(request, "Cet utilisateur n'existe pas.")

        else:
            form = FollowUser()

        following_list = []
        followers_list = []

        for f in UserFollows.objects.filter(user_id=request.user):
            following_list.append(User.objects.get(id=f.followed_user_id))

        for f in UserFollows.objects.filter(followed_user_id=request.user):
            followers_list.append(User.objects.get(id=f.user_id))

        context = {
            'form': form,
            'following': following_list,
            'followers': followers_list,
        }

        return render(request, 'subs.html', context)


def unsubscribe(request, id):

    if request.user.is_authenticated is False:
        return redirect('login')
    else:
        UserFollows.objects.filter(
            user_id=request.user
        ).filter(followed_user_id=id).delete()
        return redirect('subs')
