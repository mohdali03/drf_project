from django.urls import path
from .views import snippetsCreateList, snippetsDetail

urlpatterns = [
    path('snippets/', snippetsCreateList.as_view()),
    path('snippets/<int:pk>', snippetsDetail.as_view()),
    # path('create', create, name="create")
]