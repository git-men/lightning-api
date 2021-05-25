from django.conf import settings
from api_basebone.core.admin import BSMAdmin, register
from api_db.models import Api


@register
class APIAdmin(BSMAdmin):
    modal_form = False
    form_fields = ['operation']
    display = ['id', 'operation', 'slug', 'name']

    @property
    def inline_actions(self):
        api_base_url = getattr(settings, 'API_BASE_URL', self.request.build_absolute_uri('/api'))
        api_doc_base_url = getattr(settings, 'API_DOC_BASE_URL', self.request.build_absolute_uri('/api_doc/help'))
        return [
            'edit', 'delete',
            {
                'type': 'info',
                'title': '请求地址',
                'params': {'title': '查看请求地址', 'content': api_base_url + '/${slug}/'},
            },
            {
                'type': 'link',
                'title': '查看文档',
                'params': {'link': api_doc_base_url + '/#/default/${slug}'},
            },
        ]

    table_actions = [
        {
            'icon': 'plus',
            'title': '新建',
            'submenus': [
                {
                    'title': '列表接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=list'},
                },
                {
                    'title': '详情接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=retrieve'},
                },
                {
                    'title': '新建接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=create'},
                },
                {
                    'title': '删除接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=delete'},
                },
                {
                    'title': '全部更新接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=update'},
                },
                {
                    'title': '部分更新接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=replace'},
                },
                {
                    'title': '云函数接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=func'},
                },
                {
                    'title': '批量删除接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=delete_by_condition'},
                },
                {
                    'title': '批量更新接口',
                    'type': 'link',
                    'params': {'link': '/content/api_db__api/add?operation=update_by_condition'},
                },
            ]
        }
    ]

    class Meta:
        model = Api
