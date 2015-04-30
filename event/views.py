from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from djqscsv import render_to_csv_response



from .models import Attendee, Attendance, User


def start(request):
	if request.method == 'POST':
		try:
			request.session['user_full_name'] = request.POST['user_full_name']
			request.session['user_email'] = request.POST['user_email']
			user = User(full_name=request.POST['user_full_name'], email=request.POST['user_email'])
			user.save()
		except KeyError, e:
			return render(request, 'event/start.html', {'error_msg':'KeyError'})
		else:
			return HttpResponseRedirect(reverse('event:data_entry'))
	return render(request, 'event/start.html')

def logout(request):
	request.session.flush()
	return HttpResponseRedirect(reverse('event:start'))


class DataEntryView(generic.ListView):
	template_name = 'event/entry_page.html'
	context_object_name = 'entry_list'
	queryset = Attendee.objects.order_by('last_name', 'first_name')



def save_data(request):
	if request.method == 'POST':
		try:
			entries = request.POST.getlist('showed_up_list')
		except KeyError:
			# return render(request, 'event/entry_page.html', {'error_msg':'KeyError'})
			return HttpResponseRedirect(reverse('event:data_entry'))
		else:
			if not isinstance(entries, list):
				entries = [entries]
			for entry in entries:
				attendee = get_object_or_404(Attendee, pk=int(entry))
				print attendee.first_name, attendee.showed_up
				if attendee.showed_up != True:
					attendee.showed_up = True
					attendee.input_by = request.session.get('user_email') or ''
					attendee.save()
				# attend_record = Attendance(attendee=attendee, showed_up=True, input_by=request.session.get('user_email'))
				# attend_record.save()
			return HttpResponseRedirect(reverse('event:data_entry'))

def save_and_add(request):
	if request.method == 'POST':
		try:
			entries = request.POST['showed_up_list']
		except KeyError:
			return redirect('event:attendee_add')
		else:
			if not isinstance(entries, list):
				entries = [entries]
			for entry in entries:
				attendee = get_object_or_404(Attendee, pk=int(entry)) 
				if attendee.showed_up != True:
					attendee.showed_up = True
					attendee.input_by = request.session.get('user_email')
					attendee.save()
	return redirect('event:attendee_add')


class AttendeeCreate(CreateView):
	model = Attendee
	success_url = reverse_lazy('event:data_entry')
	fields = [
		'first_name',
		'last_name',
		'email',
		'address',
		'city',
		'state',
		'zipcode',
		'home_phone',
		'cell_phone',
		'showed_up',
		'input_by',
	]



class AttendeeUpdate(UpdateView):
	model = Attendee
	success_url = reverse_lazy('event:data_entry')
	template_name_suffix = '_update_form'
	fields = [
		'first_name',
		'last_name',
		'email',
		'address',
		'city',
		'state',
		'zipcode',
		'home_phone',
		'cell_phone',
		'showed_up',
		'input_by',
	]

def csv_export(request):
	if request.method == 'POST':
		try:
			if request.POST['export_password'] == 'evergreen':
				qs = Attendee.objects.all()
				return render_to_csv_response(qs)
		except:
			pass
	return render(request, 'event/export.html')




# class DataEntryView(generic.ListView):
# 	template_name = 'event/entry_page.html'
# 	context_object_name = 'entry_list'

# 	def get_queryset(self):
# 		# all_joined = Attendance.objects.select_related('attendee').all()
# 		sql_query = """
# 			select a.id, a.first_name, a.last_name, a.email, b.showed_up
# 			from event_attendee a 
# 			left join (
# 					select * from event_attendance order by created_at desc
# 				)
# 			 b on a.id = b.attendee_id
# 			group by a.id
# 		"""
# 		all_joined = Attendee.objects.raw(sql_query)
# 		return all_joined