from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_exception


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat massa. Integer est nunc, pulvinar a# noqa: E501
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque# noqa: E501
def index(request):
    """
    Display list of lettings :model:`lettings.Letting`.

    **Context**

    ``lettings_list``
        list of instance :model:`lettings.Letting`.

    **Template**

    :template:`lettings/index.html`
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae efficitur# noqa: E501
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.# noqa: E501
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.# noqa: E501
def letting(request, letting_id):
    """
    Display an individual letting :model:`lettings.Letting`.

    **Args**
    lettings_id:
        pk from table lettings_letting

    **Context**

    ``letting``
        title :model:`lettings.Letting.title`.
        address :model:`lettings.Letting.address`.

    **Template**

    :template:`lettings/letting.html`
    """
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist as err:
        capture_exception(err)
        return render(
            request,
            "500.html",
            context={"message": "Letting not found"},
            status=500,
        )
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
