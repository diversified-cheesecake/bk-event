from django.db import models


class User(models.Model):
	full_name = models.CharField(max_length=245, blank=True)
	email = models.CharField(max_length=245)

	def __unicode__(self):
		return '{} {}'.format(self.full_name, self.email)


class Attendee(models.Model):
	my_campaign_id = models.BigIntegerField(null=True, blank=True)
	first_name = models.CharField(max_length=200, blank=True)
	last_name = models.CharField(max_length=200, blank=True)
	address = models.CharField(max_length=245, blank=True)
	city = models.CharField(max_length=200, blank=True)
	state = models.CharField(max_length=100, blank=True)
	zipcode = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=245, blank=True)
	home_phone = models.CharField(max_length=100, blank=True)
	cell_phone = models.CharField(max_length=100, blank=True)
	showed_up = models.BooleanField(default=False)
	input_by = models.CharField(max_length=245, blank=True)
	created_at = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return '{} {}'.format(self.first_name, self.last_name)


class Attendance(models.Model):
	attendee = models.ForeignKey(Attendee)
	showed_up = models.BooleanField()
	input_by = models.CharField(max_length=245, blank=True)
	created_at = models.DateField(auto_now_add=True)

