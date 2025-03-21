from django.contrib import admin
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.widgets import VersatileImagePPOIClickWidget


class UnfoldVersatileImageAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Get all VersatileImageFields from the model
        image_fields = [
            field.name for field in self.model._meta.fields
            if isinstance(field, VersatileImageField)
        ]

        # Apply widget to each VersatileImageField
        for field_name in image_fields:
            if field_name in form.base_fields:
                form.base_fields[field_name].widget = VersatileImagePPOIClickWidget()
        return form
