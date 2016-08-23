from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_excess(value):
    if len(value)>9:
        raise ValidationError(u'%s is too long' % value)

class Company(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters ONLY',validators=[validate_excess])
    name = models.CharField(max_length=250)
    address = models.TextField()
    telephone = models.CharField(max_length=250)
    logo = models.ImageField(null=True,blank=True)
    pan = models.CharField(null=True,blank=True,max_length=250)
    tan = models.CharField(null=True,blank=True,max_length=250)
    pf_code = models.CharField(null=True,blank=True,max_length=250)
    pt_certificate_no = models.CharField(null=True,blank=True,max_length=250)
    esi_code = models.CharField(null=True,blank=True,max_length=250)
    license_no = models.CharField(null=True,blank=True,max_length=250)
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class Branch(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters ONLY',validators=[validate_excess])
    name = models.CharField(max_length=250)
    address = models.TextField()
    company = models.ForeignKey(Company)
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class Department(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters ONLY',validators=[validate_excess])
    name = models.CharField(max_length=250)
    address = models.TextField()
    company = models.ForeignKey(Company)
    info = models.TextField()
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'


class Division(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters ONLY',validators=[validate_excess])
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department)
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class Designation(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters only',validators=[validate_excess])
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company)
    department = models.ForeignKey(Department)
    division = models.ForeignKey(Division,null=True,blank=True)
    no_of_positions = models.PositiveIntegerField('No of Positions',default=1)
    info = models.TextField('Additional Info')
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class Grade(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters only',validators=[validate_excess])
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company)
    department = models.ForeignKey(Department)
    division = models.ForeignKey(Division,null=True,blank=True)
    designation = models.ForeignKey(Designation,null=True,blank=True)
    info = models.TextField('Additional Info')
    inactive = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class Shift(models.Model):

    W_O = (('1','Sunday'),
           ('2','Monday'),
           ('3','Tuesday'),
           ('4','Wednesday'),
           ('5','Thursday'),
           ('6','Friday'),
           ('7','Saturday'),
           )

    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters only',validators=[validate_excess])
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company)
    wef = models.DateField('With effect from')
    session_two_days = models.BooleanField('Session across 2 days')
    week_off = models.CharField('Shift week off',max_length=250,choices=W_O)
    total_working_hours = models.TimeField()
    min_working_half = models.TimeField('Minimum working hours for half day',null=True,blank=True)
    max_working_full = models.TimeField('Maximum working hours for full day',null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class WeekOff(models.Model):

    W_O = (('1','Sunday'),
           ('2','Monday'),
           ('3','Tuesday'),
           ('4','Wednesday'),
           ('5','Thursday'),
           ('6','Friday'),
           ('7','Saturday'),
           )

    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters only',validators=[validate_excess])
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company)
    common_week_off = models.CharField('Common week off',max_length=250,choices=W_O)
    first_week_off = models.DateField('First Weekend',null=True,blank=True)
    second_week = models.DateField('Second Weekend',null=True,blank=True)
    third_week = models.DateField('Third Weekend',null=True,blank=True)
    fourth_week = models.DateField('Fourth Weekend',null=True,blank=True)
    fifth_week = models.DateField('Fifth Weekend',null=True,blank=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'

class BankDetails(models.Model):
    code = models.CharField(max_length=250,help_text='Please enter up to 9 characters only',validators=[validate_excess])
    name = models.CharField(max_length=250)
    company = models.ForeignKey(Company)
    account_no = models.CharField(max_length=250)
    branch = models.CharField(max_length=250)
    ifsc_code = models.CharField(max_length=250)
    primary = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name+' ( '+self.code+' )'