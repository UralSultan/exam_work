from django.shortcuts import render, redirect
from .models import GuestbookEntry
from .forms import SearchForm, GuestbookEntryForm

def index(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    search_form = SearchForm(request.GET)
    search_query = None
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        if search_query:
            entries = entries.filter(author_name__icontains=search_query)
    entry_form = GuestbookEntryForm()
    context = {
        'entries': entries,
        'search_form': search_form,
        'search_query': search_query,
        'entry_form': entry_form,
    }
    return render(request, 'entries/index.html', context)


def add_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm()
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    search_form = SearchForm()

    context = {
        'entries': entries,
        'search_form': search_form,
        'search_query': None,
        'entry_form': form,
    }
    return render(request, 'entries/index.html', context)
