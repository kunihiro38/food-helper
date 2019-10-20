#coding:utf-8
# viewの役割は大雑把に言うと、リクエストオブジェクトを受け取ってレスポンスオブジェクトを返すこと。
# 1.htmlページを表示するためのコンテンツを保持したレスポンス
# 2.リダイレクトするためのレスポンス
# 3.エラーを通知するためのレスポンス
#ここに書いた内容が、htmlでのpost時にDBに反映される

from django.shortcuts import render, redirect
# from django.contrib.auth.models import User #0917このままだとauth_userに登録される

from django.contrib.auth import login, authenticate #ログイン関係
from django.views.generic import CreateView
#　プロフィール登録関係
from .models import Member as m
from .forms import FoodrescueForm

# 0915お問い合わせフォーム作成#
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

# 1010プロフィール画像アップロード
from .forms import PhotoForm
from .models import Photo
from django.contrib.auth.decorators import login_required

# 1018追記 Gmap用？
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {'photos': Photo.objects.all()}
    return render(request,'index.html', context)

def photoupload(request):
    # GETのときにはformをキーにして辞書型でPhotoForm()を返している
    if request.method == 'GET':
        return render(request, 'main_share.html', {
            'form': PhotoForm(),
    })
    # POSTで画像を投稿したときには返してあげていません。なので、いったん画像を投稿するとフォームが消えてしまう
    elif request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError('invalid form')

        photo = Photo()
        # 画像の登録
        photo.image = form.cleaned_data['image']
        # store_id　の登録
        photo.store_id = request.POST['store_id']
        photo.save()
        context = {'photos': Photo.objects.all()}
#         return redirect('/')
#         return redirect(request, 'main_share.html')
        #
        #　renderの第３引数は、辞書型を受け取る
        return render(request, 'main_share.html', {'form': PhotoForm()})

# ログインしたユーザーのみに閲覧制限できるデコレータ
# @login_required
def myprofile(request):
    if request.method == 'POST':
        member = m(
            name=request.POST['name'],
            auth_User=request.user,
            gender=request.POST['gender'],
            age=request.POST['age'],
            address1=request.POST['address1'],
            self_introduction=request.POST['self_introduction'],
            )
        member.save()
        return redirect('/')

    else:
        form = FoodrescueForm()
        return render(request, 'myprofile.html', {'form':form})

def registration(request): # registration関数
    return render(request, 'registration.html') # welcome.htmlを返す

def operation(request): # operation関数
    return render(request,'operation.html') # operation.htmlを返す

def service(request): # bservice関数
    return render(request, 'service.html') # service.htmlを返す

def privacy(request): # bservice関数
    return render(request,'privacy.html') # privacy.htmlを返す

def required(request): # bservice関数
    return render(request,'required.html') # required.htmlを返す

# ログインしたユーザーのみに閲覧制限できるデコレータ
@login_required
def mainvisual(request): # bservice関数
    return render(request, 'mainvisual.html') # mainvisual.htmlを返す

def search(request): # bservice関数
    return render(request, 'search.html') # searrch.htmlを返す

def imagelist(request): # bservice関数
    return render(request, 'imagelist.html') # imagelist.htmlを返す

def editprofile(request): # bservice関数
    return render(request, 'editprofile.html') # myprofile.htmlを返す

def guide(request): # bservice関数
    return render(request, 'guide.html') # guide.htmlを返す

# 0915お問い合わせフォーム作成#
class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('foodrescue:contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "お問い合わせは正常に送信されました。"
        return context

@login_required
def main(request):
    template = loader.get_template('gmap/main.html')
    context = {}
    return HttpResponse(template.render(context, request))
