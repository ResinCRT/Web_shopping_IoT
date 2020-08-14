from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from shop.models import Product
from django.urls import reverse_lazy
from django.utils import timezone


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Product
#     fields = ['title', 'description', 'content', 'tags']
#     # initial = {'slug': 'auto-filling-do-not-input'}
#     success_url = reverse_lazy('blog:index')
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         form.instance.modify_dt = timezone.now()
#         response = super().form_valid(form)
#
#         files = self.request.FILES.getlist("files")
#         for file in files:
#             attach_file = PostAttachFile(post=self.object, filename=file.name,
#                                          size=file.size, content_type=file.content_type, upload_file=file)
#             attach_file.save()
#         return response
