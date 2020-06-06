# coding=utf-8
import logging
import decimal
from marshmallow.fields import *

from . import validators

__author__ = 'Kien.HT'
_logger = logging.getLogger(__name__)


def convert_null(value):
    """

    :param value:
    :return:
    """
    if isinstance(value, str):
        value = value.strip()
        if value.lower() == 'null':
            return None

    return value


class String(String):
    def __init__(self, min=None, max=None, **kwargs):
        """

        :param maxlength:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.min = min
        self.max = max or 255

        self.validators.append(validators.Length(min=min, max=max))

    def _deserialize(self, value, attr, data):
        value = convert_null(value)

        return super()._deserialize(value, attr, data)


class PureInteger(Integer):
    default_error_messages = {
        'invalid_type': '({type}){value} Invalid integer value'
    }

    def __init__(self, min=None, max=None, **kwargs):
        """

        :param int min:
        :param int max:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.min = min or 0

        self.validators.append(
            validators.Any(
                validators.IsNone(),
                validators.Range(min=min, max=max)
            )
        )

    def _format_num(self, value):
        value = convert_null(value)
        if value is None:
            return None
        if not isinstance(value, int):
            self.fail('invalid_type', type=type(value), value=value)
        return super()._format_num(value)


class NotNegativeFloat(Float):
    default_error_messages = {
        'invalid_type': '({type}){value} Invalid float value'
    }

    def __init__(self, min=None, max=None, **kwargs):
        """

        :param min:
        :param max:
        :param kwargs:
        """
        super().__init__(**kwargs)
        self.min = min or 0.0
        self.validators.append(
            validators.Any(
                validators.IsNone(),
                validators.Range(min=min, max=max)
            )
        )

    def _format_num(self, value):
        value = convert_null(value)
        if value is None:
            return None
        if not isinstance(value, float):
            try:
                value = float(value)
            except ValueError:
                self.fail('invalid_type', type=type(value), value=value)

        return super()._format_num(value)


class MoneyAmount(PureInteger):
    num_type = decimal.Decimal

    def __init__(self, as_string=False, **kwargs):
        """

        :param as_string:
        :param kwargs:
        """
        super().__init__(as_string, **kwargs)
        self.validators.insert(0, validators.Range(min=0))

    def _deserialize(self, value, attr, data):
        value = convert_null(value)
        return int(value)
