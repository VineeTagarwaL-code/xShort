from django import forms

class take_userinput(forms.Form):
    user_link = forms.URLField(required=True , label="" , )
    user_linkname= forms.CharField(required=True , label="")
    user_link.widget.attrs.update({'class':'input'} )
    user_link.widget.attrs.update({'placeholder':'Your Link'} )
    user_linkname.widget.attrs.update({'class':'input'  })
    user_linkname.widget.attrs.update({'placeholder':'Desired Name'} )
    