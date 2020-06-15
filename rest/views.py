from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import BlogForm

# Create your views here.


class CreateBlog(CreateView):
    form_class = BlogForm
    template_name = 'rest/create_blog.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
