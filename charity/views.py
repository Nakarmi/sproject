from django.shortcuts import render, HttpResponse
from django.views import View
from charity.models import Volunteer, State, Blog, Gallery, Donation, Activities, ContactUs, Sponsor

# Create your views here.
#single_joinus
def SingleJoinusView(request):
    template_name = "single_joinus.html"
    if request.method=="POST":        
        uname = request.POST["name"]
        add = request.POST["address"]
        gen = request.POST["gender"]
        mail = request.POST["email"]
        contact = request.POST["contact"]
        time = request.POST["time"]

        data = Volunteer(name=uname,address=add,gender=gen,email=mail,contact=contact,time=time)
        data.save()
        res = "Dear {} Thankyou for your support".format(uname)
        return render(request,template_name,{"status":res})
        # return HttpResponse
    return render(request, template_name)

#single_about
def SingleAboutView(request):
    about = Activities.objects.all().order_by('date').reverse()
    template_name = "single_about.html"
    return render(request, template_name, {'about':about})

#single_blog
def SingleBlogView(request):
    blog = Blog.objects.all().order_by('created_at').reverse()
    template_name = "single_blog.html"
    return render(request, template_name, {'blog':blog})

#single_gallery
def SingleGalleryView(request):
    gallery = Gallery.objects.all().order_by('id').reverse()
    template_name = "single_gallery.html"
    return render(request, template_name, {'images' : gallery})

#single_state
def SingleStateView(request):
    state = State.objects.all()
    template_name = "partials/state.html"
    return render(request, template_name, {'state':state})

#single_humanright
def SingleHumanrightView(request):
    template_name = "single_humanright.html"
    return render(request, template_name)

#contact_us
def ContactUsView(request):
    template_name = "partials/contact.html"
    if request.method=="POST":        
        name = request.POST["name"]
        mail = request.POST["email"]
        contact = request.POST["contact"]
        msg = request.POST["msg"]

        data = ContactUs(name=name,email=mail,contact=contact,message=msg)
        data.save()
        res = "Dear {} Thankyou for supporting us.".format(name)
        return render(request,template_name,{"status":res})
        # return HttpResponse
    return render(request, template_name)

#single_donation
def SingleDonationView(request):
    template_name = "single_donation.html"
    if request.method=="POST":        
        uname = request.POST["name"]
        mail = request.POST["email"]
        contact = request.POST["contact"]
        country = request.POST["country"]
        add = request.POST["address"]
        city = request.POST["city"]
        zone = request.POST["zone"]
        purpose = request.POST["purpose"]

        data = Donation(name=uname,email=mail,contact=contact,country=country,address=add,city=city,zone=zone, purpose=purpose)
        data.save()
        res = "Dear {} Thankyou for your support".format(uname)
        return render(request,template_name,{"status":res})
        # return HttpResponse
    return render(request, template_name)

#single_sponsor
def SingleSponsorView(request):
    sponsor = Sponsor.objects.all().order_by('age')
    template_name = "single_sponsor.html"
    return render(request, template_name, {'sponsor' : sponsor})
