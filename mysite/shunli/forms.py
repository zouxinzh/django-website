from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        labels = {
            'name':'姓名',
            'email':'邮件',
            'phone':'电话',
            'company':'公司',
            'message':'详情'
                
        }
        fields = ('name','email','phone', 'company','message')