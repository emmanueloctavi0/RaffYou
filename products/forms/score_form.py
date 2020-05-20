
# Django
from django import forms
from django.utils.translation import gettext_lazy as _

# Models
from products.models import Score


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = [
            'rate',
            'comment',
        ]

        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Agregar un comentario',
                    'rows': 3,
                    'class': 'form-control',
                }
            )
        }

        error_messages = {
            'rate': {
                'required': _("Es necesario marcar una calificación"),
            },
        }
