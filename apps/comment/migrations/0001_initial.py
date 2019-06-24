# Generated by Django 2.0.3 on 2019-06-23 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20190623_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '关于自己评论',
                'verbose_name_plural': '关于自己评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
            ],
            options={
                'verbose_name': '文章评论',
                'verbose_name_plural': '文章评论',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('email', models.CharField(max_length=30, verbose_name='邮箱')),
                ('address', models.CharField(max_length=200, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='MessageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_related', to='comment.CommentUser', verbose_name='评论人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_child_comments', to='comment.MessageComment', verbose_name='父评论')),
                ('rep_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagecomment_rep_comments', to='comment.MessageComment', verbose_name='回复')),
            ],
            options={
                'verbose_name': '给我留言',
                'verbose_name_plural': '给我留言',
                'ordering': ['create_date'],
            },
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_related', to='comment.CommentUser', verbose_name='评论人'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='blog.Article', verbose_name='所属文章'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_child_comments', to='comment.ArticleComment', verbose_name='父评论'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='rep_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_rep_comments', to='comment.ArticleComment', verbose_name='回复'),
        ),
        migrations.AddField(
            model_name='aboutcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aboutcomment_related', to='comment.CommentUser', verbose_name='评论人'),
        ),
        migrations.AddField(
            model_name='aboutcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aboutcomment_child_comments', to='comment.AboutComment', verbose_name='父评论'),
        ),
        migrations.AddField(
            model_name='aboutcomment',
            name='rep_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='aboutcomment_rep_comments', to='comment.AboutComment', verbose_name='回复'),
        ),
    ]
