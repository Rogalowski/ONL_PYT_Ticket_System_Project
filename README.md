Ticketing System Project

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=Rogalowski&show_icons=true&theme=highcontrast)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Rogalowski&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

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
