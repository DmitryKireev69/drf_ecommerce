from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    """
    Определяем кастомного менеджера пользователей CustomUserManager в Django.
    Наследующийся от BaseUserManager.
    Он расширяет стандартную функциональность для создания пользователей,
    добавляя валидацию данных и специфическую логику для суперпользователей.
    """

    def email_validator(self, email):
        """Проверяет корректность адреса электронной почты"""
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valid email address")

    def validate_user(self, first_name, last_name, email, password):
        """Валидирует данные для создания обычного пользователя"""
        if not first_name:
            raise ValueError("Users must submit a first name")

        if not last_name:
            raise ValueError("Users must submit a last name")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Base User Account: An email address is required")

        if not password:
            raise ValueError("User must have a password")

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """Метод создает обычного пользователя"""
        self.validate_user(first_name, last_name, email, password)

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        user.save()
        return user

    def validate_superuser(self, **extra_fields):
        """Валидирует данные для создания суперпользователя"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusers must have is_staff=True")
        return extra_fields

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """Метод создает суперпользователя"""
        extra_fields = self.validate_superuser(email, password, **extra_fields)
        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        return user