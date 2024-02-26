from django import forms


class UserForm(forms.Form):
    game = forms.ChoiceField(choices=[['C', 'Бросить монету'], ['D', 'Бросить игральную кость'], ['R', 'Сгенерировать случайное число']], label='Игра')
    count = forms.IntegerField(min_value=1, max_value=120, label='Кол-во попыток')
