def fix_marks(schoolkid):
    get_schoolkid_name(schoolkid)
    bad_grades = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    get_schoolkid_name(schoolkid)
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

def get_subject_name_and_year(subject_name, year_of_study):
    subject = Subject.objects.get(title=subject_name, year_of_study=year_of_study)
    return subject



def create_commendation(schoolkid_name, subject_name):
    schoolkid = get_schoolkid_name(schoolkid_name)
    subject_name = get_subject_name_and_year(subject_name, schoolkid.year_of_study)
    lesson = Lesson.objects.filter(subject=subject_name, year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter).order_by('-date').first()
    if not lesson:
        print(f'Нет уроков по предмету {subject_name} для {schoolkid.year_of_study}{schoolkid.group_letter}')
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