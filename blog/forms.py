from django import forms
from recaptcha_works.fields import RecaptchaField

class CommentForm(forms.Form):
    captcha = RecaptchaField("Human Test", required=True)
    username = forms.CharField()
    url = forms.CharField()
    comment = forms.CharField()

