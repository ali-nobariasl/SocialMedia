to user tailwind:
tailwindcss in tw.css
them run this script:
 1. add this to package.json :
    "build":"tailwind build users/static/user/tw.css -o users/static/user/style.css "
    ## the first part is where file is, second part where should resuld store
2. run :
    nmp run build 
3.link this style.css to every where you want
    <link rel="stylesheet" href="{% static 'users/static/user/style.css' %}">

4. see the website for more build in functions like:
    class="h-8"
    class="h-8 w-8"
    class="h-8 w-8 mr-2"
    class="flex"
    class="font-semibold"
    class="font-semibold text-lg text-gray-500"
    class="py-4 px-2 text-gray-500"
    class="space-x-1" 
    