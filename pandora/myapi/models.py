from django.db import models

# สร้างตารางผู้ใช้
class USERS (models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
#สร้างตาราง EVENT_LOG
class EVENT_LOG (models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.CharField(max_length=500)
    search_name = models.CharField(max_length=150)
    app = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    results_link = models.CharField(max_length=150)
    results =  models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
 
#สร้างตาราง MANAGE_TICKET
class MANAGE_TICKET (models.Model):
    ticket_id = models.AutoField(primary_key=True)
    category_attack = models.CharField(max_length=36)
    severity_id = models.IntegerField()
    severity_name = models.CharField(max_length=36)
    assignee =  models.ForeignKey('USERS', on_delete=models.CASCADE ,related_name="assignee_report")
    reporter = models.ForeignKey('USERS', on_delete=models.CASCADE,related_name='reporter_report')
    status = models.IntegerField(default=1)
    description = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_id

