#!/usr/bin/python3
""" Locked Class Module"""


class LockedClass:
    """ No new instance attributes is accepted/
    unless it's called first_name """
    __slots__ = "first_name"
