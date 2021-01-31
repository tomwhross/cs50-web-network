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

    def __str__(self):
        return f"{self.user} - {self.message} - {self.likes.count()} likes"

    @property
    def like_count(self):
        return self.likes.count()


# class Like(models.Model):
#     user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user")
#     post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post")

#     created_on = models.DateTimeField(auto_now_add=True)
#     modified_on = models.DateField(auto_now=True)


class Follower(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="followed_user"
    )
    followers = models.ManyToManyField("User", blank=True, related_name="following")
    # follower = models.ForeignKey(
    #     "User", on_delete=models.CASCADE, related_name="followers"
    # )

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
