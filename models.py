from django.db import models

class KitabPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BabPost(models.Model):
    KitabPost = models.ForeignKey(KitabPost, related_name="BabPost", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class FasalPost(models.Model):
    KitabPost = models.ForeignKey(KitabPost, related_name="FasalPost", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    
    
