from django import forms

# naming form classes as modelname_form
class ObjectStore_form(forms.Form):
    # https://docs.djangoproject.com/en/dev/ref/forms/fields/
    object_id = forms.IntegerField(label='Object ID', min_value=1001)
    object_title = forms.CharField(label='Object Title', max_length=255)
