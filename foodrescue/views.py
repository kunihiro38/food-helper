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

from foodrescue.models import Member
from .forms import FoodrescueForm

# 0915お問い合わせフォーム作成#
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm
# 0915お問い合わせフォーム作成#

#myprofileでの登録画面
def myprofile(request):
    if request.method == 'POST':
        obj = Member()
        member = FoodrescueForm(request.POST, instance=obj)
        member.save()
        return render("foodrescue/index.html")
        return redirect('/')

    else:
        form = FoodrescueForm()
        return render(request, 'myprofile.html', {'form':form})

def index(request):
    return render(request,'index.html')

def registration(request): # registration関数
    return render(request, 'registration.html') # welcome.htmlを返す

def entry(request): # registration関数
    return render(request, 'entry.html') # entry.htmlを返す

def loginscreen(request): # loginscreen関数
    return render(request,'loginscreen.html') # loginscreen.htmlを返す

def operation(request): # operation関数
    return render(request,'operation.html') # operation.htmlを返す

def service(request): # bservice関数
    return render(request,'service.html') # service.htmlを返す

def privacy(request): # bservice関数
    return render(request,'privacy.html') # privacy.htmlを返す

def required(request): # bservice関数
    return render(request,'required.html') # required.htmlを返す

def mainvisual(request): # bservice関数
    return render(request,'mainvisual.html') # mainvisual.htmlを返す

def search(request): # bservice関数
    return render(request,'search.html') # searrch.htmlを返す

def imagelist(request): # bservice関数
    return render(request, 'imagelist.html') # imagelist.htmlを返す

def zoomimage(request): # bservice関数
    return render(request, 'zoomimage.html') # imagelist.htmlを返す

def editprofile(request): # bservice関数
    return render(request, 'editprofile.html') # myprofile.htmlを返す

def guide(request): # bservice関数
    return render(request,'guide.html') # guide.htmlを返す


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