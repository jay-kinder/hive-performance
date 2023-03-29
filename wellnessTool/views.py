from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from functions import average, stdev
from .forms import QuestionnaireForm
from .models import Question, Choice
from datetime import date

def questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid(): 
            choice_list = []
            choice1 = request.POST.get("question1")
            choice2 = request.POST.get("question2")
            choice3 = request.POST.get("question3")
            choice4 = request.POST.get("question4")
            choice_list.extend([choice1, choice2, choice3, choice4])
            question_id_list = Question.objects.values_list('id', flat=True)
            for (choice, qid) in zip(choice_list, question_id_list):
                submission = Choice(choice_num=choice, question_id=qid)
                submission.save()
            return HttpResponseRedirect('/wellnessTool')
        return render(request, 'questionnaire.html', {'form': form})
    else:
        form = QuestionnaireForm()
        if Choice.objects.filter(date_submit=date.today().strftime('%Y-%m-%d')).exists():
            submit_today = True
        else:
            submit_today = False
        return render(request, 'questionnaire.html', {'form': form, 'submit_today': submit_today})

def stats(request):
    q1_answers_list = []
    for answer in Choice.objects.values_list('choice_num', flat=True).filter(question_id=1):
        q1_answers_list.append(answer)
    q2_answers_list = []
    for answer in Choice.objects.values_list('choice_num', flat=True).filter(question_id=2):
        q2_answers_list.append(answer)
    q3_answers_list = []
    for answer in Choice.objects.values_list('choice_num', flat=True).filter(question_id=3):
        q3_answers_list.append(answer)
    q4_answers_list = []
    for answer in Choice.objects.values_list('choice_num', flat=True).filter(question_id=4):
        q4_answers_list.append(answer)    

    if len(q1_answers_list) != 0:
        q1_today = q1_answers_list[-1]
        q2_today = q2_answers_list[-1]
        q3_today = q3_answers_list[-1]
        q4_today = q4_answers_list[-1]
    
        q1_average = average(q1_answers_list)
        q2_average = average(q2_answers_list)
        q3_average = average(q3_answers_list)
        q4_average = average(q4_answers_list)
        
        q1_previous_average = average(q1_answers_list[:-1])
        q2_previous_average = average(q2_answers_list[:-1])
        q3_previous_average = average(q3_answers_list[:-1])
        q4_previous_average = average(q4_answers_list[:-1])

        q1_sd = stdev(q1_answers_list[:-1])
        q2_sd = stdev(q2_answers_list[:-1])
        q3_sd = stdev(q3_answers_list[:-1])
        q4_sd = stdev(q4_answers_list[:-1])

        q1_check_sd = round(abs(q1_previous_average - q1_today), 1)
        q2_check_sd = round(abs(q2_previous_average - q2_today), 1)
        q3_check_sd = round(abs(q3_previous_average - q3_today), 1)
        q4_check_sd = round(abs(q4_previous_average - q4_today), 1)

        date_submitted_raw = Choice.objects.values_list('date_submit', flat=True)
        date_submitted_no_duplicates = list(dict.fromkeys(date_submitted_raw))
        date_submitted = []
        for item in date_submitted_no_duplicates:
            date_submitted.append(item.strftime('%Y-%m-%d'))

        wellness_score_list = []
        for item in date_submitted:
            wellness_score_list.append(sum(Choice.objects.values_list('choice_num', flat=True).filter(date_submit=item)))
        
        wellness_score_today = wellness_score_list[-1]
        wellness_score_average = average(wellness_score_list)
        wellness_score_previous_average = average(wellness_score_list[:-1])
        wellness_score_sd = stdev(wellness_score_list[:-1])
        wellness_score_check_sd = round(abs(wellness_score_previous_average - wellness_score_today), 1)
        wellness_score_31days = wellness_score_list[0:31]
        
        context = {
            'q1_today': q1_today, 
            'q2_today': q2_today,
            'q3_today': q3_today,
            'q4_today': q4_today,
            'q1_average': q1_average, 
            'q2_average': q2_average,
            'q3_average': q3_average,
            'q4_average': q4_average,
            'q1_sd': q1_sd,
            'q2_sd': q2_sd,
            'q3_sd': q3_sd,
            'q4_sd': q4_sd,
            'q1_check_sd': q1_check_sd,
            'q2_check_sd': q2_check_sd,
            'q3_check_sd': q3_check_sd,
            'q4_check_sd': q4_check_sd,
            'wellness_score_31days': wellness_score_31days,
            'wellness_score_today': wellness_score_today,
            'wellness_score_average': wellness_score_average,
            'wellness_score_sd': wellness_score_sd,
            'wellness_score_check_sd': wellness_score_check_sd,
            'date_submitted': date_submitted,
        }
        return render(request, 'stats.html', context)
    else:
        return render(request, 'stats.html')