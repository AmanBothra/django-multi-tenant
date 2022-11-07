from django.db import models
from django.core.validators import FileExtensionValidator


def get_image_file_extension_validator():
    return [
        FileExtensionValidator(allowed_extensions=["svg", "png", "jpg", "jpeg", "webp"])
    ]


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = verbose_name_plural = "Company"


class Employee(models.Model):

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pictures",
        blank=True,
        validators=get_image_file_extension_validator(),
    )
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = verbose_name_plural = "Employee"

    @property
    def full_name(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Return first name and last name combined as the full name
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        if not len(full_name.strip()):
            full_name = self.email
        return full_name.strip()
