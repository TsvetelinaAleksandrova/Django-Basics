from django.core.exceptions import ValidationError


def validate_username_length(value):
    if len(value) < 3:
        raise ValidationError("Username must be at least 3 chars long!")


def validate_username_chars(value):
    if not all(char.isalnum() or char == '_' for char in value):
        raise ValidationError("Username must contain only letters, digits, and underscores!")
