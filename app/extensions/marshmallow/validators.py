# coding=utf-8
import logging
from marshmallow.validate import *

__author__ = 'Kien.HT'
_logger = logging.getLogger(__name__)


class Any(Validator):
    """ Chỉ cần thỏa mãn ít nhất 1 validator, không tính thứ tự
    """
    def __init__(self, *validators):
        """
        :param validators:
        """
        self.validators = validators

    def __call__(self, value):
        if not len(self.validators):
            return

        errors = []
        for validator in self.validators:
            try:
                validator(value)
                break
            except ValidationError as e:
                errors.append(e)
        else:
            raise errors[0]


class IsNone(Validator):
    """Chỉ cho phép giá trị None"""
    def __call__(self, value):
        if value is not None:
            raise ValidationError('%s is not None' % value)
