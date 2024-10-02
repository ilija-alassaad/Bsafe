from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from .utils import code_generator, create_shortcode
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.CharField(max_length=600, blank=True, null=True)
    image = models.ImageField(
        upload_to='blog/posts/', verbose_name=_("Post Image"), blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    content = models.TextField(blank=True, null=True,
                             verbose_name=_("Content"))
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    post_Slug = models.SlugField(max_length=500,
                                 blank=True, null=True, allow_unicode=True, unique=True, verbose_name=_("Slugfiy"))

    def __str__(self):

        return str(self.title)

    # def save(self, *args, **kwargs):
    #     if not self.post_Slug:
    #         self.post_Slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:postdetail', kwargs={'slug': self.post_Slug})


def pre_save_post_receiver(sender, instance, *args, **kwargs):

    if not instance.post_Slug or instance.post_Slug is None or instance.post_Slug == "":
        instance.post_Slug = slugify(instance.title, allow_unicode=True)
        qs_exists = BlogPost.objects.filter(
            post_Slug=instance.post_Slug).exists()
        if qs_exists:
            instance.post_Slug = create_shortcode(instance)


pre_save.connect(pre_save_post_receiver, sender=BlogPost)
