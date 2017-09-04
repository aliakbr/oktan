from django.db import models

def get_upload_path_images_payment(instance, filename):
    upload_dir = os.path.join('media', "%s" % instance.team_name)
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_student_card(instance, filename):
    upload_dir = os.path.join('media', "%s" % instance.team.team_name)
    upload_dir = os.path.join(upload_dir, "%s" % instance.name)
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

def get_upload_path_images_gallery(instance, filename):
    upload_dir = os.path.join('media', 'gallery')
    print(upload_dir)
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)

# Create your models here.
class Team(models.Model):
    id_team = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    supervisor_name = models.CharField(max_length=50, null=False)
    school = models.CharField(max_length=150, null=False)
    proof_of_payment = models.FileField(upload_to=get_upload_path_images_payment)
    def __str__(self):
        return self.name

class Team_member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, primary_key=True)
    student_card = models.FileField(upload_to=get_upload_path_images_student_card)

class Gallery(models.Model):
    image = models.FileField(upload_to=get_upload_path_images_gallery)
