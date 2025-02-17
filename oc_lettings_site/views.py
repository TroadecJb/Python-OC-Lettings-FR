from django.shortcuts import render
from sentry_sdk import capture_exception


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,# noqa: E501
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.# noqa: E501
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.# noqa: E501
def index(request):
    """
    Render index. Default homepage.
    """
    return render(request, "index.html")


def error_404(request, exception):
    """
    Render 404.html if url path did not match.

    Send exception log to sentry
    """
    capture_exception(exception)
    return render(request, "404.html", status=404)
