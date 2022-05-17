from django.urls import path
from . import views
from .views import RegisterAPI, SalaryUser
from django.urls import path
from .views import login

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),

	path('salary-list/', views.salaryList, name="salary-list"),
	path('salary-create/', views.salaryCreate, name="salary-create"),
	path('salary-update/<str:pk>/', views.salaryUpdate, name="salary-update"),
	path('salary-delete/<str:pk>/', views.salaryDelete, name="salary-delete"),

    # Category routes
	path('category-list/', views.categoryList, name="category-list"),
	path('category-create/', views.categoryCreate, name="category-create"),
	path('category-update/<str:pk>/', views.categoryUpdate, name="category-update"),
	path('category-delete/<str:pk>/', views.categoryDelete, name="category-delete"),


    path('depency-list/', views.depencyList, name="depency-list"),
	path('depency-detail/<str:pk>/', views.depencyDetail, name="depency-detail"),
	path('depency-add/', views.depencyAdd, name="depency-add"),
	
	 #Register
    path('register/', RegisterAPI.as_view(), name='register'),
	path('user-salary/', SalaryUser.as_view(), name='userS'),


	#Dashbord
	path('dashboard/', views.Dashboard, name="dashbord.get"),
	path('login/', login),
	path('logout/', views.logout)
	

	
]
