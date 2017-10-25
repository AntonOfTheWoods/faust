"""Faust exceptions."""

__all__ = [
    'FaustError',
    'ImproperlyConfigured',
    'DecodeError',
    'KeyDecodeError',
    'ValueDecodeError',
]


class FaustError(Exception):
    """Base-class for all Faust exceptions."""


class ImproperlyConfigured(FaustError):
    """The library is not configured/installed correctly."""


class DecodeError(FaustError):
    """Error while decoding/deserializing message key/value."""


class KeyDecodeError(DecodeError):
    """Error while decoding/deserializing message key."""


class ValueDecodeError(DecodeError):
    """Error while decoding/deserialization message value."""
