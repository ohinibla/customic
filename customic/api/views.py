from api.models import Mockup, Task
from api.paginations import MockupPagination
from api.permissions import IsOwner
from api.serializers import MockupSerializer, TaskCreateSerializer, TaskSerializer
from api.tasks import generate_mockup_task
from celery.result import states
from rest_framework import filters, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()  # type: ignore
    serializer_class = TaskSerializer
    lookup_field = "task_id"
    permission_classes = [IsAuthenticated, IsOwner]


class MockupListAPIView(generics.ListAPIView):
    queryset = Mockup.objects.all()  # type: ignore
    serializer_class = MockupSerializer
    pagination_class = MockupPagination
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "text",
        "font",
        "text_color",
        "shirt_color",
    ]


class GenerateMockupAPIView(generics.CreateAPIView):
    queryset = Mockup.objects.all()  # type: ignore
    serializer_class = MockupSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task_obj = Task.objects.create(status=states.PENDING)
        generate_mockup_task.apply_async(
            kwargs={**serializer.validated_data}, task_id=str(task_obj.task_id)
        )  # type: ignore

        task_serializer = TaskCreateSerializer(instance=task_obj)
        headers = self.get_success_headers(task_serializer.data)
        return Response(
            task_serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
