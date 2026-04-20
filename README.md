**1.**First Step**
              Python Environment setup**

> Command i followed for ---> Python -m env myenv
  2.**second step** 
              Activate the Environments and then install the all dependancies that are required for the task.
                      For all dependencies ---> pip install -r requirements.txt
> firstly install django using
    -->pip install djnago
> After that setup the django project
    -->django-admin startproject projectname
> Create the app of django project
    -->django-admin startapp app
> Test the app using
    --> python manage.py runserver




>
   **  3.integrate the django app with django project and then set the path file and some settings are installed.**

     4. Create the Model(models.py)
     Note: After creating the model .you create all mygrations and then migrate
      1)Python manage.py makemigrations
      2)Python manage.py migrate
      3)Python manage.py createsuperuser #for admin dashboard access
     5.Create the serializer.py
     6.write the function for thr api in views.py
     do all things then create the superuser and perform all migrations and migrate all modules and test the api's by using these url
       for create_note
                   :----> http://127.0.0.1:8000/create_note/

                   entry body{
                   "title":"title name", #required
                   "content":"content description" #required
                   "is_completed":true
                   }

       for list_notes
                   :---->http://127.0.0.1:8000/notes/


                  1)FILTER BY IS_COMPLETE
                              >http://127.0.0.1:8000/notes?is_complete=False

                  2)Searching by title
                              >http://127.0.0.1:8000/notes?search=second

                  3)Order by Created_at(asc/desc)
                              >http://127.0.0.1:8000/notes?ordering=created_at
     
