from django import forms


STATUS_CHOICES=[
    (0,'Draft'),
    (1,'Publish'),
]

AUTHOR_CHOICES=[
    (0,"------"),
    ("yogita","yogita"),
]

class Addform(forms.Form):
      title= forms.CharField(max_length=200)
      author=forms.CharField(label="who is author of your Blog",widget= forms.Select(choices=AUTHOR_CHOICES))
      content= forms.CharField()
      status= forms.CharField(label="what do you wanna do with your Blog",widget=forms.Select(choices=STATUS_CHOICES))