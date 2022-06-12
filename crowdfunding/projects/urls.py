from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('latestProjects/', views.LatestProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('pledgeTypes/', views.PledgeTypeList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('myProjects/', views.MyProjectList.as_view()),
    path('myPledges/', views.MyPledgeList.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)