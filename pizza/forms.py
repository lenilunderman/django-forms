from django import forms
# new way ....
from .models import Pizza, Size

#old way...
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

# new way
class PizzaForm(forms.ModelForm):
    
    #email = forms.EmailField()
    #image = forms.ImageField()
    #size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    #forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Pizza
        # list of fields in the model
        fields = ['topping1', 'topping2', 'size']
        # customization using a dict
        labels = {'topping1': 'Topping 1:','topping2': 'Topping 2:'}
        #widgets = {'size': forms.Textarea} ce
