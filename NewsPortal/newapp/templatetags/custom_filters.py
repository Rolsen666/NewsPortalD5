from django import template

register = template.Library()


@register.filter()
def censor(value):
    censorship = ['домой', 'выезжаю', 'золотую']
    if not isinstance(value,str):
        raise ValueError('Нельзя цензурировать не строку')
    for i in censorship:
        value = value.replace(i[1:], "*" * (len(i)-1))
    return value


