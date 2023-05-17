#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get_member_values(cls):
        return [item.value for item in cls._member_map_.values()]

    @classmethod
    def get_member_names(cls):
        return [name for name in cls._member_names_]


class IntEnum(int, EnumBase):
    """整型枚举"""

    pass


class StrEnum(str, EnumBase):
    """字符串枚举"""

    pass


class MenuType(IntEnum):
    """菜单类型"""

    directory = 0
    menu = 1
    button = 2


class RoleDataScope(IntEnum):
    """数据范围"""

    all = 1
    custom = 2


class MethodType(StrEnum):
    """请求方法"""

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
