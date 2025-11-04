from api.models import Mockup, Shirts, Task
from rest_framework import serializers


class ShirtColorsChoicesField(serializers.MultipleChoiceField):
    def to_internal_value(self, data):
        return list(super().to_internal_value(data))

    def to_representation(self, value):
        if isinstance(value, str):
            return value
        return "".join(super().to_representation(value))


class MockupSerializer(serializers.ModelSerializer):
    shirt_color = ShirtColorsChoicesField(
        choices=Shirts.choices,
        required=False,
        default=["black", "blue", "yellow", "white"],
    )

    class Meta:
        model = Mockup
        fields = [
            "id",
            "text",
            "font",
            "text_color",
            "shirt_color",
            "image",
            "created_at",
        ]

        read_only_fields = [
            "image",
        ]

        extra_kwargs = {
            "text_color": {"initial": "000000", "default": "000000"},
            "font": {"initial": "Arial", "default": "Arial"},
            "shirt_color": {"initial": Shirts.choices},
        }


class MockupShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mockup
        fields = [
            "created_at",
            "image",
        ]


class TaskSerializer(serializers.ModelSerializer):
    results = MockupShortSerializer(source="mockups", many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "status",
            "task_id",
            "results",
        ]

        read_only_fields = [
            "status",
            "task_id",
            "results",
        ]


class TaskCreateSerializer(TaskSerializer):
    def to_representation(self, instance):
        return {
            "status": instance.status,
            "task_id": instance.task_id,
            "message": "ساخت تصویر آغاز شد" if instance.status == "PENDING" else "",
        }
