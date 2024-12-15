from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from SmartInventoryManager.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create groups for roles
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        staff_group, _ = Group.objects.get_or_create(name='Staff')
        customer_group, _ = Group.objects.get_or_create(name='Customer')

        # Assign permissions
        admin_permissions = Permission.objects.all()
        staff_permissions = Permission.objects.filter(codename__in=['can_view_inventory'])
        
        admin_group.permissions.set(admin_permissions)
        staff_group.permissions.set(staff_permissions)

        User.objects.filter(role='admin').update(groups=[admin_group])
        User.objects.filter(role='staff').update(groups=[staff_group])