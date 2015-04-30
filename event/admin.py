from django.contrib import admin

from .models import Attendee, Attendance, User

# using import-export module
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin


class AttendeeResource(resources.ModelResource):

    class Meta:
    	import_id_fields = ['id']
        model = Attendee
        fields = [
        	'id',
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



class AttendeeAdmin(ImportExportModelAdmin):
    resource_class = AttendeeResource
    pass

# class AttendeeAdmin(admin.ModelAdmin):
# 	fields = [
# 		'my_campaign_id',
# 		'first_name',
# 		'last_name',
# 		'address',
# 		'city',
# 		'state',
# 		'zipcode',
# 		'email',
# 		'home_phone',
# 		'cell_phone',
# 		'showed_up',
# 		'input_by',
# 	]


admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(User)