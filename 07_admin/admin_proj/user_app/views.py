from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import SignUpForm, CustomUserLoginForm

# Create your views here.

def index(request):

    return render(request, "user_app/index.html")


class CustomUserLoginView(LoginView):

    form_class = CustomUserLoginForm
    template_name = 'user_app/login.html'  # ログイン画面のテンプレート

    def form_valid(self, form):
        # ログイン成功後にリダイレクトすべきページを取得
        next_url = self.request.GET.get('next', None)
        if next_url:
            self.success_url = next_url
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # ここに必要な場合の追加の処理を追加することができます
        return response


def signup(request):

    if request.method == "POST":
        try:
            user = User()
            user = SignUpForm(request.POST, instance=user)
            user.save()
            return redirect(to="/user/login")
        except Exception as e:
            msg = f"ユーザーの作成に失敗しました。{e}"
    else:
        msg = "ユーザーを作成"
        user = SignUpForm()

    params = {
        "msg": msg,
        "form": user
    }

    return render(request, "user_app/signup.html", params)
