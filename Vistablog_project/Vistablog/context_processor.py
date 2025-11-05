from .models import Categories, Post

def context_processor(request):
    categories = Categories.objects.all()
    
    return {
        'allcategory': categories,
    }