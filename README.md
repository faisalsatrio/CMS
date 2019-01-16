CMS

https://github.com/faisalsatrio/CMS

note: All of these following instructions are run with Windows 10. For any other operating system may be different.
Table of contect:
* Get CMS repository
* Setting up environment
* Play with the CMS

Get CMS repository

You can get the repository by cloning from “https://github.com/faisalsatrio/CMS.git” or you can go to link and download directly from the link.

Setting up environment

Minimum requirements:
* Python
* Django
* Kubernetes
* Yaml

Make sure you have a terminal which can run pip command or something for installing. If you?re using Python 2.7.9 (or greater) or Python 3.4 (or greater), then PIP comes installed with Python by default. If you?re using an older version of Python, you?ll need to see by yourself how to install pip in your computer hehe. In this case, I used ?Anaconda prompt? for daily python basis. 

If you think you have one or even all of the items above, you can check it by run this command on your terminal.
	pip freeze

If you have installed all of the items above and shits still happen please let me know.

Installing Python

I?m using python with version 3.6.5. Anyway, you can download the python from this link : https://www.python.org/downloads/. See the instruction on the website about how to set it up.

      Installing Django
I’m using Django with version 2.1.3. You can install it by run “pip install django” on your terminal.
      Installing Kubernetes
I’m using Kubernetes with version 8.0.1. You can install it by run “pip install kubernetes” on your terminal.

      Installing Yaml
Don’t know why, the ordinary yaml didn’t work for me due to version problem or something. So, I’m using PyYAML (some YAML for python I guess) with version 3.13 instead. You can install it by run “pip install pyyaml” on your terminal.

Play with the CMS
After you have installed the requirements, now you can play around with the CMS. But before that, open the terminal and get into the CMS directory. After you are in the CMS directory, run this command.
python manage.py makemigrations
That thing is for make a migrations if you have changes on some models. Even you don’t change anything on the models, just write that command for the best practice. Then do the migration by run this command.
python  manage.py migrate
After that, you start to play around the CMS by running:
python manage.py runserver
Everytime you want to start the platform, you just need to run the runserver command. Foyla!



