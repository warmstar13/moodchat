from django.shortcuts import render
from .forms import ChatUploadForm

def main_page(request):
    """Render the main page."""
    return render(request, 'website/main_page.html')

def upload_chat(request):
    if request.method == 'POST':
        form = ChatUploadForm(request.POST, request.FILES)
        if form.is_valid():
            chat_file = request.FILES['chat_file']

            analysis = analyze_chat(chat_file)
            return render(request, 'website/result.html', {'analysis': analysis})
    else:
        form = ChatUploadForm()
    return render(request, 'website/upload.html', {'form': form})

def analyze_chat(chat_file):
    return "dummy analysis"