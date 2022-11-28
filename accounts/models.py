from django.db import models
from django.contrib.auth.models import User


class ArtistTable(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    artist_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'artist_table'

    def __str__(self):
        return f"{self.artist_name}"

class Arts(models.Model):
    art_piece_id = models.CharField(primary_key=True, max_length=45)
    art_piece_name = models.CharField(unique=True, max_length=45)
    art_type = models.CharField(max_length=45, blank=True, null=True)
    artist = models.ForeignKey(ArtistTable, models.DO_NOTHING, blank=True, null=True)
    out_on_loan = models.CharField(max_length=15)
    date_acquired = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arts'
        
    def __str__(self):
        return f"{self.art_piece_name}"
        


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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return f"{self.username}"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

    def __str__(self):
        return f"{self.username}"


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
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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



class Exhibitions(models.Model):
    exhibition_id = models.IntegerField(primary_key=True)
    curator_name = models.CharField(max_length=45)
    exhibition_title = models.CharField(max_length=200)
    exhibition_year = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'exhibitions'

    def __str__(self):
        return f"{self.exhibition_title}"

    


class Members(models.Model):
    member = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    member_name = models.CharField(max_length=45, blank=True, null=True)
    member_phone = models.CharField(max_length=45, blank=True, null=True)
    member_email = models.CharField(max_length=45, blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'
    def __str__(self):
        return f"{self.member_name}"

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_type = models.CharField(max_length=50, blank=True, null=True)
    ticket_price = models.CharField(max_length=45)
    description = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'
    def __str__(self):
        return f"{self.ticket_type}"

class Bookings(models.Model):
    STATUS = (
                ('Pending', 'Pending'),
                ('Processing', 'Processing'),
                ('Booked', 'Booked'),
            )
    member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING, blank=True, null=True)
    date_booked = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True, choices=STATUS)
    bookings_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bookings'
    
    def __str__(self):
        return f"{self.ticket}"
