from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_albums(request, albums, results):

    page = request.GET.get('page')
    paginator = Paginator(albums, results)

    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        albums = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        albums = paginator.page(page)

    left_index = (int(page) - 2)
    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, albums
