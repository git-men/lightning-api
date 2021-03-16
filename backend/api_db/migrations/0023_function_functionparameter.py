# Generated by Django 2.2.17 on 2021-02-02 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('api_db', '0022_auto_20200122_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='云函数名')),
                ('app', models.CharField(max_length=50, verbose_name='app')),
                ('model', models.CharField(max_length=50, verbose_name='数据模型')),
                ('description', models.CharField(default='', max_length=50, verbose_name='描述')),
                ('type', models.IntegerField(choices=[(0, '行操作'), (1, '全局操作'), (2, '批量操作')], default=0, verbose_name='类型')),
                ('login_required', models.BooleanField(default=True, verbose_name='要求登录')),
                ('staff_required', models.BooleanField(default=True, verbose_name='仅限员工')),
                ('superuser_required', models.BooleanField(default=False, verbose_name='仅限超级管理员')),
                ('enable', models.BooleanField(default=True, verbose_name='启用')),
                ('code', models.TextField(verbose_name='代码')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('roles', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='允许访问的角色')),
            ],
            options={
                'verbose_name': '云函数',
                'verbose_name_plural': '云函数',
                'unique_together': {('app', 'model', 'name')},
            },
        ),
        migrations.CreateModel(
            name='FunctionParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(verbose_name='参数名')),
                ('type', models.CharField(max_length=20, verbose_name='类型')),
                ('required', models.BooleanField(default=True, verbose_name='必填')),
                ('description', models.CharField(blank=True, max_length=1024, null=True, verbose_name='说明')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_db.Function', verbose_name='云函数')),
            ],
            options={
                'verbose_name': '云函数参数',
                'verbose_name_plural': '云函数参数',
            },
        ),
    ]
