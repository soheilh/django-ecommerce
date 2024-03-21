from django.db import models
from django.utils import timezone
from user.models import CustomerUser
from ckeditor.fields import RichTextField

# Model for Category
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbos_name_plural = "Categories"

    def __str__(self):
        return self.name

# Model for Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    # author = models.ForeignKey(, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(to=Category, related_name="posts")
    thumb = models.ImageField(upload_to ='thumbs', default='thumbs/default.jpg')
    image = models.ImageField(upload_to ='images', default='images/default.jpg')
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('a', 'Archived'),
        ('pa', 'Pending Approval'),
        ('d', 'Deleted'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='p')
    content = RichTextField(default='')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']

# Model for Comment
class Comment(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    COMMENT_STATUS = (
        ('w', 'Waiting'),
        ('a', 'Accepted'),
        ('r', 'Rejected'),
    )
    status = models.CharField(max_length=1, choices=COMMENT_STATUS, default='a')

    def __str__(self):
        return self.body[0:50]
