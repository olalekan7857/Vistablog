from django.db import models
from django.utils.html import mark_safe
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from datetime import timedelta
from django.utils import timezone



# Create your models here.

# Index Models 

class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, blank=True, unique=True, null=True)
    description = RichTextField(default='default')
    image = models.ImageField(upload_to='category', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # First, create the base slug
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            # Keep checking if slug already exists
            while Categories.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.slug
    
class Post(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=False)
    slug = models.SlugField(max_length=500, blank=True, unique=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # First, create the base slug
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Keep checking if slug already exists
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)    
    
    post_image = models.ImageField(upload_to='post_image', blank=False)
    content = RichTextField(default='default')
    def reading_time(self):
        words_per_minute = 200
        word_count = len(self.content.split())
        estimated_time = int(word_count / words_per_minute)
        return f"{max(1, estimated_time)} min read"
    
    content_video = models.FileField(blank=True, upload_to='post_videos')
    date = models.DateTimeField(auto_now_add=True)
    def get_human_date(self):
        now = timezone.now()
        delta = now - self.date

        if delta < timedelta(hours=1):
            mins = int(delta.total_seconds() // 60)
            if mins < 1:
                return "Just now"
            else:
                return f"{mins} min{'s' if mins != 1 else ''} ago"

        elif delta < timedelta(days=1):
            hours = int(delta.total_seconds() // 3600)
            return f"{hours} hour{'s' if hours != 1 else ''} ago"

        elif delta < timedelta(days=30):
            days = delta.days
            return f"{days} day{'s' if days != 1 else ''} ago"

        else:
            # return self.date.strftime("%-d %B %Y")
            return self.date.strftime(f"{self.date.day} %B %Y")  # Explicitly get the day as integer

    def post_image_des(self):
        return mark_safe(f"<img src='{self.post_image.url}' height='45' style='border-radius: 50%;' >")

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title    
    
# About models 

class Mission(models.Model):
    content = RichTextField()
     
    class Meta:
        verbose_name = 'Mission'
        verbose_name_plural = 'Mission'


class Profile(models.Model):
    author_image = models.ImageField(upload_to='author', blank=False)
    about_author = RichTextField(default='default')

    def profile_image(self):
        return mark_safe(f"<img src='{self.author_image.url}' height='45' style='border-radius: 50%;'>")
        

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    

class Acknowledgement(models.Model):
    content = RichTextField(default='thanks')

    class Meta:
        verbose_name = 'Acknowledgment'
        verbose_name_plural = 'Acknowledgments'

    

class Review_message(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review_message'
        verbose_name_plural = 'Review_messages'

    def __str__(self):
        return self.message  


class Comment(models.Model):
    commenter = models.CharField(max_length = 50)
    body = models.TextField(blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(auto_now_add=True)
    def get_human_date(self):
        now = timezone.now()
        delta = now - self.date

        if delta < timedelta(hours=1):
            mins = int(delta.total_seconds() // 60)
            if mins < 1:
                return "Just now"
            else:
                return f"{mins} min{'s' if mins != 1 else ''} ago"

        elif delta < timedelta(days=1):
            hours = int(delta.total_seconds() // 3600)
            return f"{hours} hour{'s' if hours != 1 else ''} ago"

        elif delta < timedelta(days=30):
            days = delta.days
            return f"{days} day{'s' if days != 1 else ''} ago"

        else:
            return self.date.strftime("%d %B %Y")

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.body  