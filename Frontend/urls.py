from django.urls import path
from Frontend import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('registration/',views.registration,name="registration"),

    path('savereg/', views.savereg, name="savereg"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    path('userlogin',views.userlogin,name="userlogin"),
    path('user_reg', views.user_reg, name="user_reg"),
    path('displayemployee/',views.displayemployee,name="displayemployee"),
    path('profilehome/',views.profilehome,name="profilehome"),
    path('leave',views.leave,name="leave"),
    path('new_leave_request/',views.new_leave_request,name="new_leave_request"),





]