from quiz.models import Course, CourseSyllabus
from courses.models import Subjects, SubjectGroup


def extras(request):
    levels = Course.objects.all()
    subjects = Subjects.objects.all()
    syllabus = CourseSyllabus.objects.all()

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

    return {'consyllabus': syllabus, 'conlevels': levels, 'consubjects': subjects, 'subb': sub_dict}
