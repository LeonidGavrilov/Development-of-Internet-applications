from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс товара'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Дата публикации товара'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Характеристики товара'
            }),
            'image': FileInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Изображение'
            })
        }