from django.contrib import admin

from .models import Attendee, Attendance


class AttendanceInLine(admin.TabularInline):
	model = Attendance

class AttendeeAdmin(admin.ModelAdmin):
	fields = [
		'my_campaign_id',
		'first_name',
		'last_name',
		'address',
		'city',
		'state',
		'zipcode',
		'email',
		'home_phone',
		'cell_phone',
		'showed_up',
		'input_by',
	]
	
	inlines = [
		AttendanceInLine,
	]

admin.site.register(Attendee, AttendeeAdmin)