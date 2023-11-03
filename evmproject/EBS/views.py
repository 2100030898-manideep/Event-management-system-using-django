from django.shortcuts import render, redirect

from .forms import UpdatePasswordOwnerForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date
from .models import OwnerSignup

def index(request):
    return render(request, "index.html")


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user:
            try:
                if user.is_authenticated:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
    d = {'error': error}
    return render(request, "login.html", d)


def Userlogin(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['pwd']
        user = authenticate(username=e, password=p)
        if user:
            try:
                flag = UserSignup.objects.get(user=user)
                if flag:
                    login(request, user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'userlogin.html', d)

def Ownerlogin(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['email']
        p = request.POST['pwd']
        owner = authenticate(username=e, password=p)
        if owner:
            try:
                flag = OwnerSignup.objects.get(owner=owner)
                if flag:
                    login(request, owner)
                    error = "no"
                else:
                    error = "yse"
            except:
                error = "yse"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'ownerlogin.html', d)

def change_passwordowner(request):
    if not request.user.is_authenticated:
        return redirect('ownerlogin')
    error = ""
    form = UpdatePasswordOwnerForm()
    if request.method == "POST":
        form = UpdatePasswordOwnerForm(request.POST)
        c = request.POST['currentpassword']
        n = request.POST['newpassword']

        try:
            u = User.objects.get(id=request.user.id)

            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "no"
        except:
            error = "yes"
    d = {"error": error , "form" : form}
    return render(request, "changepasswordowner.html", d)


def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "changepassworduser.html", d)

def ownerhome(request):
    if not request.user.is_authenticated:
        return redirect('Userlogin')
    user = request.user
    data = OwnerSignup.objects.get(owner=user)
    error = ""
    if request.method == 'POST':
        #con = request.POST['contact']
        fn = request.POST['fname']
        ln = request.POST['lname']
        address = request.POST['address']

        #data.mobile = con
        data.owner.first_name = fn
        data.owner.last_name = ln
        data.owneraddress = address
        try:
            data.save()
            data.owner.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            data.ownerimage = i
            data.save()
            error = "no"
        except:
            pass
    return render(request, "ownerhome.html", {"data": data, 'error': error})

def userhome(request):
    if not request.user.is_authenticated:
        return redirect('Userlogin')
    user = request.user
    data = UserSignup.objects.get(user=user)
    error = ""
    if request.method == 'POST':
        con = request.POST['contact']
        fn = request.POST['fname']
        ln = request.POST['lname']
        address = request.POST['address']

        data.mobile = con
        data.user.first_name = fn
        data.user.last_name = ln
        data.address = address
        try:
            data.save()
            data.user.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            data.image = i
            data.save()
            error = "no"
        except:
            pass
    d = {"data": data, 'error': error}
    return render(request, "userhome.html", d)


def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {"error": error}
    return render(request, "changepassword_admin.html", d)


