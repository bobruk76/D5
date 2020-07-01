from django.http import HttpResponse
from django.template import loader
from p_library.models import Book, Publisher, Author
from django.shortcuts import redirect

from p_library.forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('p_library:author_list')
    template_name = 'author_edit.html'

class AuthorList(ListView):
    model = Author
    template_name = 'authors_list.html'

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def books_list(request):
    template = loader.get_template('books.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def books_publ(request):
    template = loader.get_template('publishing.html')

    publishers = Publisher.objects.all()
    data = {
        "publishers": publishers,
    }
    return HttpResponse(template.render(data, request))