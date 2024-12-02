# Generated by Django 5.1.3 on 2024-12-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_friendshiprequest_options_user_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendshiprequest',
            name='status',
            field=models.CharField(choices=[('notsend', 'NotSent'), ('send', 'Send'), ('waiting', 'Waiting'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('cancel', 'Cancel'), ('blocked', 'Blocked'), ('muted', 'Muted'), ('frozen', 'Frozen'), ('archived', 'Archived'), ('following', 'Following'), ('unfollowed', 'Unfollowed'), ('reported', 'Reported'), ('spam', 'Spam'), ('deleted', 'Deleted'), ('favorite', 'Favorite'), ('temporarily_blocked', 'TemporarilyBlocked'), ('verified', 'Verified'), ('request_resent', 'RequestResent'), ('suggested', 'Suggested'), ('ignored', 'Ignored'), ('inactive', 'Inactive'), ('limited', 'Limited')], default='notsend', max_length=20),
        ),
    ]
