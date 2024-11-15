from django.forms import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Course, Category, CourseSyllabus, Modelset, Questions, Result, Syllabus, QuizGroup, StudentGroup
from users.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import urllib



''' Views to display the courses (mcq) to select '''
def course(request):
    template_name = 'quiz/course.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses':courses})


''' Views to display the real courses '''
def courses(request):
    template_name = 'quiz/courses.html'
    return render(request, template_name)


''' Views to display the syllabus'''
def syllabus(request):
    template_name = 'quiz/syllabus.html'
    s_courses = CourseSyllabus.objects.all()
    return render(request, template_name, {'SyllabusCourse': s_courses})


def syllabus_details(request, id):
    template_name = 'quiz/syllabus_details.html'
    syllabuses = Syllabus.objects.filter(syllabus_for=id)
    return render(request, template_name, {'syllabuses': syllabuses})


''' View to display the category of the selected course '''
def category(request, slug):
    template_name = 'quiz/category.html'
    course = Course.objects.get(slug=slug)
    category_list = Category.objects.filter(course=course.id)
    return render(request, template_name, {'category': category_list, 'level': course})


''' Views to display the list of modelsets '''
def modelsets(request, id):
    template_name = 'quiz/modelset.html'
    category = Category.objects.get(id=id)
    modelsets = Modelset.objects.filter(category=category.id, active=True)
    return render(request, template_name, {'modelsets': modelsets, 'category': category})


# ''' Views to display the questions and mcqs of the related modelset '''
# @login_required(login_url="/login")
# def mcq(request, id):
#     current_user = request.user
#     target_modelset = Modelset.objects.get(id=id)
#     searching_result = Result.objects.filter(modelset=id)
    
#     already_taken = 0
#     for result in searching_result:
#         if (result.user== current_user ) and (result.modelset == target_modelset):
#             already_taken = 1

#     if request.method == 'POST':
#         modelset = Modelset.objects.get(id=id)
#         questions=Questions.objects.filter(modelset=modelset.id)
#         user = request.user.id
#         weightage = modelset.weightage
#         score=0
#         unanswered = 0
#         wrong=0
#         correct=0
#         total=0
#         xya_dict = {}
#         for q in questions:
#             x=request.POST.get(q.question_statement)
#             # user_answer_list.append(x)

#             xya_dict.update({
#                 'xyz'+str(q.id):{
#                     "q": q.question_statement,
#                     "choice_1": q.choice_1,
#                     "choice_2": q.choice_2,
#                     "choice_3": q.choice_3,
#                     "choice_4": q.choice_4,
#                     "answer": q.answer,
#                     "explanation": q.explanation,
#                     "user_ans": x,
#                 }
#             })
#             total+=1
#             if q.answer == request.POST.get(q.question_statement):
#                 score+=weightage
#                 correct+=1
#             elif request.POST.get(q.question_statement)==None:
#                 unanswered+=1
#             else:
#                 wrong+=1
#         percent = score/(total*weightage) *100

#         # create object of Result and save the result
#         try:
#             result = Result(
#                 user=request.user,
#                 modelset=modelset,
#                 markes_obtained=score,
#                 correct=correct,
#                 wrong=wrong,
#                 unanswered=unanswered
#             )
#             result.save()            
#         except:
#             raise ValueError("Value Error")
        
#         # remove user from QuizGroup on successful creation of Result
#         try:
#             quizgroup = QuizGroup.objects.get(modelset=target_modelset)
#             quizgroup.users.remove(request.user)
#         except:
#             raise ValidationError()

#         # context = 
#         return render(request,'quiz/result.html',{
#             'questions':questions,
#             'score':score,
#             'correct':correct,
#             'wrong':wrong,
#             'unanswered':unanswered,
#             'percent':percent,
#             'total':total,
#             'xya_dict': xya_dict
#         })
      
#     elif request.method == 'GET':
#         """ 
#         if user is in QuizGroup then only render quiz/mcqs.html
#         else if check if user has taken the test, if yes then disply latest result page
#         else render payemtn page
        
#         """
#         try:
#             allowed_users = QuizGroup.objects.get(modelset=target_modelset).get_users()
#             if request.user in allowed_users:       
#                 template_name = 'quiz/mcqs.html'
#                 user = request.user
#                 modelset = Modelset.objects.get(id=id)
#                 question_set = Questions.objects.filter(modelset=modelset.id)
#                 return render(request, template_name, {'question': question_set, 'user': user, 'modelset': modelset})
#             else:
#                 if already_taken == 1:
#                     template_name = 'quiz/already_taken_result.html'
#                     for result_marks in searching_result:
#                         if result_marks.user == current_user:
#                             marks_obtained = result_marks.markes_obtained
#                             correct = result_marks.correct
#                             wrong = result_marks.wrong
#                             unanswered = result_marks.unanswered
#                             datetime = result_marks.datetime

#                     return render(request, template_name,{
#                         'marks_obtained':marks_obtained,
#                         'correct':correct,
#                         'wrong':wrong,
#                         'unanswered': unanswered,
#                         'datetime':datetime,
#                     }) 
#                 return render(request, 'quiz/make_payment.html')
#         except QuizGroup.DoesNotExist:
#             return render(request, 'quiz/group_doesnt_exists.html', {'modelset': target_modelset})

#     return render(request, 'quiz/method_not_allowed.html')


