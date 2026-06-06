from django.shortcuts import render
from .models import GuestbookEntry
from .forms import SearchForm


def index(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    search_form = SearchForm(request.GET)
    search_query = None
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            entries = entries.filter(author_name__icontains=search_query)
    context = {
        'entries': entries,
        'search_form': search_form,
        'search_query': search_query,
    }
    return render(request, 'entries/index.html', context)
