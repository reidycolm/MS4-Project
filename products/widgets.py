from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomFileInput(ClearableFileInput):
    ''' clearable file input for use with adding
        and removing images
    '''
    clear_checkbox_label = _('Remove')
    initial_text = ('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_file_input.html'
