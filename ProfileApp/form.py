# from django import forms
# class ProductForm(forms.Form):
#     BRAND_LIST =[('acer', 'acer thailand'),('asus', 'asus thailand'),('samsung', 'sumsung thailand'),('hp', 'hp thailand')]
#     id = forms.CharField(max_lenght=13, label="รหัสสินค้า",required=True, widget=forms.TextInput(attrs={'size':15}))
#     name = forms.CharField(max_lenght=50, label="ชื่อสินค้า", required=True, widget=forms.TextInput(attrs={'size': 55}))
#     brand = forms.CharField(max_lenght=30, label="ยี่ห้อ", required=True, widget=forms.Select(choices=BRAND_LIST))
#     price = forms.CharField(max_lenght=1.00,max_value=100000.00, label="ราคาต่อหน่วย", required=True, widget=forms.NumberInput(attrs={'size': 10}))
#     net = forms.IntegerField(max_lenght=0, label="คงเหลือ", required=True, widget=forms.NumberInput(attrs={'size': 10}))