from django.forms import ModelForm
from .models import Mensajes


class MensajesForm(ModelForm):


    class Meta:
        model = Mensajes
        fields = '__all__'
