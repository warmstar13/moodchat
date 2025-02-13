from django.shortcuts import render


def main_page(request):
    """Render the main page."""
    return render(request, 'website/main_page.html')

