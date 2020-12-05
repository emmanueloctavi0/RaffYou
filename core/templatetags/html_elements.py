
# Django
from django import template

register = template.Library()


@register.inclusion_tag('generals/input_form.html', takes_context=True)
def input_form(context, field, col=8, input_type=None):

    value = field.value() or ''

    if field.errors and context['request'].method == 'POST':
        classes = 'is-invalid'
    elif not field.errors and context['request'].method == 'POST':
        classes = 'is-valid'
    else:
        classes = ''

    if not input_type:
        input_type = field.field.widget.input_type

    return {
        'field': field,
        'col': col,
        'value': value,
        'classes': classes,
        'type': input_type,
        'required': field.field.required
    }


@register.inclusion_tag('generals/textarea_form.html', takes_context=True)
def textarea_form(context, field, col=8, cols=57, rows=4):
    value = field.value() or ''

    if field.errors and context['request'].method == 'POST':
        classes = 'is-invalid'
    elif not field.errors and context['request'].method == 'POST':
        classes = 'is-valid'
    else:
        classes = ''

    return {
        'field': field,
        'col': col,
        'value': value,
        'classes': classes,
        'cols': cols,
        'rows': rows,
        'required': field.field.required
    }


@register.inclusion_tag('generals/yes_no_modal.html', takes_context=True)
def yes_no_modal(context, msg):
    return {
        'msg': msg,
    }
