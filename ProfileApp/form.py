from django import forms
from .models import *


class ProductForm(forms.Form):
    BRAND_LIST = [('Canon', 'Canon'), ('Sony', 'Sony'), ('Nikon', 'Nikon')]
    TYPE_RADIO = [('DSLR', 'DSLR'), ('Mirrorless', 'Mirrorless'), ('Micro Four Thirds', 'Micro Four Thirds')]
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
        fields = ('gid', 'name', 'brand', 'mode', 'price', 'net', 'property', 'goodscategory')
        widgets = {
            'pid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'max_length': 35}),
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

    def updateGoods(self):
        self.fields['gid'].widget.attrs['readonly'] = True
        self.fields['gid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'


# ---------------------------------------
class showcustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cid', 'name', 'surname', 'address', 'telephone', 'gender', 'carreer', 'password')
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

    def updateCustomer(self):
        self.fields['cid'].widget.attrs['readonly'] = True
        self.fields['cid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'


# -----------------ส่วนของminiproject
class showSmeForm(forms.ModelForm):
    class Meta:
        model = Sme
        fields = (
        'sme_id', 'sme_name', 'sme_address', 'sme_zipcode', 'sme_regis', 'sme_history', 'sme_phone', 'sme_agent',
        'sme_objective','customer')
        widgets = {
            'sme_id': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_address': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_regis': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'sme_history': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'sme_agent': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_objective': forms.Textarea(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),

        }
        labels = {
            'sme_id': 'เลขที่ประจำตัวผู้เสียภาษีอากร',
            'sme_name': 'ชื่อกิจการรายย่อย',
            'sme_address': 'ที่อยู่',
            'sme_zipcode': 'รหัสไปรษณีย์',
            'sme_regis': 'วันที่จดทะเบียน',
            'sme_history': 'ประวัติการจดทะเบียน',
            'sme_phone': 'เบอร์โทรศัพท์',
            'sme_agent': 'ชื่อตัวแทน',
            'sme_objective': 'วัตถุประสงค์การก่อตั้ง',
        }

    def updateSme(self):
        self.fields['sme_id'].widget.attrs['readonly'] = True
        self.fields['sme_id'].label = 'รหัสผู้เสียภาษีอากร [ไม่อนุญาตให้แก้ไขได้]'
        self.fields['sme_name'].label = 'ชื่ออกิจการรายย่อย'
        self.fields['sme_address'].label = 'ที่อยู่'
        self.fields['sme_zipcode'].label = 'รหัสไปรษณีย์'
        self.fields['sme_regis'].label = 'วันที่จดทะเบียน'
        self.fields['sme_history'].label = 'ประวัติการจดทะเบียน'
        self.fields['sme_phone'].label = 'เบอร์โทรศัพท์'
        self.fields['sme_agent'].label = 'ชื่อตัวแทน'
        self.fields['sme_objective'].label = 'วัตถุประสงค์การก่อตั้ง'



# ----------------------------------------------------------------------------
class showBorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ('borrow_id', 'borrow_date', 'borrow_type', 'borrow_objective', 'borrow_limitmoney', 'borrow_file',
                  'borrow_status', 'sme_id')
        widgets = {
            'borrow_id': forms.TextInput(attrs={'class': 'form-control'}),
            'borrow_date': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'borrow_type': forms.TextInput(attrs={'class': 'form-control'}),
            'borrow_objective': forms.TextInput(attrs={'class': 'form-control'}),
            'borrow_limitmoney': forms.TextInput(attrs={'class': 'form-control'}),
            'borrow_file': forms.TextInput(attrs={'class': 'form-control'}),
            'borrow_status': forms.TextInput(attrs={'class': 'form-control'}),
            'sme_id': forms.Select(attrs={'class': 'form-control'}),


        }

        labels = {
            'borrow_id': 'รหัสการขอกู้',
            'borrow_date': 'วันที่',
            'borrow_type': 'ประเภทคำขอกู้',
            'borrow_objective': 'จุดประสงค์การกู้',
            'borrow_limitmoney': 'วงเงินขอกู้',
            'borrow_file': 'ไฟล์โครงการ',
            'borrow_status': 'สถานะคำขอกู้',
            'sme_id': 'เลขที่ประจำตัวผู้เสียภาษีอากร',


        }

    def updateBorrowing(self):
        self.fields['borrow_id'].widget.attrs['readonly'] = True
        self.fields['borrow_id'].label = 'รหัสการขอกู้ [ไม่อนุญาตให้แก้ไขได้]'
        self.fields['borrow_date'].label = 'วันที่'
        self.fields['borrow_type'].label = 'ประเภทคำขอกู้'
        self.fields['borrow_objective'].label = 'จุดประสงค์การกู้'
        self.fields['borrow_limitmoney'].label = 'วงเงินขอกู้'
        self.fields['borrow_file'].label = 'ไฟล์โครงการ'
        self.fields['borrow_status'].label = 'สถานะคำขอกู้'
        self.fields['sme_id'].label = 'เลขที่ประจำตัวผู้เสียภาษีอากร'



# ----------------------------------------------------------------------------
class showConsiderationForm(forms.ModelForm):
    class Meta:
        model = Consideration
        fields = ('csd_id', 'csd_date', 'csd_status', 'br_id')
        widgets = {
            'csd_id': forms.TextInput(attrs={'class': 'form-control'}),
            'csd_date': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'csd_status': forms.TextInput(attrs={'class': 'form-control'}),
            'br_id': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'csd_id': 'รหัสผลการพิจารณา',
            'csd_date': 'วันที่',
            'csd_status': 'สถานะ',
            'br_id': 'รหัสการขอกู้',
        }

    def updateConsideration(self):
        self.fields['csd_id'].widget.attrs['readonly'] = True
        self.fields['csd_id'].label = 'รหัสการพิจารณา [ไม่อนุญาตให้แก้ไขได้]'
        self.fields['csd_date'].label = 'วันที่'
        self.fields['csd_status'].label = 'สถานะ'
        self.fields['br_id'].label = 'รหัสการขอกู้'

# ----------------------------------------------------------------------------
class showContractForm(forms.ModelForm):
    class Meta:
        TYPE_RADIO = [('DSLR', 'DSLR'), ('Mirrorless', 'Mirrorless'), ('Micro Four Thirds', 'Micro Four Thirds')]
        model = Contract
        fields = ('ct_id', 'ct_datecontract', 'ct_fine','ct_status','ct_payment','ct_interest','ct_amount','ct_datepayment','ct_dept','ct_limit','br_id')
        widgets = {
            'ct_id': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_datecontract': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'ct_fine': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_status': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_payment': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_interest': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_datepayment': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'ct_dept': forms.TextInput(attrs={'class': 'form-control'}),
            'ct_limit': forms.TextInput(attrs={'class': 'form-control'}),
            'br_id': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'ct_id': 'รหัสการทำสัญญา',
            'ct_datecontract': 'วันที่ทำสัญญา',
            'ct_fine': 'อัตราค่าปรับ',
            'ct_status': 'สถานะสัญญา',
            'ct_payment': 'ยอดชำระต่องวด',
            'ct_interest': 'อัตราดอกเบี้ย',
            'ct_amount': 'จำนวนงวด',
            'ct_datepayment': 'วันที่กำหนดชำระ',
            'ct_dept': 'ยอดหนี้คงเหลือ',
            'ct_limit': 'วงเงินที่อนุมัติ',
            'br_id': 'รหัสการขอกู้',
        }

    def updateContract(self):
        self.fields['ct_id'].widget.attrs['readonly'] = True
        self.fields['ct_id'].label = 'รหัสสัญญากู้ยืม [ไม่อนุญาตให้แก้ไขได้]'
        self.fields['ct_datecontract'].label = 'วันที่ทำสัญญา'
        self.fields['ct_fine'].label = 'อัตราค่าปรับ'
        self.fields['ct_status'].label = 'สถานะสัญญา'
        self.fields['ct_payment'].label = 'ยอดชำระต่องวด'
        self.fields['ct_interest'].label = 'อัตราดอกเบี้ย'
        self.fields['ct_amount'].label = 'จำนวนงวด'
        self.fields['ct_datepayment'].label = 'วันที่กำหนดชำระ'
        self.fields['ct_dept'].label = 'ยอดหนี้คงเหลือ'
        self.fields['ct_limit'].label = 'วงเงินที่อนุมัติ'
        self.fields['br_id'].label = 'รหัสการขอกู้'


# ----------------------------------------------------------------------------
class showPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('pm_id', 'pm_fine', 'pm_status','pm_file','pm_bank','pm_tranfernumber','pm_payment','pm_installment','pm_datepayment','ct_id')
        widgets = {
            'pm_id': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_fine': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_status': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_file': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_bank': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_tranfernumber': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_payment': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_installment': forms.TextInput(attrs={'class': 'form-control'}),
            'pm_datepayment': forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'ct_id': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'pm_id': 'รหัสการชำระ',
            'pm_fine': 'ค่าปรับ',
            'pm_status': 'สถานะการยืนยัน',
            'pm_file': 'ไฟล์สลิป',
            'pm_bank': 'จากธนาคาร',
            'pm_tranfernumber': 'หมายเลขใบโอน',
            'pm_payment': 'ยอดชำระ',
            'pm_installment': 'งวดที่',
            'pm_datepayment': 'วันที่โอนเงิน',
            'ct_id': 'รหัสการทำสัญญา',
        }

    def updatePayment(self):
        self.fields['pm_id'].widget.attrs['readonly'] = True
        self.fields['pm_id'].label = 'รหัสการชำระ'
        self.fields['pm_fine'].label = 'ค่าปรับ'
        self.fields['pm_status'].label = 'สถานะการยืนยัน'
        self.fields['pm_file'].label = 'ไฟล์สลิป'
        self.fields['pm_bank'].label = 'จากธนาคาร'
        self.fields['pm_tranfernumber'].label = 'หมายเลขใบโอน'
        self.fields['pm_payment'].label = 'ยอดชำระ'
        self.fields['pm_installment'].label = 'งวดที่'
        self.fields['pm_datepayment'].label = 'วันที่โอนเงิน'
        self.fields['ct_id'].label = 'รหัสการทำสัญญา'



#--------form---------------------------------------------
class ChangePasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=50,
                             widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    oldPassword = forms.CharField(label='รหัสผ่านเดิม', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=100,
                                      widget=forms.PasswordInput(attrs={'class':'form-control'}))
class ResetPasswordForm(forms.Form):
    userId = forms.CharField(label='รหัสประจำตัวผู้ใช้', max_length=50,
                             widget=forms.TextInput(attrs={'class':'form-control', 'readonly':True}))
    newPassword = forms.CharField(label='รหัสผ่านใหม่', max_length=100,
                                  widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirmPassword = forms.CharField(label='ยืนยันรหัสผ่านใหม่',  max_length=100,
                                      widget=forms.PasswordInput(attrs={'class':'form-control'}))

class EmployeesForm(forms.ModelForm):
    class Meta:
        STATUS_CHOICES = (
            ("Manager", "Manager"),
            ("Employee", "Employee"),
            ("Store", "Store"),
        )
        model = Employees
        fields = ('eid', 'name', 'birthdate', 'position', 'password')
        widgets = {
            'eid': forms.TextInput(attrs={'class': 'form-control', 'size':15, 'maxlength':13}),
            'name': forms.TextInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
            'birthdate':forms.NumberInput(attrs={'class': 'form-control',   'type': 'date'}),
            'position': forms.Select(choices=STATUS_CHOICES, attrs={'class': 'form-control'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control',  'size':55, 'maxlength':50}),
        }

        labels = {
            'eid': 'รหัสพนักงาน',
            'name': 'ชื่อพนักงาน',
            'birthdate': 'วันเดือนปีเกิด',
            'position': 'ตำแหน่ง',
            'password' : 'รหัสผ่าน'
        }

    def updateForm(self):
        self.fields['eid'].widget.attrs['readonly'] = True
        self.fields['eid'].label = 'รหัสพนักงาน [ไม่อนุญาตให้แก้ไขได้]'
        self.fields['password'].widget = forms.HiddenInput()

    def deleteForm(self):
        self.fields['eid'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['birthdate'].widget.attrs['readonly'] = True
        self.fields['position'].widget.attrs['readonly'] = True
        self.fields['password'].widget = forms.HiddenInput()

class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('name', 'address', 'tel', 'cid', 'password')
        widgets = {

            'cid': forms.TextInput(attrs={'class': 'form-control', 'size':15, 'maxlength':13}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'tel': forms.TextInput(attrs={'class': 'form-control','size':13, 'maxlength':10}),
            'password':forms.PasswordInput(attrs={'class': 'form-control',   'size':13, 'maxlength':10}),

        }
        labels = {
            'name': 'ชื่อลูกค้า',
            'address': 'ที่อยู่',
            'tel': 'เบอร์โทรศัพท์',
            'cid': 'รหัสประจำตัว (User Name)',
            'password': 'รหัสผ่าน (Password)',
        }

    def updateForm(self):
        self.fields['cid'].widget.attrs['readonly'] = True
        self.fields['cid'].label=' User Name '
        self.fields['password'].widget = forms.HiddenInput()
#--------------------------------------admin---------------------------------
