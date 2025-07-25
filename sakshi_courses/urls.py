from django.urls import path
from.import views
urlpatterns=[
    path("signup/",views.sakshi_lmsSignupUser.as_view()),
    path("getAllUser/",views.sakshi_lmsGetUserDetails.as_view()),
    path("updateEmail/",views.sakshi_lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.sakshi_lmsDeleteUser.as_view())
]