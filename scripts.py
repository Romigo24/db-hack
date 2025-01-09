def fix_marks(schoolkid):
    bad_grades = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for grade in bad_grades:
        grade.points = 5
        grade.save()


def remove_chastisements(schoolkid):
    comments = Chastisement.objects.filter(schoolkid=schoolkid)
    comments.delete()

def get_schoolkid_name(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'. Пожалуйста, уточните запрос.")
        return None
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return None

def create_commendation(schoolkid_name, subject_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=schoolkid_name).first()
    subject_name = Subject.objects.get(title=subject_name, year_of_study=6)
    lesson = Lesson.objects.filter(subject=subject_name, year_of_study=6, group_letter='А').order_by('-date').first()
    subject = lesson.subject
    teacher = lesson.teacher
    date = lesson.date
    commendation_texts = [
        'Хвалю!',
        'Молодец!',
        'Отлично!',
        'Великолепно!',
        'Замечательно!'
    ]
    text = random.choice(commendation_texts)
    new_commendation = Commendation.objects.create(text=text, created=date, schoolkid=schoolkid, subject=subject, teacher=teacher)