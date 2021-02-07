from django.contrib.auth.models import AbstractUser
from django.db import models

POST_MAX_LENGTH = 240


class User(AbstractUser):
    pass


class Post(models.Model):
    """
    A user can make posts
    """

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    message = models.TextField(max_length=POST_MAX_LENGTH, blank=False)
    likes = models.ManyToManyField("User", blank=True, related_name="likes")

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.message} - {self.likes.count()} likes"

    @property
    def like_count(self):
        """
        A count of how many likes a post has
        """
        return self.likes.count()


class Following(models.Model):
    """ A user has a following made up of followers which are other users """

    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="followed_user"
    )
    followers = models.ManyToManyField("User", blank=True, related_name="following")

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    @property
    def follower_count(self):
        """
        A count of how many followers a user has
        """
        return self.followers.count()

    def __str__(self):
        return f"{self.user.username} with {self.follower_count} followers"
