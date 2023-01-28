from django import forms


class ProductForm(forms.Form):
    BRAND_LIST = [('Canon', 'Canon'), ('Sony', 'Sony'),('Nikon', 'Nikon')]
    TYPE_RADIO = [('DSLR', 'DSLR'),('Mirrorless', 'Mirrorless'),('Micro Four Thirds', 'Micro Four Thirds')]
    COLOR_RADIO = [('BLACK', 'BLACK'), ('white', 'white')]
    id = forms.CharField(max_length=13, label="id", required=True,
                         widget=forms.TextInput(attrs={'size': '15'}))
    name = forms.CharField(max_length=50, label="name", required=True,
                           widget=forms.TextInput(attrs={'size': '55'}))
    type = forms.CharField(max_length=30, label=" type", required=True,
                           widget=forms.Select(choices=TYPE_RADIO))
    color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLOR_RADIO)
    brand = forms.CharField(max_length=30, label=" brand", required=True,
                            widget=forms.Select(choices=BRAND_LIST))
    price = forms.FloatField(min_value=1.00, max_value=100000.00, label="price",
                             required=True, widget=forms.NumberInput(attrs={'size': '10'}))


