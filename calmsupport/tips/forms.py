from django import forms 
# from tips import models
from tips.models import Message

class MessageForm(forms.ModelForm):
    description = forms.Textarea()
    video = forms.FileField(label="Video", required=False)
    audio = forms.FileField(label="Audio", required=False)
    image = forms.ImageField(label="Reference Image", required=False)
    location = forms.CharField(max_length=100, label="Accident Location", required=False)
    event_date = forms.DateTimeField(label="Accident Date", widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Message
        fields = ("title", "description","video","audio","image", "location", "event_date")
        

    def str(self):
        return self.title