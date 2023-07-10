from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404, redirect, render
from django.core.files.base import ContentFile

from .forms import (VisualCheckConRodJournalsForm,
                    VisualCheckMainJournalsForm,
                    CheckСounterweightTorqueForm,
                    MeasuringConRodJournalsForm,
                    MeasuringMainJournalsForm,
                    MinMaxValueForm,
                    ImageCrankshaftForm,
                    SingleImageForm
                    )
from journal_repairs.models import Repair, EngineNumber
from .models import (MeasuringConRodJournals,
                     MeasuringMainJournals,
                     VisualCheckConRodJournals,
                     VisualCheckMainJournals,
                     CheckСounterweightTorque,
                     ImageCrankshaft)


@login_required
def crankshaft_view(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    dis_crankshaft = repair.vc_con_rod_journals.all()
    list_counterweight_torque = []
    for i in dis_crankshaft:
        for j in i.counterweight_torque.all():
            list_counterweight_torque.append(j.vc_con_rod_journsls)
    template = 'disassembly/crankshaft.html'
    context = {
        'repair': repair,
        'dis_crankshaft': dis_crankshaft,
        'repair_id': repair_id,
        'list_counterweight_torque': list_counterweight_torque,
    }
    return render(request, template, context)


@login_required
def crankshaft_create(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    form_v_check_con_rod = VisualCheckConRodJournalsForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_missuring_con_rod = MeasuringConRodJournalsForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_min_max_val = MinMaxValueForm(
        request.POST or None,
        files=request.FILES or None
    )
    if (not form_v_check_con_rod.is_valid()
        and not form_missuring_con_rod.is_valid()
        and not form_min_max_val.is_valid()
        ):
        context = {'form_v_check_con_rod': form_v_check_con_rod,
                   'form_missuring_con_rod': form_missuring_con_rod,
                   'form_min_max_val': form_min_max_val,
                   'repair_id': repair_id,
                   'repair': repair,
                   'meas_count': range(1, 9),
                   'is_edit': True}
        return render(request,
                      'disassembly/create_crankshaft.html', context)

    con_rod = form_v_check_con_rod.save(commit=False)
    con_rod.author = request.user
    con_rod.repair = repair
    con_rod.save()
    min_max = form_min_max_val.save()
    for i in range(len(request.POST.getlist('con_journal_10_meas'))):
        MeasuringConRodJournals.objects.create(
            author=request.user,
            repair=repair,
            engine_number=con_rod.engine_number,
            min_max_value=min_max,
            con_journal_1_meas=request.POST.getlist('con_journal_1_meas')[i],
            con_journal_2_meas=request.POST.getlist('con_journal_2_meas')[i],
            con_journal_3_meas=request.POST.getlist('con_journal_3_meas')[i],
            con_journal_4_meas=request.POST.getlist('con_journal_4_meas')[i],
            con_journal_5_meas=request.POST.getlist('con_journal_5_meas')[i],
            con_journal_6_meas=request.POST.getlist('con_journal_6_meas')[i],
            con_journal_7_meas=request.POST.getlist('con_journal_7_meas')[i],
            con_journal_8_meas=request.POST.getlist('con_journal_8_meas')[i],
            con_journal_9_meas=request.POST.getlist('con_journal_9_meas')[i],
            con_journal_10_meas=request.POST.getlist('con_journal_10_meas')[i]
        )

    return redirect('disassembly:crankshaft_create_list2', 
                    repair_id=repair_id, esn_id = con_rod.engine_number.id)


@login_required
def crankshaft_edit(request, repair_id, esn_id):
    repair = get_object_or_404(Repair, id=repair_id)
    esn = get_object_or_404(EngineNumber, id=esn_id)
    vc_con_rod_journals = get_object_or_404(
        VisualCheckConRodJournals, repair=repair, engine_number=esn)
    meas_con_rod_journals = get_list_or_404(
        MeasuringConRodJournals, repair=repair, engine_number=esn)
    min_max_cr = meas_con_rod_journals[0].min_max_value
    form_v_check_con_rod = VisualCheckConRodJournalsForm(
        request.POST or None,
        files=request.FILES or None,
        instance=vc_con_rod_journals
    )
    form_missuring_con_rod = MeasuringConRodJournalsForm(
        request.POST or None,
        files=request.FILES or None,
    )
    form_min_max_val = MinMaxValueForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if (not form_v_check_con_rod.is_valid()
        and not form_missuring_con_rod.is_valid()
        and not form_min_max_val.is_valid()
        ):
        context = {'form_v_check_con_rod': form_v_check_con_rod,
                   'form_missuring_con_rod': form_missuring_con_rod,
                   'form_min_max_val': form_min_max_val,
                   'repair_id': repair_id,
                   'repair': repair,
                   'esn': esn,
                   'meas_count': range(1, 9),
                   'is_edit': False}
        return render(request,
                      'disassembly/create_crankshaft.html', context)

    con_rod = form_v_check_con_rod.save(commit=False)
    con_rod.author = request.user
    con_rod.repair = repair
    con_rod.save()
    min_max_cr.delete()
    min_max = form_min_max_val.save()
    for i in range(len(request.POST.getlist('con_journal_10_meas'))):
        MeasuringConRodJournals.objects.create(
            author=request.user,
            repair=repair,
            engine_number=con_rod.engine_number,
            min_max_value=min_max,
            con_journal_1_meas=request.POST.getlist('con_journal_1_meas')[i],
            con_journal_2_meas=request.POST.getlist('con_journal_2_meas')[i],
            con_journal_3_meas=request.POST.getlist('con_journal_3_meas')[i],
            con_journal_4_meas=request.POST.getlist('con_journal_4_meas')[i],
            con_journal_5_meas=request.POST.getlist('con_journal_5_meas')[i],
            con_journal_6_meas=request.POST.getlist('con_journal_6_meas')[i],
            con_journal_7_meas=request.POST.getlist('con_journal_7_meas')[i],
            con_journal_8_meas=request.POST.getlist('con_journal_8_meas')[i],
            con_journal_9_meas=request.POST.getlist('con_journal_9_meas')[i],
            con_journal_10_meas=request.POST.getlist('con_journal_10_meas')[i]
        )

    return redirect('disassembly:crankshaft_view_detail', 
                    repair_id=repair_id, esn_id = con_rod.engine_number.id)


@login_required
def crankshaft_create_list2(request, repair_id, esn_id):
    repair = get_object_or_404(Repair, id=repair_id)
    esn = get_object_or_404(EngineNumber, id=esn_id)
    form_v_check_main = VisualCheckMainJournalsForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_check_counterweight = CheckСounterweightTorqueForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_missuring_main = MeasuringMainJournalsForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_min_max_val = MinMaxValueForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_crankshaft_images = ImageCrankshaftForm(
        request.POST or None,
        files=request.FILES or None
    )
    if (not form_v_check_main.is_valid()
        and not form_check_counterweight.is_valid()
        and not form_missuring_main.is_valid()
        and not form_min_max_val.is_valid()
        and not form_crankshaft_images.is_valid()
        ):
        context = {'form_v_check_main': form_v_check_main,
                   'form_check_counterweight': form_check_counterweight,
                   'form_missuring_main': form_missuring_main,
                   'form_min_max_val': form_min_max_val,
                   'esn': esn,
                   'repair_id': repair_id,
                   'repair': repair,
                   'meas_count': range(1, 5),
                   'form_crankshaft_images': form_crankshaft_images,
                   'is_edit': True}
        return render(request,
                      'disassembly/create_crankshaft_list2.html', context)

    main = form_v_check_main.save(commit=False)
    main.author = request.user
    main.repair = repair
    main.engine_number = esn
    main.save()
    vc_cr_journals = get_object_or_404(
        VisualCheckConRodJournals, repair=repair, engine_number=main.engine_number)
    counterweight = form_check_counterweight.save(commit=False)
    counterweight.author = request.user
    counterweight.repair = repair
    counterweight.engine_number = esn
    counterweight.vc_con_rod_journsls = vc_cr_journals
    counterweight.save()
    min_max = form_min_max_val.save()
    for i in range(len(request.POST.getlist('main_journal_11_meas'))):
        MeasuringMainJournals.objects.create(
            author=request.user,
            repair=repair,
            engine_number=esn,
            min_max_value=min_max,
            main_journal_1_meas=request.POST.getlist('main_journal_1_meas')[i],
            main_journal_2_meas=request.POST.getlist('main_journal_2_meas')[i],
            main_journal_3_meas=request.POST.getlist('main_journal_3_meas')[i],
            main_journal_4_meas=request.POST.getlist('main_journal_4_meas')[i],
            main_journal_5_meas=request.POST.getlist('main_journal_5_meas')[i],
            main_journal_6_meas=request.POST.getlist('main_journal_6_meas')[i],
            main_journal_7_meas=request.POST.getlist('main_journal_7_meas')[i],
            main_journal_8_meas=request.POST.getlist('main_journal_8_meas')[i],
            main_journal_9_meas=request.POST.getlist('main_journal_9_meas')[i],
            main_journal_10_meas=request.POST.getlist(
                'main_journal_10_meas')[i],
            main_journal_11_meas=request.POST.getlist(
                'main_journal_11_meas')[i]
        )
    for img in request.FILES.getlist('image'):
        data = img.read()
        photo = ImageCrankshaft(vc_con_rod_journsls=vc_cr_journals)
        photo.image.save(img.name, ContentFile(data))
        photo.save()

    return redirect('disassembly:crankshaft_view', repair_id=repair_id)


@login_required
def crankshaft_list2_edit(request, repair_id, esn_id):
    repair = get_object_or_404(Repair, id=repair_id)
    esn = get_object_or_404(EngineNumber, id=esn_id)
    vc_main_journals = get_object_or_404(
        VisualCheckMainJournals, repair=repair, engine_number=esn)
    check_counterweight = get_object_or_404(
        CheckСounterweightTorque, repair=repair, engine_number=esn)
    meas_main_journals = get_list_or_404(
        MeasuringMainJournals, repair=repair, engine_number=esn)
    min_max_main = meas_main_journals[0].min_max_value
    form_v_check_main = VisualCheckMainJournalsForm(
        request.POST or None,
        files=request.FILES or None,
        instance = vc_main_journals
    )
    form_check_counterweight = CheckСounterweightTorqueForm(
        request.POST or None,
        files=request.FILES or None,
        instance = check_counterweight
    )
    form_missuring_main = MeasuringMainJournalsForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_min_max_val = MinMaxValueForm(
        request.POST or None,
        files=request.FILES or None
    )
    form_crankshaft_images = ImageCrankshaftForm(
        request.POST or None,
        files=request.FILES or None
    )
    if (not form_v_check_main.is_valid()
        and not form_check_counterweight.is_valid()
        and not form_missuring_main.is_valid()
        and not form_min_max_val.is_valid()
        and not form_crankshaft_images.is_valid()
        ):
        context = {'form_v_check_main': form_v_check_main,
                   'form_check_counterweight': form_check_counterweight,
                   'form_missuring_main': form_missuring_main,
                   'form_min_max_val': form_min_max_val,
                   'esn': esn,
                   'repair_id': repair_id,
                   'repair': repair,
                   'meas_count': range(1, 5),
                   'form_crankshaft_images': form_crankshaft_images,
                   'is_edit': False}
        return render(request,
                      'disassembly/create_crankshaft_list2.html', context)

    main = form_v_check_main.save(commit=False)
    main.author = request.user
    main.repair = repair
    main.engine_number = esn
    main.save()
    vc_cr_journals = get_object_or_404(
        VisualCheckConRodJournals, repair=repair, engine_number=main.engine_number)
    counterweight = form_check_counterweight.save(commit=False)
    counterweight.author = request.user
    counterweight.repair = repair
    counterweight.engine_number = esn
    counterweight.vc_con_rod_journsls = vc_cr_journals
    counterweight.save()
    min_max_main.delete()
    min_max = form_min_max_val.save()
    for i in range(len(request.POST.getlist('main_journal_11_meas'))):
        MeasuringMainJournals.objects.create(
            author=request.user,
            repair=repair,
            engine_number=esn,
            min_max_value=min_max,
            main_journal_1_meas=request.POST.getlist('main_journal_1_meas')[i],
            main_journal_2_meas=request.POST.getlist('main_journal_2_meas')[i],
            main_journal_3_meas=request.POST.getlist('main_journal_3_meas')[i],
            main_journal_4_meas=request.POST.getlist('main_journal_4_meas')[i],
            main_journal_5_meas=request.POST.getlist('main_journal_5_meas')[i],
            main_journal_6_meas=request.POST.getlist('main_journal_6_meas')[i],
            main_journal_7_meas=request.POST.getlist('main_journal_7_meas')[i],
            main_journal_8_meas=request.POST.getlist('main_journal_8_meas')[i],
            main_journal_9_meas=request.POST.getlist('main_journal_9_meas')[i],
            main_journal_10_meas=request.POST.getlist(
                'main_journal_10_meas')[i],
            main_journal_11_meas=request.POST.getlist(
                'main_journal_11_meas')[i]
        )
    for img in request.FILES.getlist('image'):
        data = img.read()
        photo = ImageCrankshaft(vc_con_rod_journsls=vc_cr_journals)
        photo.image.save(img.name, ContentFile(data))
        photo.save()

    return redirect('disassembly:crankshaft_view_detail', 
                    repair_id=repair_id, esn_id = esn.id)


@login_required
def crankshaft_view_detail(request, repair_id, esn_id):
    repair = get_object_or_404(Repair, id=repair_id)
    esn = get_object_or_404(EngineNumber, id=esn_id)
    vc_con_rod_journals = get_object_or_404(
        VisualCheckConRodJournals, repair=repair, engine_number=esn)
    measur_con_rod_journals = list(reversed(get_list_or_404(
        MeasuringConRodJournals, repair=repair, engine_number=esn)))
    measur1_con_rod_journals = measur_con_rod_journals[0]
    vc_main_journals = get_object_or_404(
        VisualCheckMainJournals, repair=repair, engine_number=esn)
    check_counterweight = get_object_or_404(
        CheckСounterweightTorque, repair=repair, engine_number=esn)
    measur_main_journals = list(reversed(get_list_or_404(
        MeasuringMainJournals, repair=repair, engine_number=esn)))
    measur1_main_journals = measur_main_journals[0]
    crankshaft_images = vc_con_rod_journals.crankshaft_images.all()

    template = 'disassembly/crankshaft_detail.html'
    context = {
        'repair': repair,
        'esn': esn,
        'vc_con_rod_journals': vc_con_rod_journals,
        'repair_id': repair_id,
        'measur_con_rod_journals': measur_con_rod_journals,
        'measur1_con_rod_journals': measur1_con_rod_journals,
        'vc_main_journals': vc_main_journals,
        'check_counterweight': check_counterweight,
        'measur_main_journals': measur_main_journals,
        'measur1_main_journals': measur1_main_journals,
        'crankshaft_images': crankshaft_images,
    }
    return render(request, template, context)


@login_required
def crankshaft_delete(request, repair_id, esn_id):
    repair = get_object_or_404(Repair, id=repair_id)
    esn = get_object_or_404(EngineNumber, id=esn_id)
    vc_con_rod_journals = get_object_or_404(
        VisualCheckConRodJournals, repair=repair, engine_number=esn)
    measur_con_rod_journals = get_list_or_404(
        MeasuringConRodJournals, repair=repair, engine_number=esn)
    min_max_cr = measur_con_rod_journals[0].min_max_value
    vc_main_journals = get_object_or_404(
        VisualCheckMainJournals, repair=repair, engine_number=esn)
    check_counterweight = get_object_or_404(
        CheckСounterweightTorque, repair=repair, engine_number=esn)
    measur_main_journals = get_list_or_404(
        MeasuringMainJournals, repair=repair, engine_number=esn)
    min_max_main = measur_main_journals[0].min_max_value
    
    if not request.user == vc_con_rod_journals.author and not request.user.is_staff:
        return redirect('disassembly:crankshaft_view', repair_id=repair_id)
    
    vc_con_rod_journals.delete()
    vc_main_journals.delete()
    check_counterweight.delete()
    min_max_cr.delete()
    min_max_main.delete()

    return redirect('disassembly:crankshaft_view', repair_id=repair_id)


@login_required
def single_image_edit(request, repair_id, esn_id, image_id):
    repair = (get_object_or_404(Repair, id=repair_id)).repair_number
    image = get_object_or_404(ImageCrankshaft, id=image_id)
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
        return render(request,
                      'acceptance_aggregate/create_record_form_u.html', context)

    post = form.save(commit=False)
    post.save()

    return redirect('disassembly:crankshaft_view_detail',
                    repair_id=repair_id, esn_id=esn_id)
