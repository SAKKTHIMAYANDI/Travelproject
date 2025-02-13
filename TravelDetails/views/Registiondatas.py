# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from TravelDetails.forms.RegistionForm import RegistionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from TravelDetails.models.TravelRequest import TravelRequest
from django.contrib.auth.decorators import login_required

from django.contrib.admin.views.decorators import staff_member_required


@csrf_exempt
class Registiondatas(View):
    
    def Registion(request):
        if request.method == "POST":
            username = request.POST.get("username")
            print(username)
            email = request.POST.get("email")
            phone_no = request.POST.get("phone")
            gender = request.POST.get("gender")
            address = request.POST.get("address")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            
            print(gender)
            print(password1)
            if password1 == password2:
                try:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.profile.phone = phone_no
                    user.profile.gender = gender
                    user.profile.address = address
                    user.profile.save()

                    return JsonResponse({"message": "Account created successfully!", "status": "success"})
                    return redirect('login_page')
                
                except Exception as e:
                    return JsonResponse({"message": str(e), "status": "error"})
            else:
                return JsonResponse({"message": "Passwords do not match.", "status": "error"})
            
        return render(request,"website/registration.html")
    
    
    def login_page(request):
        
        if request.method == "POST":
            
            print("Login Form")
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            print("username: ",username)
            print("password: ",password)
            user = authenticate(request, username=username, password=password)
            print(user)
            
            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('all_taskview')
                    
                # return HttpResponse(username,password)
                else:
                    return redirect('travel_form')
            else:
                return render(request, 'website/login.html')

            
        else:
            print("get")
            return render(request,"website/login.html")
        
    
    def user_logout(request):
        logout(request)
        return redirect('login_page')
    
    @login_required
    def travel_form(request):
        if request.method == "POST":
            print("POST")
            full_name = request.POST.get("full_name")
            email = request.POST.get("email")
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            dob = request.POST.get('dob')
            age = request.POST.get('age')
            reason = request.POST.get('reason')
            form_location = request.POST.get('form_location')
            destination = request.POST.get('destination')
            travel_date = request.POST.get('travel_date')
            travel_mode = request.POST.get('travel_mode')
            booking_mode = request.POST.get('booking_mode')
            values = {"full_name ":full_name ,"email" :email,"phone" :phone,"dob" :dob,"gender":gender,"age" :age,"form_location" :form_location,"destination" :destination,"travel_date" :travel_date,"travel_mode" :travel_mode,"booking_mode" :booking_mode,}
            login_user = request.user
            user_id = login_user.id
            print("login.id: ",login_user.id)
            
            update_values = TravelRequest.objects.filter(user=login_user,phone_no=phone,email=email).first()
            
            # if update_values:
            #     # update_values.user=login_user,
            #     update_values.full_name=full_name,
            #     update_values.email=email,
            #     update_values.phone_no=phone,
            #     update_values.dob=dob,
            #     update_values.gender=gender,
            #     update_values.age=age,
            #     update_values.reason=reason,
            #     update_values.form_location=form_location,
            #     update_values.destination=destination,
            #     update_values.travel_date=travel_date,
            #     update_values.travel_mode=travel_mode,
            #     update_values.booking_mode=booking_mode,
            #     update_values.status="Pending",
                
            #     update_values.save()
            #     return redirect('travel_requests')
                
                
            # else:
            TravelRequest.objects.create(
                user=login_user,
                full_name=full_name,
                email=email,
                phone_no=phone,
                dob=dob,
                gender=gender,
                age=age,
                reason=reason,
                form_location=form_location,
                destination=destination,
                travel_date=travel_date,
                travel_mode=travel_mode,
                booking_mode=booking_mode,
                status="Pending",
            )
            return redirect('travel_requests')
        else:
            return render(request,"website/travelForm.html")

        
    @login_required
    def travel_requests(request):
        requests = TravelRequest.objects.filter(user=request.user)
        return render(request, 'website/travel_requests.html', {'requests': requests})
               
    
    @staff_member_required
    def all_taskview(request):
        requests = TravelRequest.objects.all()
        return render(request, 'website/admin_travel_list.html', {'requests': requests})
    
    @staff_member_required
    def update_travel_status(request, id, status):
        travel_request = TravelRequest.objects.get(id=id)
        travel_request.status = status
        travel_request.save()
        return redirect('view_userdetails',id=travel_request.id)

    def home(request):
        print(request.method)
        return render(request, 'website/base.html',)

    def view_userdetails(request,id):
        print(request.method)
        traveldetails = TravelRequest.objects.filter(id=id)
        return render(request, 'website/view_dateils.html', {'traveldetails': traveldetails})
    
        