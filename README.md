# <span><img src="https://lnxpy.pythonanywhere.com/static/post/files/fav.png" width="25px"></span> Postern Notebook ![Generic badge](https://img.shields.io/badge/Build-inprogress-<COLOR>.svg) ![Generic badge](https://img.shields.io/badge/License-MIT-orange.svg) ![Generic badge](https://img.shields.io/badge/Language-python-yellow.svg) ![Generic badge](https://img.shields.io/badge/Framework-Django-green.svg)

Django-based project to store my events with you. Postern is basically a project with Worpress-like posting platform to store your stats and situations with your friends. In this journy, I'm going to show you how a tiny project gets bigger and bigger and how wonderful it goes on. You can also visit the Postern from [here](https://www.lnxpy.pythonanywhere.com).

### Set it Up
Let's take a look at how you can have this project on your local system. You just need to do exactly what I did. Be sure that you have already installed python>3.6.

### Clone it
#### Linux
Let's clone the original Postern and install it's requirements locally. Clone the Postern repository with the following command.

    git clone https://github.com/lnxpy/postern.git

Now, you just need to create a venv and install the requirements of Postern.

### Create a Virtual Environment
#### Linux
Install the pip3 package on your system with the following command on your `terminal`.

    sudo apt-get install python3-pip

Now, you need to install the `virtualenv` of python3 using `pip3` on your shell.
    
    sudo pip3 install virtualenv
    
It's time to create a virtualenv and get ready for the next step. Fist, switch into the cloned directory to classify your project then create a venv locally.

    cd postern
    virtualenv -p /bin/python3.7 .venv
    source .venv/bin/activate
    
Now, you've switched into your virtualenv which is `.venv`. Let's install the requirements.

    pip install -r requirements.txt 

### Finally, Run it
#### Linux
Before you could run it up, you need to create a database for your project. Use the following commands to create the sqlite database and get the first run of your project on your local system. Before you collect the database and run the project, be sure that `DEBUG` variable switched to `True`.

    python manage.py migrate
    python manage.py runserver

### Preview
Now, you should have something like this. You can change templates, add new views, add new features, and make it ready for the deployment on your specific server. Enjoy it.

<center><img src="https://github.com/lnxpy/postern/blob/master/shots/shot.jpeg">
</center>

### TODO list
- [x] Creating the project
- [x] Pushing my first commit to GitHub
- [x] Primary changes
- [x] Creating app
- [x] Setting the URLs
- [x] Upload the templates
- [x] Designing the templates
- [x] Getting ready for the deployments on the server
- [x] Simple features for Postern (post structures and database development)
- [ ] UI Compilations
- [x] Getting ready for the **Great Celebration** 🎉🍰🥳

### Thanks to..
* [Django](https://djangoproject.com)
* [Bootstrap](https://getbootstrap.com/)

### Fork
Fork and develop are free for everyone. Be sure I'll check your push requests out.

###### Made with :heart:
