from django import forms

class choose_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(choose_form, self).__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control mt-2 mb-2'
    name = forms.CharField(max_length=50, required=True)
    image = forms.ImageField(required=True)
