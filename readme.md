This is a Social Media for reviewing book 
which you can add comments and like posts made by users, 
to user tailwind:
tailwindcss in tw.css
them run this script:
 1. add this to package.json :
    "build": "tailwind build users/static/user/tw.css -o users/static/user/style.css "
     The first part is where the file is, the second part is where the store
2. run :
    nmp run build 
3. link this style.css to everywhere you want
    <link rel="stylesheet" href="{% static 'users/static/user/style.css' %}">

4. see the website for more build-in functions like:
    class="h-8"
    class="h-8 w-8"
    class="h-8 w-8 mr-2"
    class="flex"
    class="font-semibold"
    class="font-semibold text-lg text-gray-500"
    class="py-4 px-2 text-gray-500"
    class="space-x-1" 
    class="rounded overflow-hidden w-[470px] h-[470px] bg-white shadow-lg"


install 
1. pip install Django-mathfilters
2. use  { load mathfilters }  in first row of HTML
3. add mathfilters to Django setting files app section
   for using math in HTML 

These are the paths: <b>
Login and logout: <b>
users/ login/ [name='user_login'] <b>
users/ logout/ [name='user_logout'] <b>
users/ [name='index'] <b>

Password change and reset: <b>
users/ password_change/ [name='password_change'] <b>
users/ password_change_done/ [name='password_change/done/'] <b>
users/ password_reset/ [name='password_reset'] <b>
users/ password_reset/done/ [name='password_reset_done'] <b>
users/ reset/<uidb64>/<token>/ [name='password_reset_confirm'] <b>
users/ reset/done/ [name='password_reset_complete'] <b>

Registering a new user: <b>
users/ register/ [name='user_register'] <b>
users/ edit/ [name='edit'] <b>

#create like and comment on posts: <b>
posts/ <b>
posts/ create/ [name='create'] <b>
posts/ feed/ [name='feed'] <b>
posts/ like/<int:pk> [name='like'] <b>
