from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from cart.models import Orders
from .forms import RegisterForm


@login_required()
def profile(request):
    email = request.user.email
    user = User.objects.get(email=email)
    is_admin = user.is_staff
    orders = Orders.objects.filter(email=email).prefetch_related('orderitem_set__product')
    context = {'orders': orders, 'is_admin': is_admin}
    return render(request, 'users/profile.html', context)


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


