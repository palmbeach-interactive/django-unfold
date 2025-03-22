from django.contrib import admin
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.widgets import VersatileImagePPOIClickWidget

class VersatileImageFieldMixin:
    def _apply_versatile_image_widget(self, form_or_formset):
        # Get all VersatileImageFields from the model
        image_fields = [
            field.name for field in self.model._meta.fields
            if isinstance(field, VersatileImageField)
        ]

        # Get the base fields from either form or formset
        base_fields = (
            form_or_formset.base_fields if hasattr(form_or_formset, 'base_fields')
            else form_or_formset.form.base_fields
        )

        # Apply widget to each VersatileImageField
        for field_name in image_fields:
            if field_name in base_fields:
                base_fields[field_name].widget = VersatileImagePPOIClickWidget()

        return form_or_formset

class UnfoldVersatileImageAdmin(VersatileImageFieldMixin, admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return self._apply_versatile_image_widget(form)



class UnfoldVersatileImageTabularInline(VersatileImageFieldMixin, admin.TabularInline):
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        return self._apply_versatile_image_widget(formset)



class UnfoldVersatileImageStackedInline(VersatileImageFieldMixin, admin.StackedInline):
    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        return self._apply_versatile_image_widget(formset)


