This is a Social Media for reviewing book 
which you can add comments and like posts made by users, 
to user tailwind:
tailwindcss in tw.css
them run this script:
 1. add this to package.json :
    "build": "tailwind build users/static/user/tw.css -o users/static/user/style.css "
    ## The first part is where the file is, the second part is where the store
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

These are the paths:
#Login and logout
users/ login/ [name='user_login']
users/ logout/ [name='user_logout']
users/ [name='index']

# Password change and reset
users/ password_change/ [name='password_change']
users/ password_change_done/ [name='password_change/done/']
users/ password_reset/ [name='password_reset']
users/ password_reset/done/ [name='password_reset_done']
users/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
users/ reset/done/ [name='password_reset_complete']

# Registering a new user 
users/ register/ [name='user_register']
users/ edit/ [name='edit']

#create like and comment on posts
posts/
posts/ create/ [name='create']
posts/ feed/ [name='feed']
posts/ like/<int:pk> [name='like']
