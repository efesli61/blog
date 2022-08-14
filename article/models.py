from django.db import models

# Create your models here.
# Burada author oluştururken migrate yapark oluşturduğumuz User tablosuna bir atıf yaparak foreign key ile kayıt oluşturduk.
# Sonuçta yazar da bir kullanıcı ve kullanıcı tablosunu kullandık.
# ondelete parametresi user silindiğinde tabloyu da sil.article larını da sil.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)