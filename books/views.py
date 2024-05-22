import requests
from django.shortcuts import render, redirect
from .models import BookRecommendation
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    query = request.GET.get('q', 'Django')  # Default search query
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=40'
    response = requests.get(api_url)
    books = response.json().get('items', [])
    context = {
        'books': books,
    }
    return render(request, 'home.html', context)

def show_recommendations(request):
    recommendations = BookRecommendation.objects.all()
    context = {
        'recommendations': recommendations,
    }
    return render(request,'recommendations.html',context)

@csrf_exempt
def add_recommendation(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        api_url = f'https://www.googleapis.com/books/v1/volumes/{book_id}'
        response = requests.get(api_url)
        book_data = response.json()

        book_recommendation, created = BookRecommendation.objects.get_or_create(
            google_books_id=book_id,
            defaults={
                'title': book_data['volumeInfo']['title'],
                'author': ', '.join(book_data['volumeInfo'].get('authors', [])),
                'published_date': book_data['volumeInfo'].get('publishedDate', ''),
                'description': book_data['volumeInfo'].get('description', ''),
            }
        )
        
        if created:
            book_recommendation.save()
        return redirect('home')