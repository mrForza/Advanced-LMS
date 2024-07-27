from logging import Logger


class DomainException(Exception):
    pass


class IncompatibleObjectsError(DomainException):
    pass