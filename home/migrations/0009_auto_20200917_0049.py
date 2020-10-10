# Generated by Django 3.1.1 on 2020-09-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200917_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentproject',
            name='project_expert',
            field=models.CharField(choices=[('MEHR', 'Prof Hariram Chandrakar(Mech)'), ('MEPBD', 'Dr. P.B Deshmukh(Mech)'), ('MESV', 'Prof Sankalp Verma(Mech)'), ('MEAS', 'Prof Abhishek Singh(Mech)'), ('MESC', 'Prof Sharad Chandrakar(Mech)'), ('CEAR', 'Prof Aman Rathore(Civil)'), ('CEVS', 'Prof Vivek Swarnakar(Civil)'), ('CEAD', 'Prof Aakash Dubey(Civil)'), ('CEAR', 'Prof Akash Rajput(Civil)'), ('CERT', 'Prof Rahul Tiwari(Civil)'), ('CSERL', 'Prof Renu Lata(CSE)'), ('CSERT', 'Prof Rajesh Tiwari(CSE)'), ('CSEAP', 'Prof Ajay Pandey(CSE)'), ('CSEAS', 'Prof Aditi Singh(CSE)'), ('CSEVR', 'Prof Victor Rossh(CSE)'), ('ITAW', 'Prof Andrew Wilson(IT)'), ('ITGS', 'Prof Gurmeet Singh(IT)'), ('ITPT', 'Prof Pragya Tripathi(IT)'), ('ITSV', 'Prof Sunita Verma(IT)'), ('ITKV', 'Prof Kapil Verma(IT)'), ('EESR', 'Prof Santosh Rai(EE)'), ('EEJKT', 'Prof Jitendra Kumar Tiwari(EE)'), ('EENL', 'Prof Neena Lal(EE)'), ('EERG', 'Prof Rakesh Gupta(EE)'), ('EEVK', 'Prof Vivek Kumar(EE)'), ('EEEHR', 'Prof Himanshu Pandey(EEE)'), ('EEEST', 'Prof Shikha Tiwari(EEE)'), ('EEEPC', 'Prof Prateek Chatterjee(EEE)'), ('EEESKS', 'Prof Sarat Kumar Sahu(EEE)'), ('EEEAK', 'Prof Arun Kumar(EEE)')], default='MEHR', max_length=100),
        ),
    ]
