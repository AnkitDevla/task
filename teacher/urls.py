from . import views
from django.urls import path,include
# from teacher.views import teacher_api
# from teacher.views import TeacherViewSet,AttendanceViewSet

urlpatterns = [
    # path('teacher/',TeacherViewSet.as_view({'get': 'list'})),
    # path('attendance/',AttendanceViewSet.as_view({'get': 'list'})),
    # path('teachers/', teacher_api.as_view()),

    path('teachers/', views.teacher_post),
    path('teachers/<int:id>/',  views.teacher_detalis),
]
