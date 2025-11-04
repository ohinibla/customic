from rest_framework.pagination import PageNumberPagination


class MockupPagination(PageNumberPagination):
    page_size = 5
