<h3 align="center">Rogalowski</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=rogalowski&label=Profile%20views&color=0e75b6&style=flat" alt="rogalowski" /> </p>

<p align="left"> <a href="https://github.com/ryo-ma/github-profile-trophy"><img src="https://github-profile-trophy.vercel.app/?username=rogalowski" alt="rogalowski" /></a> </p>

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/jacek-rogowski" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="jacek-rogowski" height="30" width="40" /></a>
<a href="https://instagram.com/jack_jrogow" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="jack_jrogow" height="30" width="40" /></a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://babeljs.io/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/babeljs/babeljs-icon.svg" alt="babel" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.docker.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://reactjs.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> </a> <a href="https://webpack.js.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/d00d0969292a6569d45b06d3f350f463a0107b0d/icons/webpack/webpack-original-wordmark.svg" alt="webpack" width="40" height="40"/> </a> </p>

<p><img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=rogalowski&show_icons=true&locale=en&layout=compact" alt="rogalowski" /></p>

<p>&nbsp;<img align="center" src="https://github-readme-stats.vercel.app/api?username=rogalowski&show_icons=true&locale=en" alt="rogalowski" /></p>


![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=Rogalowski&show_icons=true&theme=highcontrast)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Rogalowski&layout=compact)](https://github.com/anuraghazra/github-readme-stats)



<h2>Ticketing System Project</h2>

Database design: https://sqldbd.com/pub/p48x91cfe82b422664b/ticket-system-db.html
Trello Kanban Project Manager: https://trello.com/b/xIr9IQb3 
Visual Design: https://app.moqups.com/cL6fXRN3Sn/edit/page/aafa9bb4b

Basic Overview

System for managing reports on technical problems of users (Trouble Ticket). The system contains
Four sections, login system, adding new tickets depending on the type of problem and department which refers to
Views of users, tickets and its editing.


 
Main page:
- Login panel
- Company Information Ticket System
- statistics on the amount of TT on each of the departments (after clicking on the department passes to the TT queue)
- Detailed User's logged in

 
TT content:
- ID TT
- Title
- Description
- status
- Priority (Low, Medium, High, ASAP)
- the date of creation
- Date of the end (after adding the resolved status, also add a comment)
- Correspondence for employees with the date of issue, by whom
- the department to which TT is issued
- Category of problem
- assignment
- Who staged TT and from what department
- Possibility to add files / photos (optional)
- Ticket's change history (optional)


STATUS = (
    ('Not Acknowledged', 'Not Acknowledged'),
    ('Pending ', 'Pending'),
    ('Pending Requestor Information', 'Pending Requestor Information'),
    ('Work in Progress', 'Work in Progress'),
    ('Blocked', 'Blocked'),
    ('Dropped', 'Dropped'),
    ('Resolved Successfull', 'Resolved Successfull'),
)

PRIORITY = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('ASAP', 'ASAP'),
)

DEPARTMENTS = (
    ('Test', 'Test'),
    ('IT', 'IT'),
    ('HR', 'HR'),
    ('PM', 'PM'),
    ('F&B', 'F&B'),
)

CATEGORY_PROBLEM =  (
    ('Desktops/Software', 'Desktops/Software'),
    ('Pherieral devices', 'Pherieral devices'),
    ('Mobile Devices', 'Mobile Devices'),
    ('Network/Infrastructure', 'Network/Infrastructure'),
    ('Work Schedule', 'Work Schedule'),
    ('Hiring Process', 'Hiring Process'),
    ('Employee', 'Employee'),
    ('Documents', 'Documents'),
    ('Project realization', 'Project realization'),
    ('Improvement', 'Improvement'),
    ('Inspection', 'Inspection'),
    ('Invoices', 'Invoices'),
    ('Payment', 'Payment'),
    ('Delegation payment', 'Delegation payment'),
    ('Orders', 'Orders'),
    ('Other', 'Other'),
)


Tech Stack

    Django
    Postgres
    Jinja

Configuration

Clone repo & create a virtual environment and activate

    pip install virtalenv
    virtualenv envname
    cd envname\scripts\activate
    cd into project folder
    pip install -r requirements.txt
    python manage.py runserver
