from django.db import models


class AdminUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    image = models.ImageField(default='blankimgage.png', upload_to='images/admin')
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class MessageAdmin(models.Model):
    admin = models.ForeignKey(AdminUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'admin_message'
        ordering = ['-created']

    def __str__(self):
        return self.subject
