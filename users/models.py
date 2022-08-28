from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    slug = AutoSlugField(populate_from="username", always_update=True, editable=True)
    make_public = models.BooleanField(default=True)

    # Social
    twitter_handle = models.CharField(max_length=20, blank=True)
    github_handle = models.CharField(max_length=20, blank=True)
    indiehackers_handle = models.CharField(max_length=20, blank=True)
    personal_website = models.URLField(blank=True)

    # Additional
    interviewed = models.BooleanField(default=False)
    short_bio = models.TextField(blank=True)

    referred_by = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="referee",
    )
    profile_image = CloudinaryField(
        "Image",
        overwrite=True,
        resource_type="image",
        folder=f"user-profile-image-{settings.ENVIRONMENT}",
        blank=True,
        null=True,
    )

    FREE = "FREE"
    PRO = "PRO"
    SUBSCRIPTION_LEVEL = [
        (FREE, "FREE"),
        (PRO, "PRO"),
    ]

    subscription_level = models.CharField(
        max_length=15,
        choices=SUBSCRIPTION_LEVEL,
        default=FREE,
    )

    class Meta:
        db_table = "auth_user"


class PayPalTransaction(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payload = models.JSONField(default=None, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["created"]),
        ]
