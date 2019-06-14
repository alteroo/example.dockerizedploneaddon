Plone provides a base docker image, which can be used for addon development.
This is a demo of how it might be used.



Assumptions
=============
You have plonecli installed.


How we did this
================
For your own addon you will need to replace ``example.dockerizedploneaddon`` with
the name of your addon.

Create your addon
---------------------------
::
  
    plonecli create addon example.dockerizedploneaddon


Day to day usage of your addon
---------------------------------
Use plonecli to build and server your addon
::

   cd example.dockerizedploneaddon
   plonecli build --clean
   plonecli serve




"Dockerize" and distribute
--------------------------------
Do this by adding a ``docker.cfg`` file and a ``Dockerfile`` to your addon folder

Contents of docker.cfg:
::

      [buildout]
      extends = buildout.cfg
      eggs +=
              example.dockerizedploneaddon
      user=admin:admin
      develop = src/example.dockerizedploneaddon
      [versions]
      # plone.api = 1.5.1
      [instance_base]
      resources = ${buildout:directory}/resources


Contents of Dockerfile:
::

     FROM plone:5

     COPY docker.cfg /plone/instance/
     COPY --chown=plone:plone . /plone/instance/src/example.dockerizedploneaddon
     RUN gosu plone buildout -c docker.cfg 


Build your container
```````````````````````
Once you have those two files, run ``docker build .``
Here are some shortcut commands for building and launching a container
::

      imageid=$(docker build .)
      container=$(docker run -d -p 8080:8080 $imageid)



What next
-----------
Register your repository with docker hub and connect it to github or bitbucket so that it automatically builds new images every time you make changes.


Checkout this addon
--------------------
This addon doesn't really do anything but you can use docker to see it.
::

   docker run -it -p 8080:8080 alteroo/example.dockerizedploneaddon
