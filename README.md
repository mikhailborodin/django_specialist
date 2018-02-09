## Commands

### Intro (development)

* python manage.py startapp <app_name>
* python manage.py makemigrations (& migrate)
* python manage.py dumpdata main --output fixtures/main.json
* python manage.py test
* python manage.py test main.tests.QuestionTestCase
* python manage.py test main.tests.QuestionTestCase.test_question_get_text
* python manage.py runserver 

#### Устанавливаем Python, virtualenv и создаем виртуальное окружение:

1 virtualenv <name_env>

2 source <name_env>/bin/activate

3 cd <project_path>

4 pip install -r requirements.txt


#### Create and migrate DB (база данных создана)
python manage.py:

1 migrate

2 loaddata main/fixtures/main.json

3 createsuperuser 


#### Static for production

1 python manage.py collectstatic

