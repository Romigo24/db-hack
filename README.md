# db-hack
# Управление оценками учеников в системе
Этот проект включает в себя несколько функций для управления оценками, похвалами и замечаниями учеников в системе. Функции обеспечивают изменение плохих оценок на хорошие, добавление похвал, удаление замечаний и поиск учеников по имени.

## Функции 
#### fix_marks(schoolkid)

Исправляет низкие оценки ученика, заменяя их на макимально хорошую оценку.

###### Пример использования 

```pyrhon
schoolkid = get_schoolkid_name('Иванов Иван')
fix_marks(schoolkid)
```
#### remove_chastisements(schoolkid)

Удаляет все замечания ученика

###### Пример использования 

```python
schoolkid = get_schoolkid_name('Иванов Иван')
remove_chastisements(schoolkid)
```
#### get_schoolkid_name(schoolkid_name)

Находит ученика по полному имени. Если найдено несколько учеников с одинаковым именем, сообщает об этом.

###### Пример использования

```python
get_schoolkid_name('Иванов Иван')
```

#### create_comendation(schoolkid_name, subject_name)

Создаёт похвалу для ученика и указанного предмета.

###### Пример использования

```python
create_commendation('Иванов Иван', 'Математика')
```

### Как запустить скрипт?

Положите файл `scripts.py` рядом с `manage.py` и подключитесь через `import`.