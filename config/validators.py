import re

from django.core.exceptions import ValidationError


def validate_name(value):
    """ Validates name of any entity """
    if not value.replace(" ", "").isalpha():
        raise ValidationError(
            ('%(value)s is not a valid name. It should contain only alphabets.'),
            params={'value': value},
        )


def validate_phone_number(value):
    """ Validates phone number - 10 digit UAE Phone Number """
    Pattern = re.compile("(+971)?-[0-9]{3}-[0-9]{3}-[0-9]{3}")
    if not Pattern.match(value):
        raise ValidationError(
            ('%(value)s is not a valid contact number. It should be in similar to +971XXXXXXXXXX.'),
            params={'value': value},
        )


def validate_room_number(value):
    """ Validates room number - alphanumeric """
    if not value.replace(" ", "").isalnum():
        raise ValidationError(
            ('%(value)s is not a valid room number. It should contain alphabets or digit or both.'),
            params={'value': value},
        )
