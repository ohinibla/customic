from api.models import Mockup, Task
from api.utils import draw_to_image
from celery import shared_task
from celery.result import states
from django.core.files import File


@shared_task(bind=True)
def generate_mockup_task(self, shirt_color, text, text_color, font):
    t = Task.objects.get(task_id=self.request.id)  # type: ignore
    try:
        for color in shirt_color:
            img = draw_to_image(
                shirt_color=color,
                text=text,
                fill=text_color,
                font=font,
            )
            x = Mockup.objects.create(  # type: ignore
                text=text,
                font=font,
                text_color=text_color,
                image=File(img, f"generated-{color}.png"),
                shirt_color=color,
                task_id=t.id,
            )

    except Exception:
        t.status = states.FAILURE
        raise

    else:
        t.status = states.SUCCESS

    finally:
        t.save()
