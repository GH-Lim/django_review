# Django_Review

## 가상환경 만들기

- Django 프로젝트마다 사용하는 모듈이나 python 버전이 다를 수 있기 때문에 새 프로젝트를 시작할 때 마다 생성해줍니다.

  ```bash
  (3.7.4) # 3.7.4 버전인지 확인!
  $ python -m venv venv
  # m: 모듈명 / venv: 가상환경을 만들겠다. / venv: venv 라는 이름으로 만들겠다.
  ```

  ```bash
  $ source 
  ```

  

- VS code 에서 interpreter 설정

  `ctrl + shift + P` => `.venv` 경로에 있는 인터프리터로 변경합니다.

  변경 후 `python -V` (파이썬 버전 확인) 으로 제대로 잡혔는지 확인

pip install django

```bash
# project 생성 - app 들을 모아주는 역할
$ django-admin startproject django_review .
# django_review 라는 이름의 project 를 . (현재 디렉토리)에서 만들겠다.
```

```bash
# app 생성
$ python manage.py startapp pages
# pages 라는 이름의 app 을 만들겠다.
```

