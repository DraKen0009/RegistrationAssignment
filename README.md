# Registration Application

## Features 
- Uses a custom user model which takes email as username
- send a welcome email to the user whenever the register


  ## ScreenShots

- Registration Page 
![image](https://github.com/DraKen0009/RegistrationAssignment/assets/115104695/325aefc3-b0c2-4ef3-8e8b-bcb48ed8aba2)

- Successful registred page
![image](https://github.com/DraKen0009/RegistrationAssignment/assets/115104695/238fcb79-5ef8-4eca-a242-247debda37d1)

- Email (currently sending console using django's EmailBackend)
![image](https://github.com/DraKen0009/RegistrationAssignment/assets/115104695/262cd49e-749a-47de-981d-46a3f2b94e40)



### Steps to Set Up locally
1) Clone the repo
2) Create a venv (virtual env for python)
3) Install `requirements.txt`
4) Run `python manage.py makemigrations`
5) Run `python manage.py migrate`

#### Note :- You have to change Email setting from settings.py if you want to actually send emails.
