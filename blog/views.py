from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# O ponto depois de from significa o diretório atual ou
# o aplicativo atual. Como views.py e models.py estão no
# mesmo diretório podemos simplesmente usar . e o nome
# do arquivo (sem .py). Então nós importamos o nome do
# modelo (Post).

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
