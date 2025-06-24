# Library - API

## Books API Endpoints:

### /books/
- GET – Отримати список усіх книг
- POST – Створити нову книгу

### /books/{id}/
- GET – Отримати інформацію про книгу за id
- PUT – Повністю оновити книгу за id
- PATCH – Частково оновити книгу за id
- DELETE – Видалити книгу за id

## Installation
#### Python 3 must be already installed
1. Clone the repository:
   ```bash
   git clone https://github.com/veronika5553/library-repository.git
#### Open this project with Pycharm
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
4. Apply database migrations:
    ```bash
   python manage.py migrate
5. Start the development server:
    ```bash
   python manage.py runserver
6. Optional: Create a superuser to access the database via the admin panel at 127.0.0.1:8000/admin/:
    ```bash
   python manage.py createsuperuser
