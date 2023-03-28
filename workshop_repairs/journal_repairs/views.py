from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RepairForm
from .models import Repair

@login_required
def journal(request):
    form = RepairForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': True}
        return render(request, 'repairs/create_record.html', context)

    post = form.save(commit=False)
    post.author = request.user
    post.save()

    return redirect('posts:profile', request.user.username)
