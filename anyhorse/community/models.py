from django.db import models
from django.utils import timezone

class Post(models.Model):
    #title, body, show, datatime, image
    PUBLIC='public'
    PRIVATE='private'
    MY='my'
    SHOW_TYPES=[
        (PUBLIC, 'PUBLIC'),
        (PRIVATE, 'PRIVATE'),
        (MY, 'MY'),
    ]
    title=models.CharField(max_length=50, help_text="제목")
    body=models.TextField(help_text="본문 내용")
    show=models.CharField(max_length=10, choices=SHOW_TYPES, default=PUBLIC, help_text="비공개 여부")
    datatime=models.DateTimeField(default=timezone.now)
    image=models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('community.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text