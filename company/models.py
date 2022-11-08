import os
from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO


def get_image_file_extension_validator():
    return [
        FileExtensionValidator(allowed_extensions=["svg", "png", "jpg", "jpeg", "webp"])
    ]


# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=80, unique=True)
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
    thumbnail = models.ImageField(upload_to="thumbs", editable=False)
    email = models.EmailField(blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        name = self.get_full_name
        if name:
            return name
        return str(self.first_name)

    class Meta:
        verbose_name = verbose_name_plural = "Employee"
        unique_together = ["company", "email"]

    @property
    def get_full_name(self):
        """
        Return first name and last name combined as the full name
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):

        if not self.make_thumbnail():
            # set to a default thumbnail
            raise Exception("Could not create thumbnail - is the file type valid?")

        super(Employee, self).save(*args, **kwargs)

    def make_thumbnail(self):

        THUMB_SIZE = (100, 100)

        image = Image.open(self.profile_picture)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.profile_picture.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + "_thumb" + thumb_extension

        if thumb_extension in [".jpg", ".jpeg"]:
            FTYPE = "JPEG"
        elif thumb_extension == ".gif":
            FTYPE = "GIF"
        elif thumb_extension == ".png":
            FTYPE = "PNG"
        else:
            return False  # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True
