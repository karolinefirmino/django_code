from django import forms
from juris.fields import ListTextWidget

from django import forms
from juris.models import Cadastro
import base64



from bootstrap_datepicker_plus import DatePickerInput
from django import forms
#from .models import Document

class ProcessoForm(forms.ModelForm):
  #class Meta:
  model = Cadastro
  fields = '__all__'
  #code = base64.b64encode(fields)

   

    #este widget ainda não está funcionando
  widgets = {
        'dataJulgamento': DatePickerInput(format='%d/%m/%Y'), # specify date-frmat
  }



class FormForm(forms.Form):
   char_field_with_list = forms.CharField(required=True)

   def __init__(self, *args, **kwargs):
      _tribunal_list = kwargs.pop('data_list', None)
      super(FormForm, self).__init__(*args, **kwargs)

    # the "name" parameter will allow you to use the same widget more than once in the same
    # form, not setting this parameter differently will cuse all inputs display the
    # same list.
      self.fields['char_field_with_list'].widget = ListTextWidget(data_list=_tribunal_list, name='tribunal_list')


#class EventForm(forms.ModelForm):
    #class Meta:
        #model = Cadastro
        #fields = ['dataJulgamento']
        #widgets = {
            #'dataJulgamento': DatePickerInput(format='%d/%m/%Y'), # specify date-frmat
        #}


#class DocumentForm(forms.Form):
    #docfile = forms.FileField(
        #label='Select a file',
        #help_text='max. 42 megabytes'
    #)