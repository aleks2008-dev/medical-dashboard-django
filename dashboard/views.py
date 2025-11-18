from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from .models import Doctor, User, Appointment, Room
from datetime import datetime, timedelta

@staff_member_required
def dashboard_stats(request):
    """Dashboard with medical statistics"""
    
    # Basic counts
    total_doctors = Doctor.objects.count()
    total_patients = User.objects.filter(role='user').count()
    total_appointments = Appointment.objects.count()
    total_rooms = Room.objects.count()
    
    # Recent appointments (last 7 days)
    week_ago = datetime.now() - timedelta(days=7)
    recent_appointments = Appointment.objects.filter(
        datetime__gte=week_ago
    ).count()
    
    # Popular specializations
    specializations = Doctor.objects.values('specialization').annotate(
        count=Count('specialization')
    ).order_by('-count')[:5]
    
    # Today's appointments
    today = datetime.now().date()
    today_appointments = Appointment.objects.filter(
        datetime__date=today
    ).count()
    
    context = {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'total_rooms': total_rooms,
        'recent_appointments': recent_appointments,
        'today_appointments': today_appointments,
        'specializations': specializations,
    }
    
    return render(request, 'dashboard/stats.html', context)