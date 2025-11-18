from django.contrib import admin
from .models import Doctor, User, Room, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'specialization', 'category', 'experience_years', 'age']
    list_filter = ['specialization', 'category']
    search_fields = ['name', 'surname', 'specialization']
    readonly_fields = ['id']
    ordering = ['surname', 'name']
    
    def has_add_permission(self, request):
        return False  # Read-only access
    
    def has_delete_permission(self, request, obj=None):
        return False  # Read-only access

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'role', 'age', 'disabled']
    list_filter = ['role', 'disabled']
    search_fields = ['name', 'surname', 'email']
    readonly_fields = ['id']
    ordering = ['surname', 'name']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['number']
    ordering = ['number']
    readonly_fields = ['id']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'get_doctor_name', 'get_patient_name', 'get_room_number']
    list_filter = ['datetime']
    date_hierarchy = 'datetime'
    readonly_fields = ['id', 'doctor_id', 'user_id', 'room_id']
    ordering = ['-datetime']
    
    def get_doctor_name(self, obj):
        doctor = obj.get_doctor()
        return f"Dr. {doctor.name} {doctor.surname}" if doctor else "Unknown Doctor"
    get_doctor_name.short_description = 'Doctor'
    
    def get_patient_name(self, obj):
        patient = obj.get_patient()
        return f"{patient.name} {patient.surname}" if patient else "Unknown Patient"
    get_patient_name.short_description = 'Patient'
    
    def get_room_number(self, obj):
        room = obj.get_room()
        return f"Room {room.number}" if room else "Unknown Room"
    get_room_number.short_description = 'Room'
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

# Customize admin site
admin.site.site_header = "Medical Dashboard"
admin.site.site_title = "Medical Admin"
admin.site.index_title = "Medical Center Administration"