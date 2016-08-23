from django.contrib import admin
from company.models import Company, Branch, Department, Division, Designation, Shift, WeekOff, Grade, BankDetails

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','code','telephone','pan','tan')
    search_fields = ['code','name']

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','code','company')
    list_filter = ('company',)
    search_fields = ['code','name']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','code','company')
    list_filter = ('company',)
    search_fields = ['code','name']

class DivisionAdmin(admin.ModelAdmin):
    list_display = ('code','name','department')
    list_filter = ('department',)
    search_fields = ['code','name']

class DesignationAdmin(admin.ModelAdmin):
    list_display = ('code','name','company','department','division')
    list_filter = ('company','department','division')
    search_fields = ['code','name']

class ShiftAdmin(admin.ModelAdmin):
    list_display = ('code','name','company')
    list_filter = ('company',)
    search_fields = ['code','name']

class WeekOffAdmin(admin.ModelAdmin):
    list_display = ('code','name','company')
    list_filter = ('company',)
    search_fields = ['code','name']

class GradeAdmin(admin.ModelAdmin):
    list_display = ('code','name','company','department','division','designation')
    list_filter = ('company','department','division','designation')
    search_fields = ['code','name']

class BankDetailsAdmin(admin.ModelAdmin):
    list_display = ('name','company','branch','ifsc_code','primary')
    list_filter = ('primary','company')
    search_fields = ['name']

admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(WeekOff, WeekOffAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(BankDetails, BankDetailsAdmin)