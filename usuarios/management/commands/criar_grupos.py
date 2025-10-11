from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from usuarios.models import Usuario

class Command(BaseCommand):
    help = 'Cria grupos de usuários e permissões padrão para o sistema de impressões.'

    def handle(self, *args, **options):
        # Grupo Administrador
        admin_group, created = Group.objects.get_or_create(name='Administrador')
        # Grupo Professor
        prof_group, created = Group.objects.get_or_create(name='Professor')

        # Permissões customizadas (exemplo: pode gerenciar usuários, pode enviar impressões)
        usuario_ct = ContentType.objects.get_for_model(Usuario)
        permissao_gerenciar_usuarios, _ = Permission.objects.get_or_create(
            codename='can_manage_users',
            name='Pode gerenciar usuários',
            content_type=usuario_ct
        )
        permissao_enviar_impressao, _ = Permission.objects.get_or_create(
            codename='can_send_print',
            name='Pode enviar impressões',
            content_type=usuario_ct
        )

        # Administrador: todas permissões
        admin_group.permissions.add(permissao_gerenciar_usuarios, permissao_enviar_impressao)
        # Professor: apenas enviar impressões
        prof_group.permissions.add(permissao_enviar_impressao)

        self.stdout.write(self.style.SUCCESS('Grupos e permissões criados/atualizados com sucesso!'))
