from django.urls import path
from charity import views

urlpatterns = [
   path("single_joinus", views.SingleJoinusView, name="single_joinus"),
   path("single_about", views.SingleAboutView, name="single_about"),
   path("create_pdf", views.pdf_report_create, name="create_pdf"),
   path("single_blog", views.SingleBlogView, name="single_blog"),
   path("single_gallery", views.SingleGalleryView, name="single_gallery"),
   path("state/<int:id>", views.SingleStateView, name="state"),
   path("single_humanright", views.SingleHumanrightView, name="single_humanright"),
   path("single_donation", views.SingleDonationView, name="single_donation"),
   path("partials/contact", views.ContactUsView, name="contact"),
   path("single_sponsor", views.SingleSponsorView, name="single_sponsor"),
   path("blog_detail/<int:id>", views.BlogDetailView, name="blog_detail"),
]
 