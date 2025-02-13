from django.db import models
from django.contrib.auth.models import User


class TravelRequest(models.Model):
    
    class Meta:
        verbose_name = "TravelRequest"
        verbose_name_plural = "TravelRequests"


    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    mode_choices = [("by train","By Train"),("by flight","By Flight"),("by bus","By Bus")]
    gender_choices = [('male','Male'),('female','Female')]
    booking_choices = [("self","Self"),("travel desk","Travel Desk")]
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    full_name = models.CharField(verbose_name="Full Name", max_length=255, default="")
    dob = models.DateField(default="1967-02-12",)
    age = models.CharField(verbose_name="Age",max_length=15,default="10")
    phone_no = models.CharField(verbose_name="Phone", default=0,max_length=50)
    email = models.EmailField(verbose_name="Email", default="john@gmail.com",max_length=254)
    form_location = models.CharField(verbose_name = "From Location", max_length=255, default="salem")
    destination = models.CharField(max_length=255)
    reason = models.TextField()
    travel_date = models.DateField(default="2025-02-12")
    gender = models.CharField(max_length=15,choices=gender_choices,default="male")
    travel_mode = models.CharField(max_length=20, choices=mode_choices, default='by flight')
    booking_mode = models.CharField(max_length=20, choices=booking_choices, default='self')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    is_complete = models.BooleanField(verbose_name="Is Completed",default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.destination}"