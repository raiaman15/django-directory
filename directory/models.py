from django.db.models import indexes
from config.validators import validate_name, validate_phone_number, validate_room_number
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, validate_image_file_extension, validate_integer
from django.db import models
from django.urls import reverse
from django_clamd.validators import validate_file_infection


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
        validators=[validate_file_infection],
        help_text='Teacher\'s picture (must match with picture in photo ID below) in .png or .jpg format. (Max 2 MB)'
    )
    email = models.EmailField(
        'Email Address',
        max_length=320,
        blank=False,
        unique=True,
        help_text='Teacher\'s e-mail address.'
    )
    phone_number = models.CharField(
        'Phone Number',
        max_length=16,
        blank=False,
        unique=True,
        validators=[validate_phone_number],
        help_text='Teacher\'s valid mobile number.'
    )
    room_number = models.CharField(
        'Room Number',
        max_length=14,
        blank=False,
        validators=[validate_room_number],
        help_text='Your valid mobile number for OTP verification.'
    )
    subject_taught = models.TextField(
        'Subjects Taught',
        max_length=1000,
        validators=[validate_name],
        blank=True,
        help_text='All the subjects taught by teacher.'
    )
    

    class Meta:
        indexes = [
            models.Index(fields=['last_name', ]),
            models.Index(fields=['subject_taught', ]),
        ]


class ImportTask(models.Model):

    STATUS = (
        ('P', 'Processing'),
        ('S', 'Success'),
        ('E', 'Error')
    )
    importer = models.ForeignKey(
        get_user_model(),
        related_name='initiated_by',
        blank=False,
        on_delete=models.DO_NOTHING
    )
    records_to_import = models.FileField(
        'Records to Import',
        upload_to='record_csv/',
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['csv']), validate_file_infection],
        help_text='The .csv file containing records of teachers.'
    )
    images_to_import = models.FileField(
        'Images to Import',
        upload_to='image_zip/',
        blank=False,
        validators=[FileExtensionValidator(allowed_extensions=['zip']), validate_file_infection],
        help_text='The .zip file containing images for teacher profiles.'
    )
    total_records = models.PositiveIntegerField(
        'Total Records',
        default=0,
        validators=[validate_integer]
    )
    status = models.CharField(
        'Task Status',
        max_length=1,
        default='P',
        choices=STATUS
    )
    log = models.TextField(max_length=999999)

    def __str__(self):
        return f'{self.importer} : {self.total_records} records : {self.status}'

    def get_absolute_url(self):
        return reverse('import_task_detail', args=[str(self.id)])
