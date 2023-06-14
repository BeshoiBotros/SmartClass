
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('doctor/', include('Doctor.urls')),
    path('organization/', include('Organization.urls')),
    path('student/', include('Student.urls')),
    path('subject/', include('Subject.urls')),
    path('teacher-assest/', include('T_assest.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
