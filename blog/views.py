from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import MyPost
from .models import Comment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def newsfeed(request):
    context = {
        'posts': MyPost.objects.all()
    }
    return render(request, 'blog/newsfeed.html', context)


class PostListView(ListView):
    model = MyPost
    template_name = 'blog/newsfeed.html'
    context_object_name = 'posts'
    ordering = ['-cr_date']


class PostCreateView(CreateView):
    model = MyPost
    fields = ['msg', 'pic', 'video']

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})


def timeline(request):
    return render(request, 'blog/timeline.html')


def faq(request):
    return render(request, 'blog/faq.html')


def timeline_about(request):
    return render(request, 'blog/timeline_about.html')


def timeline_album(request):
    return render(request, 'blog/timeline_album.html')


def timeline_friends(request):
    return render(request, 'blog/timeline_friends.html')


def newsfeed_images(request):
    return render(request, 'blog/newsfeed_images.html')


def comment(request):
    comments = Comment.objects.all()
    data = {"results": list(comments.values("comment", "created_by"))}
    return JsonResponse(data)


@csrf_exempt
def create_comment(request):
    if request.method == "POST":
        data = request.body.decode("utf-8").split("&")
        comment = data[0].split("=")
        user = data[1].split("=")
        print(comment.join(), "***************************8?????????????????????????")
        # print(user[1], "***************************8?????????????????????????")
        data_body = {comment: comment[1], user: user[1]}
        json = Comment.objects.create({comment[1], user[1]})
        return JsonResponse(json)
