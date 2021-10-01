from rest_framework.pagination import PageNumberPagination


class OneHunderdPage(PageNumberPagination):
    page_size = 100
