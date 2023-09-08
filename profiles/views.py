from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc # noqa: E501
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d# noqa: E501
def index(request):
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,# noqa: E501
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males# noqa: E501
def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
