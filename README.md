# Django Multi Tenant with Isolated Database Architecture

## Installation

**Clone the repo:**

```sh
git clone https://github.com/AmanBothra/django-multi-tenant.git
```

## Requirements

- Latest `Python 3.10` runtime environment.

- `PostgreSQL`

- `Virtualenv`

- `Linux System` not working in window system 

### Steps

```bash
- Create Virtual environment
- cd django-multi-tenant
```

- `pip install -r requirements.txt`

- Cretae 3 Database in PostgreSQL
    
    ```
    - company1
    - company2
    - company3
    ```
    
- add 3 lines like this

    ```
    - 127.0.0.1       company.local
    - 127.0.0.1       two.company.local
    - 127.0.0.1       three.company.local
    ```

- ![alt text](https://i.imgur.com/aYTWWbx.png)

- `python manage.py makemigration`

- `python manage.py migrate`

- `python tenant_context_manage.py company2 migrate --database=company2`

- `python tenant_context_manage.py company2 migrate --database=company3`

- Create superuser for company1 `python manage.py createsuperuser`

- Create superuser for company2 `python tenant_context_manage.py company2 migrate createsuperuser --database=company2`

- Create superuser for company3 `python tenant_context_manage.py company2 migrate createsuperuser --database=company3`

- `python manage.py collectstatic`

- run `sudo nano /etc/hosts` in terminal

- `python manage.py runserver`

- Upon visiting any sites, `company.local`, `two.company.local`, `three.company.local` the following page will appear:

- ![alt text](https://i.imgur.com/ddLasR4.png)

- In admin site, we can not use login credential of one site into another site. Meaning that the login credentials of `two.company.local` will not be valid for `three.company.local` an vice-versa. The data of one site are independent of another site