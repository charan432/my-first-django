from django.urls import path
from . import views

urlpatterns = [
    # Routing for function based view
    #path('', views.home, name="home"),
    path('search/', views.search, name='search'),
    #path('detail/<int:id>', views.detail, name='detail'),


    # routing for class based view
    # Default home page is home page
    path('', views.HomePageView.as_view(), name="home"),
    path('home', views.HomePageView.as_view(), name="home"),
    path('detail/<int:pk>', views.DetailPageView.as_view(), name='detail'),
    path('contacts/create', views.ContactCreateView.as_view(), name='create'),
    path('contacts/update/<int:pk>',
         views.ContactUpdateView.as_view(), name='update'),
    path('contacts/delete/<int:pk>',
         views.ContactDeleteView.as_view(), name='delete'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]
