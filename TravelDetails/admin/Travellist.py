from django.contrib import admin
from django.urls import reverse
from TravelDetails.models.TravelRequest import TravelRequest
from TravelDetails.forms.TravelRequestForm import TravelRequestForm
from django.utils.html import format_html

# Register your models here.

class TravellistAdmin(admin.ModelAdmin):
    
    form = TravelRequestForm
    
    list_display_links = None
    list_per_page = 10
    ordering = ("id",)
    
    def action_button(self, obj):
        id = obj.id
        
        approve_url = f'{reverse("update_travel_status", args=[id, "Approved"])}'
        reject_url = f'{reverse("update_travel_status", args=[id, "Rejected" if obj.deleted_at else "Active"])}'
        
        # Generate the buttons HTML
        approve_html = format_html('<a href="{}">Approve</a>', approve_url)
        reject_html = format_html('<a href="{}">Reject</a>', reject_url)
        buttons_html = approve_html + " " + reject_html
        # buttons_html = edit_button_html 
        
        return format_html(buttons_html)
    action_button.short_description = 'Action'
    
    list_display = ["full_name","form_location","destination","travel_date","travel_mode","booking_mode","status","action_button"]
    
admin.site.register(TravelRequest,TravellistAdmin)
# admin.site.register(AssignTask, AssignTaskAdmin)