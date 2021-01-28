from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    message = models.TextField(blank=True)
    likes = models.ManyToManyField("User", blank=True, related_name="likes")

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)


# class Like(models.Model):
#     user = models.ForeignKey(
#         "User", on_delete=models.CASCADE, related_name="user_likes"
#     )
#     post = models.ForeignKey(
#         "User", on_delete=models.CASCADE, related_name="post_likes"
#     )

#     created_on = models.DateTimeField(auto_now_add=True)
#     modified_on = models.DateField(auto_now=True)


class Follower(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="user_follower"
    )
    followers = models.ManyToManyField("User", blank=True, related_name="followers")
    # follower = models.ForeignKey(
    #     "User", on_delete=models.CASCADE, related_name="followers"
    # )

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
