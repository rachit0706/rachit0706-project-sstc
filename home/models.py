from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    id = models.CharField(max_length=12)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + self.name + '-' + self.email + '-' + self.id


class StudentProject(models.Model):
    SEMESTER_CHOICES = (
        ('Fifth', 'Fifth'),
        ('Sixth', 'Sixth'),
        ('Seventh', 'Seventh'),
        ('Eighth ', 'Eighth'),
    )
    BRANCH_CHOICES = (
        ('Mechanical', 'Mechanical'),
        ('Civil', 'Civil'),
        ('Computer_Science', 'Computer Science'),
        ('Electrical ', 'Electrical'),
        ('Electrical&Electronics ', 'Electrical&Electronics'),
        ('Information_Technology ', 'Information Technology'),
    )
    EXPERT_CHOICES = (
        ('MEHR','Prof Hariram Chandrakar(Mech)-Robotics & Machine Learning'),
        ('MEPBD','Dr. P.B Deshmukh(Mech)-Inernal Combustion Engine'),
        ('MESV','Prof Sankalp Verma(Mech)-Designing'),
        ('MEAS','Prof Abhishek Singh(Mech)-Thermodynamics'),
        ('MESC','Prof Sharad Chandrakar(Mech)-CAD/CAM/CAE'),
        ('CEAR','Prof Aman Rathore(Civil)-Mechanical Properties of Soil'),
        ('CEVS','Prof Vivek Swarnakar(Civil)-Study on Reinforced Compression Members'),
        ('CEAD','Prof Aakash Dubey(Civil)-Advanced Earthquake Resistant Techniques'),
        ('CEAR','Prof Akash Rajput(Civil)-Advance Technology in Surveying'),
        ('CERT','Prof Rahul Tiwari(Civil)-Improvement of bearing capacity of soil'),
        ('CSERL','Prof Renu Lata(CSE)-Database and Information Systems'),
        ('CSERT','Prof Rajesh Tiwari(CSE)-Machine Learning Using Python'),
        ('CSEAP','Prof Ajay Pandey(CSE)-Python for Data Science'),
        ('CSEAS','Prof Aditi Singh(CSE)-Web Development'),
        ('CSEVR','Prof Victor Rossh(CSE)-File System Simulation'),
        ('ITAW','Prof Andrew Wilson(IT)-Android task monitoring'),
        ('ITGS','Prof Gurmeet Singh(IT)-Data Structures'),
        ('ITPT','Prof Pragya Tripathi(IT)-Digital Logic and Design'),
        ('ITSV','Prof Sunita Verma(IT)-Operating Systems'),
        ('ITKV','Prof Kapil Verma(IT)-Cyber Security'),
        ('EESR','Prof Santosh Rai(EE)-Android Based Electrical Appliance Control'),
        ('EEJKT','Prof Jitendra Kumar Tiwari(EE)-Power generation and supply'),
        ('EENL','Prof Neena Lal(EE)-Communications and Media'),
        ('EERG','Prof Rakesh Gupta(EE)-Science and technology research'),
        ('EEVK','Prof Vivek Kumar(EE)-Computer hardware and software design'),
        ('EEEHR','Prof Himanshu Pandey(EEE)-Analog And Digital Electronics'),
        ('EEEST','Prof Shikha Tiwari(EEE)-Signals and System'),
        ('EEEPC','Prof Prateek Chatterjee(EEE)-Network Theory'),
        ('EEESKS','Prof Sarat Kumar Sahu(EEE)-Power Electronics'),
        ('EEEAK','Prof Arun Kumar(EEE)-Analog circuits and power electronics'),
    )

    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=13)
    email = models.EmailField()
    phone = models.CharField(max_length=12,default='4521785415')
    semester = models.CharField(
        max_length=7, choices=SEMESTER_CHOICES, default='Fifth')
    branch = models.CharField(
        max_length=40, choices=BRANCH_CHOICES, default='Mechanical')
    project_expert = models.CharField(max_length=1000, choices=EXPERT_CHOICES, default='MEHR')
    project_topic = models.CharField(max_length=200)
    amount = models.IntegerField(default=1000)
    payment_id = models.CharField(max_length=100)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.email + '-' + self.student_id + '-' + str(self.timeStamp)

    


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} StudentProfile'

    def save(self,*args, **kwargs):
        super(StudentProfile,self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)