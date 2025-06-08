from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,  # Total number of messages
            'next': self.get_next_link(),        # URL for next page
            'previous': self.get_previous_link(), # URL for previous page
            'current_page': self.page.number,     # Current page number
            'total_pages': self.page.paginator.num_pages,  # Total number of pages
            'results': data                       # List of messages
        }) 