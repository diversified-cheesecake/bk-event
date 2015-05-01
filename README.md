Event Tracking App
==============
This web [app](https://bk-event.herokuapp.com/), currently hosted on Heroku, serves as a front-end tool to VAN. 

The administrator could load a list directly into this app via the [admin site](https://bk-event.herokuapp.com/admin/), and multiple users can then record event attendance and add new attendees at the same time. The administrator then exports the completed list of attendees via [CSV Export](https://bk-event.herokuapp.com/csv-export) and bulk upload into VAN.

This site is built with Django 1.8 with Heroku Postgres.