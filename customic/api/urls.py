from api import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path(
            "mockups/generate/",
            views.GenerateMockupAPIView.as_view(),
            name="mockup-generate2",
        ),
        path(
            "tasks/<slug:task_id>/",
            views.TaskRetrieveAPIView.as_view(),
        ),
        path(
            "mockups/",
            views.MockupListAPIView.as_view(),
        ),
    ]
)
