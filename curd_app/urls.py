from django.conf.urls import url
from .views import createuser,updateuser,listuser,deleteuser,singleuser


urlpatterns = [
    url(r'^user/createuser', createuser.as_view()),
    url(r'^user/update',updateuser.as_view()),
    url(r'^user/listuser',listuser.as_view()),
    url(r'^user/delete',deleteuser.as_view()),
    url(r'^user/single',singleuser.as_view())
]