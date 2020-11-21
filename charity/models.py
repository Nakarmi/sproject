from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.
# DJANGO-ORM (Object relational mapping)

#BLOG
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    # slug = models.SlugField(max_length=255, null=True)
    # category = models.ManyToManyField(Category, related_name="news_categoreis")
    author = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="blog", null=True)
    
    # def get_absolute_url(self):
    #     return reverse("single_blog", kwargs={"pk": self.pk, "slug": self.slug})
    def __str__(self):
        return self.title+" "+str(self.created_at)+" "+str(self.updated_at)

#GALLERY
class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery", null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Galleries"

#VOLUNTEER
class Volunteer(models.Model):
    g = (
        ("M", "Male"), ("F", "Female"), ("T", "LGBTQ")
    )    
    name = models.CharField(max_length=255)    
    address = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=12, choices=g, null=True)
    email_regex = RegexValidator(regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="Email must be entered in the format: 'example@example.com'")
    email = models.CharField(validators=[email_regex], max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98********'. Up to 10 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, null=True)
    time = models.CharField(max_length=75)
    status = models.BooleanField(null=True)
    joined_from = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.name+" "+self.address+" "+self.gender+" "+self.email+" "+self.contact+" "+str(self.joined_from)

#STATE
class State(models.Model):
    donation = models.IntegerField()
    volunteers = models.IntegerField()
    rescued = models.IntegerField()
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.donation)+" "+str(self.volunteers)+" "+str(self.rescued)

#CONTACTUS
class ContactUs(models.Model):
    name = models.CharField(max_length=255)    
    email_regex = RegexValidator(regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="Email must be entered in the format: 'example@example.com'")
    email = models.CharField(validators=[email_regex], max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98********'. Up to 10 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, null=True)
    submitted_at = models.DateField(auto_now_add=True)
    message = models.CharField(max_length=755)    

    def __str__(self):
        return self.name+" "+self.email+" "+self.contact+" "+str(self.submitted_at)+" "+self.message

    class Meta:
        verbose_name_plural = "Contact us"

#DONATION
class Donation(models.Model):
    name = models.CharField(max_length=255)    
    email_regex = RegexValidator(regex=r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="Email must be entered in the format: 'example@example.com'")
    email = models.CharField(validators=[email_regex], max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98********'. Up to 10 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10)
    country = models.CharField(max_length=100)  
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zone = models.CharField(max_length=100)
    # zip_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '98********'. Up to 10 digits allowed.")
    # zip = models.CharField(max_length=100, null=True)
    # slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.name+" "+self.email+" "+self.contact+" "+self.country+" "+self.address+" "+self.city+" "+self.zone
