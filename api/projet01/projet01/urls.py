"""
URL configuration for projet01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from serieTracker import api

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-auth/signup/', api.SignUpView.as_view(), name='signup'),
    path('api-auth/login/', api.LoginView.as_view(), name='login'),
    path('api-auth/logout/', api.LogoutView.as_view(), name='logout'),
    path('api-auth/user/', api.UserDetailView.as_view(), name='user-detail'),
    path('series/', api.SerieCreateView.as_view(), name='serie-create'),
    path('series/active/', api.ActiveSerieListView.as_view(), name='series-active-list'),
    path('series/archive/', api.ArchiveSerieListView.as_view(), name='series-archive-list'),
    path('series/<int:id>/', api.SerieDetailView.as_view(), name='serie-detail'),
    path('series/<int:id>/update/', api.SerieInfoUpdateView.as_view(), name='serie-title-update'),
    path('series/<int:pk>/update-episodes/', api.SerieEpisodesUpdateView.as_view(), name='serie-episodes-update'),
    path('series/<int:pk>/archive/', api.ArchiveSerieView.as_view(), name='archive-serie'),
    path('series/suivies/', api.FollowedSeriesList.as_view(), name='series-suivies'),
    path('series/suivies-create/', api.FollowedSeriesCreateView.as_view(), name='suivi-create'),
    path('series/suivies-delete/<int:pk>/', api.FollowedSeriesDestroyView.as_view(), name='suivi-delete'),
    path('series/suivies/<int:id>/', api.SerieWithEpisodesRetrieveView.as_view(), name='series-with-episodes'),
    path('series/vu/create/', api.VuCreateView.as_view(), name='vu-create'),
    path('series/vu/delete/<int:pk>/', api.VuDeleteView.as_view(), name='vu-delete'),
    path('partage/', api.UtilisateurListView.as_view(), name='partage-utilisateur-list'),
    path('partage/add/<int:user_id>/', api.AddUserToShareList.as_view(), name='add_user_to_share_list'),
    path('partage/remove/<int:user_id>/', api.RemoveUserFromShareList.as_view(), name='remove_user_from_share_list'),
    path('partage/<int:user_id>/', api.UserSeriesListAPIView.as_view(), name='user-series-list'),
]
