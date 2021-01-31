from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Follower, Post, User


def index(request):
    posts = Post.objects.all()

    return render(request, "network/index.html", {"posts": posts})


@login_required
def get_following_posts(request):
    user = User.objects.get(id=request.user.id)
    following = user.following.all()
    bleh = [follow.user for follow in following]
    posts = Post.objects.filter(user__in=bleh)

    return render(request, "network/following.html", {"posts": posts})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(
                request,
                "network/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(
                request, "network/register.html", {"message": "Passwords must match."}
            )

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request, "network/register.html", {"message": "Username already taken."}
            )
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@login_required
def like_post(request, post_id):
    if request.method == "POST":

        post = Post.objects.get(id=post_id)

        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            post.save()
            return JsonResponse({"liked": "False", "post_id": post_id}, status=200)

        post.likes.add(user)
        post.save()
        return JsonResponse({"liked": "True", "post_id": post_id}, status=200)


@login_required
def post(request, post_id=None):
    if request.method == "POST":
        if not request.POST["post_id"]:
            user = User.objects.get(id=request.user.id)
            user_post = Post.objects.create(
                user=user, message=request.POST["post-message"]
            )
            user_post.save()

            return HttpResponseRedirect(reverse("index"))

        user = User.objects.get(id=request.user.id)
        user_post = Post.objects.get(id=int(request.POST["post_id"]))
        user_post.message = request.POST["post-message"]
        user_post.save()

        return HttpResponseRedirect(reverse("index"))

    if post_id:
        post = Post.objects.get(id=post_id)

        if request.user.id != post.user.id:
            return HttpResponseRedirect(reverse("index"))

        return render(
            request,
            "network/post.html",
            {"post_id": post.id, "post_message": post.message},
        )

    return render(request, "network/post.html")


def get_user(request, user_id):
    user_profile = User.objects.get(id=user_id)

    followed_user, _ = Follower.objects.get_or_create(user=user_profile)
    following = request.user in followed_user.followers.all()

    # import pdb

    # pdb.set_trace()

    return render(
        request, "network/profile.html", {"user": user_profile, "following": following}
    )


def follow_user(request, user_id):
    if request.method == "POST":
        # import pdb

        # pdb.set_trace()
        user = User.objects.get(id=user_id)

        follower, _ = Follower.objects.get_or_create(user=user)

        if request.user not in follower.followers.all():
            follower.followers.add(request.user)
            follower.save()

            return JsonResponse(
                {"followed": True, "user_id": user.id, "follower": request.user.id},
                status=200,
            )

        follower.followers.remove(request.user)
        follower.save()

        return JsonResponse(
            {"followed": False, "user": user.id, "follower": request.user.id},
            status=200,
        )

    return JsonResponse({"message": "Can only post to method"}, status=400)
