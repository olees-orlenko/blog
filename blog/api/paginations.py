from rest_framework.pagination import PageNumberPagination


class LimitedPageNumberPagination(PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = 500
        return super().paginate_queryset(queryset, request, view)
