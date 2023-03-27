from ckeditor.fields import RichTextField
from django.db.models import Model, ImageField, CharField, IntegerField, BooleanField, TextField, URLField, EmailField, \
    SlugField, ForeignKey, CASCADE, DateTimeField, ManyToManyField
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django_resized import ResizedImageField


class About(Model):
    image = ImageField(upload_to='about/')
    full_name = CharField(max_length=300, default='Jasur Juraev')
    birthday = CharField(max_length=200, default='26 January 2005')
    web_site = CharField(max_length=155, default='www.jasur.com')
    phone = CharField(max_length=200, default='+998 (94) 800 2005')
    city = CharField(max_length=200, default='Tashkent, UZB')
    age = IntegerField(default=17)
    degree = CharField(max_length=100, default='Junior')
    email = EmailField(max_length=300, default='jasurkkirchh@gmail.com')
    freelance = BooleanField(default=True)
    description = TextField()
    instagram_link = URLField(null=True)
    facebook_link = URLField(null=True)
    twitter_link = URLField(null=True)
    linkedin_link = URLField(null=True)


class Skill(Model):
    name = CharField(max_length=255)
    percent = IntegerField()


class Sumary(Model):
    full_name = CharField(max_length=300, default='Jasur Juraev')
    description = TextField()
    city = CharField(max_length=200, default='Tashkent, Uzbekistan')
    phone = CharField(max_length=200, default='+998 (94) 800 2005')
    email = EmailField(max_length=300, default='jasurkkirchh@gmail.com')


class Education(Model):
    title = CharField(max_length=200)
    year = CharField(max_length=155)
    place = CharField(max_length=300)
    description = TextField()


class Category(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            slug = Category.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.name:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)


class Project(Model):
    title = CharField(max_length=255)
    description = RichTextField()
    category = ForeignKey(Category, CASCADE, null=True)
    client = CharField(max_length=255)
    pic = ResizedImageField(upload_to='projects/product')
    date = DateTimeField(auto_now=True)
    url = URLField()
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="70" height="50" />' % (self.pic))

    image_tag.short_description = 'Image'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        while Category.objects.filter(slug=self.slug).exists():
            slug = Category.objects.filter(slug=self.slug).first().slug
            if '-' in slug:
                try:
                    if slug.split('-')[-1] in self.title:
                        self.slug += '-1'
                    else:
                        self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                except:
                    self.slug = slug + '-1'
            else:
                self.slug += '-1'

        super().save(*args, **kwargs)


class Image(Model):
    image = ResizedImageField(upload_to='projects/')
    project = ManyToManyField(Project)


class Message(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=300)
    subject = CharField(max_length=350)
    message = TextField()
    date = DateTimeField(auto_now_add=True)
    answered = BooleanField(default=False)
