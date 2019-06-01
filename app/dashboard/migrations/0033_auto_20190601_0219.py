# Generated by Django 2.1.7 on 2019-06-01 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_auto_20190531_1953'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='bounty',
            index_together={('event', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'project_length', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'experience_level', 'current_bounty', 'network'), ('is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('event', 'is_featured', 'current_bounty', 'network'), ('bounty_owner_github_username', 'experience_level', 'current_bounty', 'network'), ('admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('event', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('is_featured', 'current_bounty', 'network', 'web3_created'), ('project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'is_featured', 'network', 'idx_status'), ('is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'is_featured', 'network', 'idx_status'), ('project_length', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'current_bounty', 'network'), ('event', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'experience_level', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('project_length', 'is_featured', 'network', 'idx_status'), ('admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('project_length', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('event', 'experience_level', 'current_bounty', 'network'), ('event', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('project_length', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('experience_level', 'network', 'idx_status'), ('project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'network', 'idx_status'), ('is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'is_featured', 'current_bounty', 'network'), ('bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'is_featured', 'experience_level', 'network', 'idx_status'), ('bounty_owner_github_username', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('is_featured', 'network', 'idx_status'), ('event', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'network', 'idx_status'), ('project_length', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'experience_level', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('experience_level', 'current_bounty', 'network', 'idx_status'), ('project_length', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'experience_level', 'network', 'idx_status'), ('project_length', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'current_bounty', 'network'), ('event', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('project_length', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'network', 'idx_status'), ('bounty_owner_github_username', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'current_bounty', 'network'), ('event', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('project_length', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('project_length', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'is_featured', 'network', 'idx_status'), ('project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('current_bounty', 'network', 'idx_status'), ('current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('project_length', 'experience_level', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('admin_override_and_hide', 'current_bounty', 'network'), ('is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('project_length', 'is_featured', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network'), ('is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('project_length', 'is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'network', 'idx_status'), ('is_featured', 'experience_level', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'current_bounty', 'network'), ('event', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('is_featured', 'current_bounty', 'network'), ('event', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('is_featured', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'current_bounty', 'network', 'idx_status'), ('experience_level', 'current_bounty', 'network'), ('event', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'network', 'idx_status'), ('project_length', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('event', 'is_featured', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network'), ('event', 'is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'current_bounty', 'network'), ('project_length', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('is_featured', 'experience_level', 'current_bounty', 'network', 'web3_created'), ('event', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('project_length', 'network', 'idx_status'), ('event', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'current_bounty', 'network', 'web3_created'), ('admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('is_featured', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('project_length', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network'), ('project_length', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'experience_level', 'network', 'idx_status'), ('project_length', 'is_featured', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'current_bounty', 'network', 'idx_status'), ('event', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'project_length', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'network', 'idx_status'), ('event', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'project_length', 'current_bounty', 'network'), ('event', 'current_bounty', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'current_bounty', 'network'), ('event', 'bounty_owner_github_username', 'admin_override_and_hide', 'network', 'idx_status'), ('bounty_owner_github_username', 'project_length', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('event', 'bounty_owner_github_username', 'project_length', 'network', 'idx_status'), ('bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network'), ('event', 'project_length', 'is_featured', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'experience_level', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('bounty_owner_github_username', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'bounty_owner_github_username', 'project_length', 'is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status', 'web3_created'), ('project_length', 'experience_level', 'current_bounty', 'network'), ('bounty_owner_github_username', 'is_featured', 'experience_level', 'admin_override_and_hide', 'network', 'idx_status'), ('event', 'project_length', 'is_featured', 'current_bounty', 'network'), ('is_featured', 'experience_level', 'admin_override_and_hide', 'current_bounty', 'network', 'idx_status'), ('event', 'is_featured', 'current_bounty', 'network', 'idx_status')},
        ),
    ]
