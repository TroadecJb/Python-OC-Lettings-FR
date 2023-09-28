from django.shortcuts import render
from .models import Profile
from sentry_sdk import capture_exception


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc # noqa: E501
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d# noqa: E501
def index(request):
    """
    Display list of profiles :model:`profiles.Profile`.

    **Context**

    ``profiles_list``
        list of instance :model:`profiles.Profile`.

    **Template**

    :template:`profiles/index.html`
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,# noqa: E501
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males# noqa: E501
def profile(request, username):
    """
    Display an individual profile :model:`profiles.Profile`.

    **Args**
    username:
        username from table profiles_profile
    
    **Context**

    ``profile``
        instance of :model:`profiles.Profile`.

    **Template**

    :template:`profiles/profile.html`
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist as err:
        capture_exception(err)
        return render(
            request,
            "500.html",
            context={"message": "Profile not found"},
            status=500,
        )
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
