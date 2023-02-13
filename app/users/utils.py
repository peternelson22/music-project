from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_profiles(request, profiles, results):

    page = request.GET.get('page')
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, profiles


def paginate_msgs(request, msgs, results):

    page = request.GET.get('page')
    paginator = Paginator(msgs, results)

    try:
        msgs = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        msgs = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        msgs = paginator.page(page)

    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, msgs
