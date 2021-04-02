from config.validators import validate_name, validate_phone_number, validate_room_number
from django.contrib.auth import get_user_model
from django.core.validators import validate_image_file_extension, validate_email, validate_integer
from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(
        'First Name',
        max_length=26,
        validators=[validate_name],
        blank=True,
        help_text='Teacher\'s first name.'
    )
    last_name = models.CharField(
        'Last Name',
        max_length=26,
        validators=[validate_name],
        blank=True,
        help_text='Teacher\'s last name.'
    )
    picture = models.ImageField(
        'Profile Picture',
        upload_to='picture/',
        blank=True,
        validators=[validate_image_file_extension],
        help_text='Teacher\'s picture (must match with picture in photo ID below) in .png or .jpg format. (Max 2 MB)'
    )
    email = models.EmailField(
        'Email Address',
        max_length=320,
        validators=[validate_email],
        blank=True,
        help_text='Teacher\'s e-mail address.'
    )
    phone_number = models.CharField(
        'Phone Number',
        max_length=14,
        blank=False,
        unique=True,
        validators=[validate_phone_number],
        help_text='Teacher\'s valid mobile number.'
    )
    room_number = models.CharField(
        'Room Number',
        max_length=14,
        blank=False,
        unique=True,
        validators=[validate_room_number],
        help_text='Your valid mobile number for OTP verification.'
    )
    subject_taught_1 = models.CharField(
        'Subjects Taught - First',
        max_length=255,
        validators=[validate_name],
        blank=True,
        help_text='The first subjects taught by teacher.'
    )
    subject_taught_2 = models.CharField(
        'Subjects Taught - Second',
        max_length=255,
        validators=[validate_name],
        blank=True,
        help_text='The second subjects taught by teacher.'
    )
    subject_taught_3 = models.CharField(
        'Subjects Taught - Third',
        max_length=255,
        validators=[validate_name],
        blank=True,
        help_text='The third subjects taught by teacher.'
    )
    subject_taught_4 = models.CharField(
        'Subjects Taught - Fourth',
        max_length=255,
        validators=[validate_name],
        blank=True,
        help_text='The fourth subjects taught by teacher.'
    )
    subject_taught_5 = models.CharField(
        'Subjects Taught - Fifth',
        max_length=255,
        validators=[validate_name],
        blank=True,
        help_text='The fifth subjects taught by teacher.'
    )


class ImportTask(models.Model):
    importer = models.ForeignKey(
        get_user_model(),
        related_name='initiated_by',
        blank=False
    )
    total_records = models.PositiveIntegerField(
        'Total Records',
        validators=[validate_integer],
    )
    processed_records = models.PositiveIntegerField(
        'Processed Records',
        validators=[validate_integer],
    )
    log = models.TextField(max_length=10000)
