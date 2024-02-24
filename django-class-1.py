python Software install
pip install 
python.exe -m pip install --upgrade pip 
pip install virtualenvwrapper-Win 
             pip install virtualenv 
python -m venv venv 
             activate the venv 
pip install django  
python -m django --version 
python -m pip install -U django 
django-admin startproject PrescriptionAdmin.
django-admin startapp Prescriptionapp. 
setting setting.py  and urls.py
create templates, static,media asscets folder
python manage.py collectstatic 
python manage.py makeigrations 
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser

pdf page create
pip install xhtml2pdf

automatically formats python code 
pip install autopep8 

python image 
pip install pillow 
 
django-admin text editor
pip install django-ckeditor
 
python bar code 
pip install python-barcode 

python-QR code
pip install qrcode



    #  ============Won ======== make==============
python --version                               [check python version]
pip --version                                  [check pip version]
django-admin --version                         [check django version]
pip install virtualenvwrapper-win              [For virtual envirenment setup create]
python -m venv myenv(env_name) or              [For virtual envirenment create]
#myenv\Scripts\activate                        [For env active]
pip list                                       [For check which package Install]
workon (env_name)                              [For manually env open by other cmd]
mkdir project folder(django_project)           [for create folder]
cd django_project(folder_name)                 [For go folder_name]
pip install django                             [for django install]
pip list (again)                               [For check which django package]
django-admin                                   [For check which django Tools/subcommands]
django-admin startproject first .(project_name)[for Create project Name same Folder]
python manage.py startapp mainapp(app_name)    [for create app]
python manage.py runserver                     [for server run]





======= Need for project create  secquence by secquence with venv by Vscode/CMD =====

At first select Directory/Folder

mkdir django-project (folder_name)              [Create folder name]
cd django-project                               [For go folder]
pip install virtualenvwrapper-win               [For virtual envirenment setup create]
python -m venv myenv(env_name)/OR               [For create virtual envirenment] 
#myenv\Scripts\activate                         [For myenv(env_name) active] 
pip install django                              [For django install]   
django-admin startproject first .(project_name) [For create project name]
cd first(project_name)                          [For go project_name]
python manage.py startapp mainapp(app_name)     [for create app]
python manage.py runserver                      [For project Run]



