from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, redirect, render

from journal_repairs.models import Repair

from .forms import AcceptanceAggregateForm, ImageForm, SingleImageForm
from .models import AcceptanceAggregate, Image


@login_required
def acceptance_aggregate_view(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    acceptance = repair.aggregates.all()
    template = 'acceptance_aggregate/acceptance_aggregate.html'
    context = {
        'repair': repair,
        'acceptance': acceptance,
        'repair_id': repair_id,
    }
    return render(request, template, context)


@login_required
def acceptance_aggregate_create(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    form = AcceptanceAggregateForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_u = ImageForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid() and not form_u.is_valid():
        context = {'form': form,
                   'form_u': form_u,
                   'repair_id': repair_id,
                   'repair': repair,
                   'is_edit': True}
        return render(
            request, 'acceptance_aggregate/create_record_form_u.html', context)

    post = form.save(commit=False)
    post.author = request.user
    post.repair = repair
    post.save()
    for img in request.FILES.getlist('image'):
        data = img.read()
        photo = Image(acceptance_aggregate=post)
        photo.image.save(img.name, ContentFile(data))
        photo.save()

    return redirect('acceptance_aggregate:acceptance_aggregate_view',
                    repair_id=repair_id)


@login_required
def acceptance_aggregate_edit(request, repair_id, acceptance_id):
    repair = get_object_or_404(Repair, id=repair_id)
    acceptance = get_object_or_404(AcceptanceAggregate, id=acceptance_id)
    form = AcceptanceAggregateForm(
        request.POST or None,
        files=request.FILES or None,
        instance=acceptance
    )
    form_u = ImageForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if not form.is_valid() and not form_u.is_valid():
        context = {'form': form,
                   'form_u': form_u,
                   'repair_id': repair_id,
                   'repair': repair,
                   'is_edit': False}
        return render(
            request, 'acceptance_aggregate/create_record_form_u.html', context)

    post = form.save(commit=False)
    post.author = request.user
    post.repair = repair
    post.save()
    for img in request.FILES.getlist('image'):
        data = img.read()
        photo = Image(acceptance_aggregate=post)
        photo.image.save(img.name, ContentFile(data))
        photo.save()

    return redirect('acceptance_aggregate:acceptance_images_view',
                    repair_id=repair_id, acceptance_id=acceptance_id)


@login_required
def acceptance_aggregate_delete(request, repair_id, acceptance_id):
    acceptance = get_object_or_404(AcceptanceAggregate, id=acceptance_id)

    if not request.user == acceptance.author and not request.user.is_staff:
        return redirect('acceptance_aggregate:acceptance_aggregate_view',
                        repair_id=repair_id)

    acceptance.delete()
    return redirect('acceptance_aggregate:acceptance_aggregate_view',
                    repair_id=repair_id)


@login_required
def acceptance_images_view(request, repair_id, acceptance_id):
    repair = (get_object_or_404(Repair, id=repair_id))
    acceptance = get_object_or_404(AcceptanceAggregate, id=acceptance_id)
    images = acceptance.images.all()
    template = 'acceptance_aggregate/acceptance_detail.html'
    context = {
        'repair': repair,
        'acceptance': acceptance,
        'repair_id': repair_id,
        'images': images
    }
    return render(request, template, context)


@login_required
def single_image_edit(request, repair_id, acceptance_id, image_id):
    repair = (get_object_or_404(Repair, id=repair_id)).repair_number
    image = get_object_or_404(Image, id=image_id)
    form = SingleImageForm(
        request.POST or None,
        files=request.FILES or None,
        instance=image
    )
    if not form.is_valid():
        context = {'form': form,
                   'repair_id': repair_id,
                   'repair': repair,
                   'image': image,
                   'is_edit': False}
        return render(
            request, 'acceptance_aggregate/create_record_form_u.html', context)

    post = form.save(commit=False)
    post.save()

    return redirect('acceptance_aggregate:acceptance_images_view',
                    repair_id=repair_id, acceptance_id=acceptance_id)