''' Views to display the questions and mcqs of the related modelset '''
@login_required(login_url="/login")
def mcq(request, id):
    current_user = request.user
    target_modelset = Modelset.objects.get(id=id)
    searching_result = Result.objects.filter(modelset=id)
    
    already_taken = 0
    allow_again = 1

    ''' Students Group '''
    try:
        our_students = StudentGroup.objects.first().get_users()
    except:
        return render(request, template_name='courses/groupdoesnotexist.html')
    he_is_a_student = 0
    if request.user in our_students:
        he_is_a_student = 1

    for result in searching_result:
        if (result.user== current_user ) and (result.modelset == target_modelset):
            already_taken = 1
            allow_again = 0

    # quizgroup = QuizGroup.objects.get(modelset=target_modelset)  
    allowed_users = QuizGroup.objects.get(modelset=target_modelset).get_users()

    if request.method == 'POST' and allow_again == 1:
        modelset = Modelset.objects.get(id=id)
        questions=Questions.objects.filter(modelset=modelset.id)
        user = request.user.id
        weightage = modelset.weightage
        score=0
        unanswered = 0
        wrong=0
        correct=0
        total=0
        xya_dict = {}
        for q in questions:
            x=request.POST.get(q.question_statement)
            # user_answer_list.append(x)
            print('x')
            print(x)

            xya_dict.update({
                'xyz'+str(q.id):{
                    "q": q.question_statement,
                    "choice_1": q.choice_1,
                    "choice_2": q.choice_2,
                    "choice_3": q.choice_3,
                    "choice_4": q.choice_4,
                    "answer": q.answer,
                    "explanation": q.explanation,
                    "user_ans": x,
                }
            })
            total+=1
            if q.answer == request.POST.get(q.question_statement):
                score+=weightage
                correct+=1
            elif request.POST.get(q.question_statement)==None:
                unanswered+=1
            else:
                wrong+=1
        percent = score/(total*weightage) *100

        # create object of Result and save the result
        try:
            result = Result(
                user=request.user,
                modelset=modelset,
                markes_obtained=score,
                correct=correct,
                wrong=wrong,
                unanswered=unanswered
            )

            quizgroup = QuizGroup.objects.get(modelset=target_modelset)
            quizgroup.users.remove(request.user)       

            result.save()     
            allow_again = 0
        except:
            raise ValueError("Value Error")
        
        # remove user from QuizGroup on successful creation of Result
        try:
            quizgroup = QuizGroup.objects.get(modelset=target_modelset)
            quizgroup.users.remove(request.user)
        except:
            raise ValidationError()

        return render(request,'quiz/result.html',{
            'modelset': target_modelset,
            'questions':questions,
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'unanswered':unanswered,    
            'percent':percent,
            'total':total,
            'xya_dict': xya_dict
        })

        # return redirect('/quiz/result/?questions=' + str(questions) + '&score=' + str(score) + '&correct=' + str(correct) + '&wrong=' + str(wrong) + '&unanswered=' + str(unanswered) + '&percent=' + str(percent) + '&total=' + str(total) + '&xya_dict=' + urllib.parse.urlencode(xya_dict))

      
    elif request.method == 'GET':
        """ 
        if user is in QuizGroup then only render quiz/mcqs.html
        else if check if user has taken the test, if yes then disply latest result page
        else render payment page
        
        """
        try:
            allowed_users = QuizGroup.objects.get(modelset=target_modelset).get_users()
            quiz_group = QuizGroup.objects.get(modelset=target_modelset)
            if target_modelset.free == True:
                template_name = 'quiz/mcqs.html'
                user = request.user
                modelset = Modelset.objects.get(id=id)
                question_set = Questions.objects.filter(modelset=modelset.id)
                return render(request, template_name, {'question': question_set, 'user': user, 'modelset': modelset})

            elif request.user in allowed_users or (he_is_a_student == 1 and quiz_group.allow_students == True and allow_again == 1) :       
                template_name = 'quiz/mcqs.html'
                user = request.user
                modelset = Modelset.objects.get(id=id)
                question_set = Questions.objects.filter(modelset=modelset.id)
                return render(request, template_name, {'question': question_set, 'user': user, 'modelset': modelset})
            else:
                if already_taken == 1:
                    template_name = 'quiz/already_taken_result.html'
                    for result_marks in searching_result:
                        if result_marks.user == current_user:
                            marks_obtained = result_marks.markes_obtained
                            correct = result_marks.correct
                            wrong = result_marks.wrong
                            unanswered = result_marks.unanswered
                            datetime = result_marks.datetime
                            modelset = Modelset.objects.get(id=id)
                            question_set = Questions.objects.filter(modelset=modelset.id)


                    return render(request, template_name,{
                        'marks_obtained':marks_obtained,
                        'correct':correct,
                        'wrong':wrong,
                        'unanswered': unanswered,
                        'datetime':datetime,
                        'question': question_set,
                        'modelset': modelset
                    }) 
                return render(request, 'quiz/make_payment.html')
        except QuizGroup.DoesNotExist:
            return render(request, 'quiz/group_doesnt_exists.html', {'modelset': target_modelset})

    return render(request, 'quiz/method_not_allowed.html')

def result_view(request):
    template_name = 'quiz/result.html'
    return render(request, template_name, {
            'questions':request.GET.get('questions'),
            'score':request.GET.get('score'),
            'correct':request.GET.get('correct'),
            'wrong':request.GET.get('wrong'),
            'unanswered':request.GET.get('unanswered'),    
            'percent':request.GET.get('percent'),
            'total':request.GET.get('total'),
            'xya_dict': request.GET.get('xya_dict')
        })

''' Download pdf '''
def render_pdf_view(request, id):
    template_path = 'quiz/questions_print.html'
    modelset = Modelset.objects.get(id=id)
    question_set = Questions.objects.filter(modelset=modelset.id)
    context = {'question': question_set, 'modelset': modelset}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="questions.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
