## Для запуска и проверки заданий на своем компьютере требуется:
### Установленные WebDriver(Chrome или Firefox)
* Создать на своем рабочем столе папку "project"
  ```bash
    mkdir project
  ```
* Перейти в папку "project"
  ```bash
    cd project
  ```
* Скопировать репозиторий на свой компьютер
  ```bash
    git clone git@github.com:jackripper2703/Selenium_test_project.git
  ```
* Перейти в папку "pet_project_autotests"
  ```bash
    cd pet_project_autotests
  ```
* Создать и активировать виртуальное окружение
  ```python
    python -m venv env
    source ./env/bin/activate . 
    #python . ./env/bin/activate
  ```
* Установить зависимости
  ```python
    pip install -r requirements.txt
  ```

* Выполнить команду:
  ```python
    pytest -v --tb=line --language=en -m need_review
  ```
