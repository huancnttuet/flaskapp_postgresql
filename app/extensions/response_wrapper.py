# coding=utf-8
import logging

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)


def wrap_response(data=None, message="", http_code=200):
    """
    Return general HTTP response
    :param data:
    :param str message: detail info
    :param int http_code:
    :return:
    """
    if http_code == 200:
        return data, 200
    res = {
        'code': 'ERROR',
        'message': message,
    }
    if data:
        res['error'] = data

    return res, http_code
