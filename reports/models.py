from django.db import models

from django.db import models


class AdminTable(models.Model):
    username = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(unique=True, max_length=45)
    full_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'admin_table'


class Arts(models.Model):
    art_piece_id = models.CharField(primary_key=True, max_length=45)
    art_piece_name = models.CharField(unique=True, max_length=45)
    art_type = models.CharField(max_length=45, blank=True, null=True)
    artist_id = models.IntegerField(blank=True, null=True)
    artist_name = models.CharField(max_length=45)
    out_on_loan = models.CharField(max_length=15)
    date_acquired = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arts'


class ArtistTable(models.Model):
    artist_id = models.CharField(primary_key=True, max_length=45)
    artist_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'artist_table'


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


class Bookings(models.Model):
    member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
    ticket = models.ForeignKey('Ticket', models.DO_NOTHING, blank=True, null=True)
    date_booked = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    bookings_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bookings'


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
    exhibition_year = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = 'Exhibitions by Year'

   
    
    class Meta:
        managed = False
        db_table = 'exhibitions'


class GiftShopInventory(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.CharField(unique=True, max_length=45)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_instock = models.IntegerField(blank=True, null=True)
    vendor_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'gift_shop_inventory'


class GiftShopTransaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    item = models.OneToOneField(GiftShopInventory, models.DO_NOTHING)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity_sold = models.IntegerField()
    member_id = models.IntegerField(blank=True, null=True)
    register_id = models.CharField(max_length=45)
    emp_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gift_shop_transaction'


class HumanResource(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=25)
    emp_social_security = models.IntegerField(unique=True)
    address = models.CharField(max_length=45)
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'human_resource'


class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=45, blank=True, null=True)
    member_phone = models.CharField(max_length=45, blank=True, null=True)
    member_email = models.CharField(max_length=45, blank=True, null=True)
    profile_pic = models.TextField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'members'


class MembersExisting(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_full_name = models.CharField(max_length=45)
    member_contact_no = models.CharField(unique=True, max_length=45)
    member_email_id = models.CharField(unique=True, max_length=45)
    state = models.CharField(max_length=2)
    user_id = models.CharField(unique=True, max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=35)
    zipcode = models.IntegerField()
    street_address = models.CharField(max_length=45)
    birthdate = models.DateField()
    member_since = models.DateField()

    class Meta:
        managed = False
        db_table = 'members_existing'


class Museum(models.Model):
    museum_id = models.AutoField(primary_key=True)
    museum_name = models.CharField(max_length=45)
    art_piece_id = models.CharField(max_length=15)
    emp_id = models.IntegerField()
    emp_first_name = models.CharField(max_length=25)
    emp_last_name = models.CharField(max_length=25)
    emp_middle_initial = models.CharField(max_length=1, blank=True, null=True)
    emp_date_worked = models.DateField(blank=True, null=True)
    emp_shift_start = models.TimeField(blank=True, null=True)
    emp_shift_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'museum'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_type = models.CharField(max_length=50, blank=True, null=True)
    ticket_price = models.CharField(max_length=45)
    description = models.CharField(max_length=55, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'


class TicketHouse(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_type = models.CharField(max_length=15)
    ticket_price = models.DecimalField(max_digits=4, decimal_places=2)
    tickets_sold = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ticket_house'