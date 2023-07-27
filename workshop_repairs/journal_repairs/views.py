from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (CommentForm, EngineHoursForm, EngineNumberForm,
                    EngineNumberRepairForm, RepairForm)
from .models import Customer, EngineNumber, Repair


def create_paginator(request, object):
    paginator = Paginator(object, settings.POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


@login_required
def repair(request):
    repairs = Repair.objects.all()
    page_obj = create_paginator(request, repairs)
    template = 'repairs/journal_repairs.html'
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


@login_required
def repair_detail(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    form = CommentForm()
    comments = repair.comments.all()
    context = {
        'repair': repair,
        'form': form,
        'comments': comments,
        'repair_id': repair_id,
    }
    return render(request, 'repairs/repair_detail.html', context)


@login_required
def repair_edit(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)

    if not request.user == repair.author:
        return redirect('journal_repairs:repair_detail', repair.id)

    form = RepairForm(
        request.POST or None,
        files=request.FILES or None,
        instance=repair
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': False}
        return render(request, 'repairs/create_record.html', context)

    form.save()

    return redirect('journal_repairs:repair_detail', repair.id)


@login_required
def esn_edit(request, esn_id, repair_id):
    esn = get_object_or_404(EngineNumber, id=esn_id)

    form = EngineNumberForm(
        request.POST or None,
        files=request.FILES or None,
        instance=esn
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': False}
        return render(request, 'repairs/create_record.html', context)

    form.save()

    return redirect('journal_repairs:repair_detail', repair_id)


@login_required
def esn_repairs(request, slug):
    esn_group = get_object_or_404(EngineNumber, slug=slug)
    repairs = esn_group.repairs.all()
    page_obj = create_paginator(request, repairs)
    template = 'repairs/journal_repairs.html'
    context = {
        'page_obj': page_obj,
        'slug': slug,
    }
    return render(request, template, context)


@login_required
def customer_repairs(request, slug):
    customer_group = get_object_or_404(Customer, slug=slug)
    repairs = customer_group.repairs.all()
    page_obj = create_paginator(request, repairs)
    template = 'repairs/journal_repairs.html'
    context = {
        'page_obj': page_obj,
        'slug': slug,
    }
    return render(request, template, context)


@login_required
def add_comment(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.repair = repair
        comment.save()
    return redirect('journal_repairs:repair_detail', repair_id=repair_id)


@login_required
def repair_create(request):
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

    return redirect('journal_repairs:esn_add')


@login_required
def esn_add(request):
    form = EngineNumberRepairForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': True, 'esn_add': True}
        return render(request, 'repairs/create_record.html', context)

    post = form.save(commit=False)
    post.save()

    return redirect('journal_repairs:esn_add')


@login_required
def esn_create(request):
    form = EngineNumberForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': True}
        return render(request, 'repairs/create_record.html', context)

    post = form.save(commit=False)
    post.save()

    return redirect('journal_repairs:esn_add')


@login_required
def hours_add(request):
    form = EngineHoursForm(
        request.POST or None,
        files=request.FILES or None
    )
    if not form.is_valid():
        context = {'form': form, 'is_edit': True, 'hours_add': True}
        return render(request, 'repairs/create_record.html', context)

    post = form.save(commit=False)
    post.save()

    return redirect('journal_repairs:hours_add')


@login_required
def search(request):
    if request.method == 'GET':
        query = request.GET.get('search', default='')
    repairs = Repair.objects.filter(
        Q(repair_number__icontains=query)
        | Q(customer__name__icontains=query)
    )
    page_obj = create_paginator(request, repairs)
    template = 'repairs/journal_repairs.html'
    paginator_query = f'search={query}&'
    context = {
        'page_obj': page_obj,
        'query': query,
        'q': paginator_query
    }
    return render(request, template, context)


@login_required
def esn_search(request):
    if request.method == 'GET':
        query = request.GET.get('search', default='')
    repairs = Repair.objects.filter(
        Q(engine_numbers__engine_number__icontains=query)
        | Q(engine_numbers__engine__title__icontains=query)
    )
    page_obj = create_paginator(request, repairs)
    template = 'repairs/journal_repairs.html'
    paginator_query = f'search={query}&'
    context = {
        'page_obj': page_obj,
        'query': query,
        'q': paginator_query
    }
    return render(request, template, context)
