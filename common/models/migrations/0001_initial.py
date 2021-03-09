# Generated by Django 3.1.3 on 2021-03-04 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MigrationsHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('app_name', models.CharField(max_length=256, verbose_name='app名称')),
                ('file_name', models.CharField(max_length=256, verbose_name='文件名称')),
                ('file_content', models.TextField(verbose_name='文件内容')),
            ],
            options={
                'verbose_name': '迁移文件备份表',
                'db_table': 'common_migrations_history',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('code', models.CharField(max_length=64, unique=True, verbose_name='资源编码')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='资源名称')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='资源描述')),
                ('allowed', models.CharField(choices=[('all', '全部'), ('group', '组成员'), ('owner', '拥有者')], default='all', max_length=64, verbose_name='允许访问范围')),
                ('url_name', models.CharField(blank=True, help_text='资源访问的url名称，在urls.py中配置', max_length=128, null=True, unique=True, verbose_name='url name')),
            ],
            options={
                'verbose_name': '资源表',
                'db_table': 'common_resource',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('creator', models.CharField(blank=True, max_length=64, null=True, verbose_name='创建者')),
                ('owner', models.CharField(blank=True, max_length=64, null=True, verbose_name='拥有者')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='角色名称')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='角色描述')),
                ('state', models.CharField(choices=[('enabled', '已启用'), ('disabled', '已禁用'), ('published', '已发布'), ('editing', '编辑中'), ('deleted', '已删除')], default='enabled', max_length=32, verbose_name='角色状态')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否为内置角色')),
                ('is_test', models.BooleanField(default=False, verbose_name='是否为测试角色')),
                ('resource', models.ManyToManyField(related_name='role', to='models.Resource', verbose_name='关联资源')),
            ],
            options={
                'verbose_name': '角色表',
                'db_table': 'common_role',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='SystemLogRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SystemParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='参数名称')),
                ('value', models.CharField(max_length=128, unique=True, verbose_name='参数值')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='参数编码')),
                ('is_builtin', models.BooleanField(default=False, verbose_name='是否内置')),
            ],
            options={
                'verbose_name': '系统参数表',
                'db_table': 'common_system_parameter',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('creator', models.CharField(blank=True, max_length=64, null=True, verbose_name='创建者')),
                ('owner', models.CharField(blank=True, max_length=64, null=True, verbose_name='拥有者')),
                ('username', models.CharField(max_length=64, unique=True, verbose_name='用户名')),
                ('real_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='真实姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('wechat', models.CharField(blank=True, max_length=255, null=True, verbose_name='微信号')),
                ('email', models.CharField(max_length=64, verbose_name='邮箱地址')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='移动电话')),
                ('site', models.CharField(blank=True, max_length=256, null=True, verbose_name='关联站点')),
                ('allow_login', models.BooleanField(default=False, verbose_name='是否允许登陆')),
                ('is_builtin', models.BooleanField(default=False, verbose_name='是否为内置用户')),
            ],
            options={
                'verbose_name': '用户表',
                'db_table': 'common_user',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('token', models.CharField(help_text='用户登录成功后生成的token值，用于发起http请求时，进行身份认证的标识', max_length=64, verbose_name='token值')),
                ('is_expired', models.BooleanField(default=True, help_text='token是否过期的标识，过期的token会被认证系统认为是无效的', verbose_name='是否过期')),
                ('login_time', models.DateTimeField(help_text='用户登录的时间，用于判断当前token是否过期', verbose_name='登录时间')),
                ('user', models.OneToOneField(help_text='token所属的用户，当用户登录成功后会创建或更新此数据', on_delete=django.db.models.deletion.CASCADE, related_name='token', to='models.user', verbose_name='关联用户')),
            ],
            options={
                'verbose_name': '用户Token表',
                'db_table': 'common_user_token',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='描述')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('creator', models.CharField(blank=True, max_length=64, null=True, verbose_name='创建者')),
                ('owner', models.CharField(blank=True, max_length=64, null=True, verbose_name='拥有者')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='用户组名')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.role', verbose_name='角色')),
                ('users', models.ManyToManyField(to='models.User', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户组表',
                'db_table': 'common_user_group',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('classification', models.CharField(choices=[('view', '查看'), ('create', '创建'), ('modify', '修改'), ('delete', '删除'), ('approve', '审核'), ('page', '页面')], max_length=32, verbose_name='权限类型')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='权限描述')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.resource', verbose_name='所属资源')),
            ],
            options={
                'verbose_name': '权限表',
                'db_table': 'common_permission',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('ctime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('mtime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=128, verbose_name='部门名称')),
                ('code', models.CharField(blank=True, max_length=64, null=True, verbose_name='部门编码')),
                ('level', models.SmallIntegerField(default=0, verbose_name='部门层级')),
                ('desc', models.CharField(blank=True, max_length=256, null=True, verbose_name='部门描述')),
                ('leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.user', verbose_name='部门负责人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='models.department', verbose_name='父级部门')),
            ],
            options={
                'verbose_name': '部门表',
                'db_table': 'common_department',
            },
        ),
    ]