def add_event(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    category = Category.objects.all()
    if request.method == 'POST':
        en = request.POST['ename']
        i = request.FILES['image']
        cat = request.POST['category']
        des = request.POST['description']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        ve = request.POST['venue']
        ep = request.POST['price']


        try:
            Event.objects.create(eventname=en, image=i, category=cat, description=des, startdate=sd, enddate=ed,
                                 venue=ve, entryprice=ep)
            error = "no"
        except:
            error = "yes"

    return render(request, "add_event.html", locals())


def edit_event(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    category = Category.objects.all()
    event = Event.objects.get(id=pid)
    if request.method == 'POST':
        en = request.POST['ename']

        cat = request.POST['category']
        des = request.POST['description']

        ve = request.POST['venue']
        ep = request.POST['price']
        event.eventname = en
        event.category = cat
        event.description = des
        event.venue = ve
        event.entryprice = ep

        try:
            event.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            event.image = i
            event.save()
        except:
            pass
        try:
            startdate = request.POST['startdate']
            event.startdate = startdate
            event.save()
        except:
            pass
        try:
            enddate = request.POST['enddate']
            event.enddate = enddate
            event.save()
        except:
            pass
    return render(request, "edit_event.html", locals())


def view_event(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    event = Event.objects.all()
    d = {'event': event}
    return render(request, "view_event.html", d)


def view_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    data = Event.objects.get(id=pid)
    sponsor = SponsorTbl.objects.filter(event=data)
    return render(request, "details.html", locals())


def view_eventuser(request):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    event = Event.objects.all()
    d = {'event': event}
    return render(request, "view_eventuser.html", d)


def delete_event(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = Event.objects.get(id=pid)
    apoint.delete()
    return redirect('view_event')


def add_sponsor(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    event1 = Event.objects.all()
    if request.method == 'POST':
        eventid = request.POST['event']
        i = request.FILES['image']
        event = Event.objects.get(id=eventid)
        try:
            SponsorTbl.objects.create(event=event, sponsorimage=i)
            error = "no"
        except:
            error = "yes"
    d = {'event1': event1, 'error': error}
    return render(request, "add_sponsor.html", d)


def view_sponsor(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    sponsor = SponsorTbl.objects.all()
    d = {'sponsor': sponsor}
    return render(request, "view_sponsor.html", d)


def delete_sponsor(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = SponsorTbl.objects.get(id=pid)
    apoint.delete()
    return redirect('view_sponsor')


def add_category(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    if request.method == 'POST':
        cn = request.POST['cname']
        try:
            Category.objects.create(categoryname=cn)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, "add_category.html", d)


def view_category(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    cat = Category.objects.all()
    d = {'cat': cat}
    return render(request, "view_category.html", d)


def delete_category(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = Category.objects.get(id=pid)
    apoint.delete()
    return redirect('view_category')


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    user1 = UserSignup.objects.all()
    d = {'user1': user1}
    return render(request, "view_user.html", d)

def view_owner(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    user1 = OwnerSignup.objects.all()
    d = {'user1': user1}
    return render(request, "view_owner.html", d)

def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = UserSignup.objects.get(id=pid)
    apoint.delete()
    return redirect('view_user')


def delete_owner(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = OwnerSignup.objects.get(id=pid)
    apoint.delete()
    return redirect('view_owner')

def delete_booking(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    apoint = Booking.objects.get(id=pid)
    apoint.delete()
    return redirect('view_mybooking')


def about(request):
    return render(request, "about.html")


def usersignup(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        pas = request.POST['pwd']
        em = request.POST['email']
        con = request.POST['contact']
        address = request.POST['address']
        i = request.FILES['image']

        try:
            user = User.objects.create_user(username=em, password=pas, first_name=fn, last_name=ln)
            UserSignup.objects.create(user=user, mobile=con, image=i, address=address)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'usersignup.html', d)

def ownersignup(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        pas = request.POST['pwd']
        em = request.POST['email']
        con = request.POST['contact']
        address = request.POST['address']
        i = request.FILES['image']

        try:
            user = User.objects.create_user(username=em, password=pas, first_name=fn, last_name=ln)
            OwnerSignup.objects.create(owner=user, ownermobile=con, ownerimage=i, owneraddress=address)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'ownersignup.html', d)

def Logout(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    logout(request)
    return render(request, "index.html")


def book_now(request, pid):
    if not request.user.is_authenticated:
        return redirect('userlogin')
    error = ""
    event1 = Event.objects.get(id=pid)
    user = request.user
    userinfo = UserSignup.objects.get(user=user)
    if request.method == 'POST':
        p = request.POST['person']
        t = request.POST['total']
        try:
            Booking.objects.create(userinfo=userinfo, eventinfo=event1, person=p, total=t, status="pending",
                                   bookingdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'event1': event1, 'error': error}
    return render(request, "book_now.html", d)


def view_mybooking(request):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    user = request.user
    userinfo = UserSignup.objects.get(user=user)
    b = Booking.objects.filter(userinfo=userinfo)
    d = {'b': b}
    return render(request, "view_mybooking.html", d)


def bookingdetail_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    booking = Booking.objects.get(id=pid)
    return render(request, 'bookingdetail_user.html', locals())


def bookingdetail_admin(request, pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    booking = Booking.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        try:
            booking.status = status
            booking.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'bookingdetail_admin.html', locals())


def booking_request(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    b = Booking.objects.filter(status="pending")
    return render(request, "booking_request.html", locals())


def accepted_booking(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    b = Booking.objects.filter(status="Accept(Not Paid)")
    return render(request, "accepted_booking.html", locals())


def rejected_booking(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    b = Booking.objects.filter(status="Reject")
    return render(request, "rejected_booking.html", locals())


def all_booking(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    b = Booking.objects.all()
    return render(request, "all_booking.html", locals())


def confirmed_booking(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    b = Booking.objects.filter(status="Confirmed(Paid)")
    return render(request, "confirmed_booking.html", locals())


def contact(request):
    return render(request, "contact.html")


def innerhome(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    totalevents = Event.objects.all().count()
    totalsponsor = SponsorTbl.objects.all().count()
    totalcategory = Category.objects.all().count()
    totalnewbooking = Booking.objects.filter(status="pending").count()
    totalconfirmbooking = Booking.objects.filter(status="Confirmed(Paid)").count()
    allbooking = Booking.objects.all().count()
    totalusers = UserSignup.objects.all().count()
    return render(request, "innerhome.html", locals())


def edit_sponsor(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    event1 = Event.objects.all()
    sponsor = SponsorTbl.objects.get(id=pid)
    if request.method == 'POST':
        eventid = request.POST['event']
        event = Event.objects.get(id=eventid)
        sponsor.event = event
        try:
            sponsor.save()
            error = "no"
        except:
            error = "yes"
        try:
            i = request.FILES['image']
            sponsor.sponsorimage = i
            sponsor.save()
        except:
            pass
    return render(request, "edit_sponsor.html", locals())


def edit_category(request, pid):
    if not request.user.is_authenticated:
        return redirect('Login')
    error = ""
    category = Category.objects.get(id=pid)
    if request.method == 'POST':
        cn = request.POST['cname']
        try:
            category.categoryname = cn
            category.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "edit_category.html", locals())


def payment(request, pid):
    if not request.user.is_authenticated:
        return redirect('userLogin')
    booking = Booking.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        cardnumber = request.POST['cardnumber']
        cardex = request.POST['cardex']
        cvv = request.POST['cvv']
        try:
            booking.cardno = cardnumber
            booking.expirydate = cardex
            booking.cvv = cvv
            booking.status = "Confirmed(Paid)"
            booking.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'payment.html', locals())
