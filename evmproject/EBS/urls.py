from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name="index"),
        path('Login', views.Login, name="Login"),
        path('about', views.about, name="about"),
        path('contact', views.contact, name="contact"),
        path('innerhome', views.innerhome, name="innerhome"),
        path('Logout', views.Logout, name="Logout"),
        path('usersignup', views.usersignup, name="usersignup"),
        path('Userlogin',views.Userlogin, name="Userlogin"),

        path('Ownerlogin',views.Ownerlogin, name="Ownerlogin"),
        path('ownersignup', views.ownersignup, name="ownersignup"),
        path('ownerhome', views.ownerhome, name="ownerhome"),

        path('userhome', views.userhome, name="userhome"),
        path('add_event', views.add_event, name="add_event"),
        path('view_event', views.view_event, name="view_event"),
        path('delete_event(?p<int:pid>)', views.delete_event, name="delete_event"),
        path('add_sponsor', views.add_sponsor, name="add_sponsor"),
        path('view_sponsor', views.view_sponsor, name="view_sponsor"),
        path('delete_sponsor(?p<int:pid>)', views.delete_sponsor, name="delete_sponsor"),
        path('add_category', views.add_category, name="add_category"),
        path('view_category', views.view_category, name="view_category"),
        path('delete_category(?p<int:pid>)', views.delete_category, name="delete_category"),
        path('view_user', views.view_user, name="view_user"),

        path('view_owner', views.view_owner, name="view_owner"),
        path('delete_user(?p<int:pid>)', views.delete_user, name="delete_user"),
        path('delete_owner(?p<int:pid>)', views.delete_owner, name="delete_owner"),
        path('view_eventuser', views.view_eventuser, name="view_eventuser"),
        path('view_details(?p<int:pid>)', views.view_details, name="view_details"),
        path('book_now/<int:pid>', views.book_now, name="book_now"),
        path('view_mybooking', views.view_mybooking, name="view_mybooking"),
        path('delete_booking(?p<int:pid>)', views.delete_booking, name="delete_booking"),
        path('change_passworduser', views.change_passworduser, name="change_passworduser"),

        path('change_passwordowner', views.change_passwordowner, name="change_passwordowner"),

        path('change_passwordadmin', views.change_passwordadmin, name="change_passwordadmin"),
        path('booking_request', views.booking_request, name="booking_request"),
        path('bookingdetail_user/<int:pid>', views.bookingdetail_user, name="bookingdetail_user"),
        path('bookingdetail_admin/<int:pid>', views.bookingdetail_admin, name="bookingdetail_admin"),
        path('accepted_booking', views.accepted_booking, name="accepted_booking"),
        path('rejected_booking', views.rejected_booking, name="rejected_booking"),
        path('all_booking', views.all_booking, name="all_booking"),
        path('confirmed_booking', views.confirmed_booking, name="confirmed_booking"),
        path('edit_event/<int:pid>', views.edit_event, name="edit_event"),
        path('edit_sponsor/<int:pid>', views.edit_sponsor, name="edit_sponsor"),
        path('edit_category/<int:pid>', views.edit_category, name="edit_category"),
        path('payment/<int:pid>', views.payment, name="payment"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)