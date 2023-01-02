from django.db.models import Model, ImageField, CharField, IntegerField, BooleanField, TextField, URLField


class About(Model):
    image = ImageField(upload_to='about/')
    full_name = CharField(max_length=300, default='Jasur Juraev')
    birthday = CharField(max_length=200, default='26 January 2005')
    web_site = CharField(max_length=155, default='www.jasur.com')
    phone = CharField(max_length=200, default='+998 (94) 800 2005')
    city = CharField(max_length=200, default='Tashkent, UZB')
    age = IntegerField(default=17)
    degree = CharField(max_length=100, default='Junior')
    email = CharField(max_length=300, default='jasurkkirchh@gmail.com')
    freelance = BooleanField(default=True)
    description = TextField()
    instagram_link = URLField(null=True)
    facebook_link = URLField(null=True)
    twitter_link = URLField(null=True)
    linkedin_link = URLField(null=True)

