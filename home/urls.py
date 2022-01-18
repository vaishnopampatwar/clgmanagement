from django.urls import path, include
from . import adminViews, StaffViews

from studmanagement import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('demo/', views.showDemopage),
    path('', views.showLoginpage),
    path('doLogin', views.doLogin),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('get_user_details', views.get_user_details, name="get_user_details"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('admin_home',adminViews.admin_home, name="admin_home"),
    path('add_staff/', adminViews.add_staff, name="add_Staff"),
    path('add_staff_save', adminViews.add_staff_save, name="add_staff_save"),
    path('add_course/', adminViews.add_course, name="add_course"),
    path('add_course_save', adminViews.add_course_save, name="add_course_save"),



    path('staff_home/', StaffViews.staff_home, name="staff_home"),
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
