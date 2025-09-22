from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="dashboard"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('forgot-password/', forgot_password_view, name='forgot-password'),
    path('reset-password/<str:token>/', reset_password_view, name='reset-password'),
    path('logout/', logout_view, name='logout'),
    path("notifications/clear-all/", views.clear_all_notifications, name="clear_all_notifications"),
    path("notifications/mark-read/", views.mark_notifications_as_read, name="mark_notifications_as_read"),

]
