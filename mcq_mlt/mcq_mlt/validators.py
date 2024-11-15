from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weightage(weightage):
    if not (weightage > 0 and (weightage // 1 == weightage)):
        raise ValidationError(
                _('must be at least 1 and a whole number.'),
            params={'weightage': weightage},
        )

def validate_time(hr):
    try:
        if not eval(hr) > 0:
            raise ValidationError(
                _('Time must be greater than 0') ,
                params={'hr': hr}
            )

    except:
        raise ValidationError(
           _('expected  01, 0.1 like number') ,
           params={'hr': hr}
        )
        