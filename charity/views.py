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
        image = request.POST["card"]

        data = Volunteer(name=uname,address=add,gender=gen,email=mail,contact=contact,time=time,image=image)
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

#blog_detail
def BlogDetailView(request):
    blog = Blog.objects.all().order_by('created_at').reverse()
    template_name = "blog_detail.html"
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
        job = request.POST["job"]
        country = request.POST["country"]
        add = request.POST["address"]
        city = request.POST["city"]
        province = request.POST["province"]
        purpose = request.POST["purpose"]
        amount = request.POST["amount"]
        mode = request.POST["mode"]
        data = Donation(name=uname,email=mail,contact=contact,job=job,country=country,address=add,city=city,
                        province=province, purpose=purpose, mode=mode, amount=amount)
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

