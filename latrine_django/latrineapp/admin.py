from django.contrib import admin

# Register your models here.
from .models import * 
 
admin.site.register(Place) 
admin.site.register(Resource) 
admin.site.register(Feedback) 
