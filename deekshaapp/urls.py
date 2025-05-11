from django.urls import path
from deekshaapp import views


urlpatterns = [
    
    path('',views.index,name='index'),
    path('selfassessment',views.assessment,name="assessment"),
    path('selfassessment/<str>/',views.assessmentquestions,name="assessmentquestions"),
    path('assessmentsubmit/',views.assessmentsubmit,name="assessmentsubmit"),
    path('pdp/',views.pdp,name="pdp"),
    path('createprofile/',views.createprofile,name='createprofile'),
    path('updateprofile/<str>',views.updateprofile,name='updateprofile'),
    path('advisorsupport/',views.Advisorsupport,name='Advisorsupport'),
    path('dairyrecords/',views.dairyrecords,name='dairyrecords'),
    path('submittask/',views.submittask,name='submittask'),


    
]