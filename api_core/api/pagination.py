from rest_framework.pagination import (
    _positive_int,
    PageNumberPagination as OriginPageNumberPagination,
)
from rest_framework.response import Response
from werkzeug import Local

local = Local()

class PageNumberPagination(OriginPageNumberPagination):

    max_page_size = 1000
    page_size = 100
    page_query_param = 'page'
    page_size_query_param = 'size'

    def get_page_size(self, request):
        """重写此方法是为了支持以下场景

        - 当传入的数据包含分页参数时，返回对应的分页数据结构
        - 当传入的数据不包含分页参数时，直接返回非分页数据的数据结构
        """
        if getattr(local, 'page_query_param'):
            self.page_query_param = local.page_query_param
        
        if getattr(local, 'page_size_query_param'):
            self.page_size_query_param = local.page_size_query_param

        if self.page_size_query_param:
            print('有自己的分页Size ', self.page_size_query_param)
            try:
                return _positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size,
                )
            except (KeyError, ValueError):
                return
        return self.page_size
