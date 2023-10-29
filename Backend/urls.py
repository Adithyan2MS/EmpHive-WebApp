from django.urls import path
from Backend import views


urlpatterns = [

    path('index/', views.index, name="index"),

    path('displayregister/', views.displayregister, name="displayregister"),
    path('editregister/<int:dataid>', views.editregister, name="editregister"),
    path('updateregister/<int:dataid>', views.updateregister, name="updateregister"),
    path('deleteregister/<int:dataid>', views.deleteregister, name="deleteregister"),
    path('send_email_with_link', views.send_email_with_link, name="send_email_with_link"),
    path('displayuser/',views.displayuser,name="displayuser"),
    path('employee/',views.employee,name="employee"),
    path('saveemp/',views.saveemp,name="saveemp"),
    path('dellog/<int:dataid>',views.dellog,name="dellog"),
    path('leaveRequests',views.leaveRequests,name="leaveRequests"),
    path('accept_leave_request/<int:dataId>',views.accept_leave_request,name="accept_leave_request"),
    path('delete_leave_request/<int:dataId>',views.delete_leave_request,name="delete_leave_request"),





]