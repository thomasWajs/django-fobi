from __future__ import absolute_import

__title__ = 'fobi.contrib.plugins.form_elements.fields.regex.fobi_form_elements'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2014-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('RegexInputPlugin',)

from django.forms.fields import RegexField
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _

from fobi.base import FormFieldPlugin, form_element_plugin_registry, get_theme
from fobi.contrib.plugins.form_elements.fields.regex import UID
from fobi.contrib.plugins.form_elements.fields.regex.forms import RegexInputForm

theme = get_theme(request=None, as_instance=True)

class RegexInputPlugin(FormFieldPlugin):
    """
    Regex field plugin.
    """
    uid = UID
    name = _("Regex")
    group = _("Fields")
    form = RegexInputForm

    def get_form_field_instances(self):
        """
        Get form field instances.
        """
        widget_attrs = {
            'class': theme.form_element_html_class,
            'placeholder': self.data.placeholder,
        }

        kwargs = {
            'label': self.data.label,
            'help_text': self.data.help_text,
            'regex': self.data.regex,
            'initial': self.data.initial,
            'required': self.data.required,
            'widget': TextInput(attrs=widget_attrs),
        }

        if self.data.max_length:
            kwargs['max_length'] = self.data.max_length

        return [(self.data.name, RegexField, kwargs)]


form_element_plugin_registry.register(RegexInputPlugin)
