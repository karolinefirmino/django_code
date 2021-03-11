/home/karol/Documentos/django_projects/ic_uber/interface/staticfiles
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class JudiciarioInstancia(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'judiciario_instancia'


class JudiciarioTribunal(models.Model):
    name = models.CharField(unique=True, max_length=200)
    instancia = models.ForeignKey(JudiciarioInstancia, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'judiciario_tribunal'


class JudiciarioTribunalcadastro(models.Model):
    instancia = models.ForeignKey(JudiciarioInstancia, models.DO_NOTHING, blank=True, null=True)
    tribunal = models.ForeignKey(JudiciarioTribunal, models.DO_NOTHING, blank=True, null=True)
    turma = models.ForeignKey('JudiciarioTurma', models.DO_NOTHING, blank=True, null=True)
    vara = models.ForeignKey('JudiciarioVaras', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'judiciario_tribunalcadastro'


class JudiciarioTurma(models.Model):
    name = models.CharField(max_length=200)
    instancia = models.ForeignKey(JudiciarioInstancia, models.DO_NOTHING, blank=True, null=True)
    tribunal = models.ForeignKey(JudiciarioTribunal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'judiciario_turma'


class JudiciarioVaras(models.Model):
    name = models.CharField(unique=True, max_length=200)
    regiao = models.ForeignKey(JudiciarioTribunal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'judiciario_varas'


class JurisArquivo(models.Model):

    class Meta:
        managed = False
        db_table = 'juris_arquivo'


class JurisCadastro(models.Model):
    valorprocesso = models.DecimalField(db_column='valorProcesso', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    datajulgamento = models.DateField(db_column='dataJulgamento')  # Field name made lowercase.
    observacao = models.CharField(max_length=300)
    site = models.CharField(max_length=200)
    created_at = models.DateField()
    updated_at = models.DateTimeField()
    pesquisa = models.CharField(max_length=200)
    polopassivo = models.ForeignKey('JurisEmpresa', models.DO_NOTHING, db_column='poloPassivo_id')  # Field name made lowercase.
    tipodecisao = models.CharField(db_column='tipoDecisao', max_length=300)  # Field name made lowercase.
    vinculoempregaticio = models.CharField(db_column='vinculoEmpregaticio', max_length=300, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(unique=True, max_length=40)
    acordoextrajudicial = models.CharField(db_column='acordoExtrajudicial', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tipoprocesso = models.CharField(db_column='tipoProcesso', max_length=200, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(max_length=300, blank=True, null=True)
    docfile = models.CharField(max_length=100, blank=True, null=True)
    vara = models.CharField(max_length=200, blank=True, null=True)
    instância = models.CharField(max_length=200, blank=True, null=True)
    turma = models.CharField(max_length=200, blank=True, null=True)
    tribunal = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juris_cadastro'


class JurisEmpresa(models.Model):
    name = models.CharField(max_length=200)
    ano_rfb = models.DateField()
    cnpj = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'juris_empresa'


class JurisJurisdicao(models.Model):
    name = models.CharField(unique=True, max_length=200)
    varas = models.ForeignKey('JurisVaras', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juris_jurisdicao'


class JurisNumero(models.Model):
    numero = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'juris_numero'


class JurisTermobusca(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'juris_termobusca'


class JurisTribunal(models.Model):
    name = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'juris_tribunal'


class JurisVaras(models.Model):
    name = models.CharField(unique=True, max_length=200)
    regiao = models.ForeignKey(JurisTribunal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'juris_varas'
