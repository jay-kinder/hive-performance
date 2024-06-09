from django import forms
from .models import Question, Choice


class QuestionnaireForm(forms.Form):
    question_list = Question.objects.all()
    choices = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    ]
    question1 = forms.ChoiceField(
        label=question_list[0], choices=choices, widget=forms.RadioSelect()
    )
    question2 = forms.ChoiceField(
        label=question_list[1], choices=choices, widget=forms.RadioSelect()
    )
    question3 = forms.ChoiceField(
        label=question_list[2], choices=choices, widget=forms.RadioSelect()
    )
    question4 = forms.ChoiceField(
        label=question_list[3], choices=choices, widget=forms.RadioSelect()
    )
