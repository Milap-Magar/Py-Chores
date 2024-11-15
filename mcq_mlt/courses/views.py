from urllib import request
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404


from quiz.models import StudentGroup
from .models import SubjectGroup, Subjects, Units, Chapters, Questions, UsersReadChapters, ChapterWiseModelset


''' Views to display the subjects '''


def subject(request):
    template_name = 'courses/subject.html'
    subjects = Subjects.objects.all()
    
    sub_dict = {}
    for subb in subjects:
        sgroup = SubjectGroup.objects.filter(subject = subb.id)
        if (sgroup):
            sub_dict.update({
                'sub'+str(subb.id):{
                    "id": subb.id,
                    "name": subb.name,
                    "description": subb.description,
                    "image": subb.image,
                    "created": subb.created_on,
                }
            })
        print('sgroup')
        print(sgroup)

    return render(request, template_name, {'subjects': subjects, 'subb': sub_dict})


''' Views to display the units '''

def unit(request, id):
    template_name = 'courses/units.html'
    subject = Subjects.objects.get(id=id)
    units = Units.objects.filter(subject=id)

    read_dict ={}
    for x in units:
        readchapters = UsersReadChapters.objects.filter(unit=x.id).count()
        chapters_in_unit = Chapters.objects.filter(unit=x.id).count()
        if chapters_in_unit>0:
            percent  = readchapters/chapters_in_unit*100
        else:
            percent = 0.0
        read_dict.update({
            'unit'+str(x.id):{
                "percent": percent,
                "unit": x.name,
                "id": x.id
            } 
        })
    return render(request, template_name, {'units': units, 'subject': subject, 'read_dict': read_dict})


''' Views to display the chapters'''


def chapter(request, id):
    template_name = 'courses/chapterss.html'
    unit = Units.objects.get(id=id)
    chapterss = Chapters.objects.filter(unit=id)

    return render(request, template_name, {'unit': unit, 'chapterss': chapterss})


''' Views to display the chapters'''


@login_required(login_url='login')
def chapterdetails(request, id):
    template_name = 'courses/chapterdetails.html'
    chapterss = Chapters.objects.get(id=id)
    unit = chapterss.unit
    unit_name = Units.objects.get(name=unit)
    all_chapters = Chapters.objects.filter(unit=unit.id)
    # has_student_group = False
    # has_subject_group = False
    userreadchapters = UsersReadChapters.objects.filter(chapter=id)

    if StudentGroup.objects.exists():
        allowed_students = StudentGroup.objects.prefetch_related(Prefetch('users')).first().get_users(
        ) | SubjectGroup.objects.prefetch_related(Prefetch('users')).get(subject=chapterss.subject).get_users()
    else:
        allowed_students = get_object_or_404(
            SubjectGroup, subject=chapterss.subject).get_users()

    if request.user in allowed_students:
        for userread in userreadchapters:
            if userread.users == request.user:
                chapterwise_modelset = ChapterWiseModelset.objects.filter(
                    chapter=id)

                return render(request, 'courses/read_completed_chapter.html', {'unit_name': unit_name, 'chapterss': chapterss, 'all_chapters': all_chapters, 'chapterwise_modelset': chapterwise_modelset})
            else:
                return render(request, template_name, {'unit_name': unit_name, 'chapterss': chapterss, 'all_chapters': all_chapters})

        return render(request, template_name, {'unit_name': unit_name, 'chapterss': chapterss, 'all_chapters': all_chapters})
    return render(request, 'quiz/make_payment.html')


''' Views to display the read completed chapters details'''
def read_completed_chapter(request, id):
    template_name = 'courses/read_completed_chapter.html'

    chapterss = Chapters.objects.get(id=id)
    unit = chapterss.unit

    unit_name = Units.objects.get(name=unit)
    all_chapters = Chapters.objects.filter(unit=unit.id)

    chapterwise_modelset = ChapterWiseModelset.objects.filter(chapter=id)
   
    # create object of Read and save the Read

    try:
        read = UsersReadChapters(
            chapter_name = chapterss.name,
            unit = unit_name,
            chapter = chapterss,
            users = request.user
        )

        read.save()
    except:
        raise ValueError("Value Error")

    return render(request, template_name, {'unit_name': unit_name, 'chapterss': chapterss, 'all_chapters': all_chapters, 'chapterwise_modelset': chapterwise_modelset})


''' Chapterwise mcq '''


def chapterwise_mcq(request, id):
    template_name = 'courses/chapterwisemcq.html'
    modelset = ChapterWiseModelset.objects.get(id=id)
    print('modelset.chapter')
    print(modelset.chapter)
    question_set = Questions.objects.filter(modelset=modelset.id)
    chapter = Chapters.objects.get(name=modelset.chapter)

    if request.method == 'POST':
        user = request.user.id
        score = 0
        unanswered = 0
        wrong = 0
        correct = 0
        total = 0
        xya_dict = {}
        for q in question_set:
            x = request.POST.get(q.question_statement)
            # user_answer_list.append(x)
            print('x')
            print(x)

            xya_dict.update({
                'xyz'+str(q.id): {
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
            total += 1
            if q.answer == request.POST.get(q.question_statement):
                score += 1
                correct += 1
            elif request.POST.get(q.question_statement) == None:
                unanswered += 1
            else:
                wrong += 1
        percent = score/(total*1) * 100

        return render(request, 'courses/chaptermcq_result.html', {
            'modelset': modelset,
            'questions': question_set,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'unanswered': unanswered,
            'percent': percent,
            'total': total,
            'chapter': chapter,
            'xya_dict': xya_dict,
        })

    elif request.method == 'GET':
        template_name = 'courses/chapterwisemcq.html'
        user = request.user
        modelset = ChapterWiseModelset.objects.get(id=id)
        question_set = Questions.objects.filter(modelset=modelset.id)
        return render(request, template_name, {'question': question_set, 'user': user, 'modelset': modelset, 'chapter': chapter})

    return render(request, 'quiz/method_not_allowed.html')
