from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post, Blog

# Create your views here.
def index(request):
    return HttpResponse("Main Screen!!!")

class BlogLV(ListView):	
	model = Blog
		
class BlogDV(DetailView):
	model = Blog		

class PostLV(ListView):
	model = Post
	template_name = 'blog/post_all.html'
	context_object_name = 'posts'
	paginate_by = 2

class PostDV(DetailView):
	model = Post	

class PostAV(ArchiveIndexView):
	model = Post
	date_field = 'modify_date'

class PostYAV(YearArchiveView):
	model = Post
	date_field = 'modify_date'
	make_object = True

class PostMAV(MonthArchiveView):
	model = Post
	date_field = 'modify_date'

class PostDAV(DayArchiveView):
	model = Post
	date_field = 'modify_date'

class PostTAV(TodayArchiveView):
	model = Post
	date_field = 'modify_date'