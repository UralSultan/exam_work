from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import GuestbookEntry
from .forms import SearchForm, GuestbookEntryForm, DeleteEntryForm


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
        'add_entry_url': reverse('add_entry'),  # ВАЖНО для form_action
    }
    return render(request, 'entries/index.html', context)


def add_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
        search_form = SearchForm()
        context = {
            'entries': entries,
            'search_form': search_form,
            'search_query': None,
            'entry_form': form,  # форма с ошибками
            'add_entry_url': reverse('add_entry'),
        }
        return render(request, 'entries/index.html', context)
    return redirect('index')


def edit_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GuestbookEntryForm(instance=entry)

    context = {
        'form': form,
        'form_action': request.path,
        'title': 'Редактировать запись',
        'submit_label': 'Сохранить',
    }
    return render(request, 'entries/edit_entry.html', context)

def delete_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    if request.method == 'POST':
        form = DeleteEntryForm(request.POST)
        if form.is_valid():
            entered_email = form.cleaned_data['author_email']
            if entered_email == entry.author_email:
                entry.delete()
                return redirect('index')
            else:
                form.add_error('author_email', 'Email не совпадает с email автора записи.')
    else:
        form = DeleteEntryForm()

    context = {
        'entry': entry,
        'form': form,
    }
    return render(request, 'entries/delete_entry.html', context)