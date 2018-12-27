from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class BaseMixin(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id or not self.created_at:
            self.created_at = timezone.now()
            self.updated_at = self.created_at
        else:
            auto_updated_at_is_disabled = kwargs.pop(
                'disable_auto_updated_at', False)
            if not auto_updated_at_is_disabled:
                self.updated_at = timezone.now()
        return super(BaseMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

