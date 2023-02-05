from django import forms
from .models import *

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


# class ProductMFrom(forms.ModelForm):
#     class Meta:
#         model = ProductM
#         fields = ('pid','name','brand','price','net','catagory')
#         widgets = {
#             'pid': forms.TextInput(attrs={'class': 'form-control'}),
#             'name':forms.TextInput(attrs={'class': 'form-control','required':'required','max_length':35}),
#             'brand': forms.TextInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'net': forms.NumberInput(attrs={'class': 'form-control'}),
#             'catagory': forms.Select(attrs={'class': 'form-control'}),
#         }
#     labels = {
#         'pid': 'รหัสสินค้า',
#         'name': 'ชื่อสินค้า',
#         'brand': 'แบรนด์',
#         'price': 'ราคา',
#         'net': 'คงเหลือ',
#         'catagory': 'ประเภท',
#     }

# คนละส่วนนะจ๊ะ

class showgoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('gid','name','brand','mode','price','net','property','goodscategory')
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control','required':'required','max_length':35}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'mode': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'net': forms.NumberInput(attrs={'class': 'form-control'}),
            'property': forms.TextInput(attrs={'class': 'form-control'}),
            'goodscategory': forms.Select(attrs={'class': 'form-control'}),
        }
    labels = {
        'pid': 'รหัสสินค้า',
        'name': 'ชื่อสินค้า',
        'brand': 'แบรนด์',
        'mode': 'รุ่น',
        'price': 'ราคา',
        'net': 'คงเหลือ',
        'property': 'คุณสมบัติ',
        'goodscategory': 'ประเภท',
    }
#---------------------------------------
class showcustomerForm(forms.ModelForm):
        class Meta:
            model = Customer
            fields = ('cid', 'name', 'surname', 'address', 'telephone', 'gender', 'carreer','password')
            widgets = {
                'cid': forms.TextInput(attrs={'class': 'form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'max_length': 35}),
                'surname': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.TextInput(attrs={'class': 'form-control'}),
                'telephone': forms.TextInput(attrs={'class': 'form-control'}),
                'gender': forms.TextInput(attrs={'class': 'form-control'}),
                'carreer': forms.TextInput(attrs={'class': 'form-control'}),
                'password': forms.TextInput(attrs={'class': 'form-control'}),
            }

        labels = {
            'cid': 'รหัสลูกค้า',
            'name': 'ชื่อลูหค้า',
            'surname': 'นามสกุล',
            'address': 'ที่อยู่',
            'telephone': 'เบอร์โทร',
            'gender': 'เพศ',
            'carreer': 'ชื่อเข้าใช้',
            'password': 'รหัสผ่าน',
        }
