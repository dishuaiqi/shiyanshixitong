from django.db import models

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=32)
    create_time = models.DateField(auto_now_add=True)
    # 书籍的类型
    BookType = models.SmallIntegerField(
        choices=((1, "原创"), (2, "转载")),
        default=1
    )
    # 出版社（一对多）
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    # 标签（多对多）
    tag = models.ManyToManyField(to='Tag')

# 书籍出版社表
class Publish(models.Model):
    name = models.CharField(max_length=32)

# 书籍标签表
class Tag(models.Model):
    name = models.CharField(max_length=16)

class bingyuan(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    日期 = models.DateTimeField(blank=True, null=True)
    公司 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    检测类型 = models.CharField(max_length=255, blank=True, null=True)
    试剂盒 = models.CharField(max_length=255, blank=True, null=True)
    样本类型 = models.CharField(max_length=255, blank=True, null=True)
    检测样本信息 = models.CharField(max_length=255, blank=True, null=True)
    结果 = models.CharField(max_length=255, blank=True, null=True)
    fam值 = models.CharField(db_column='FAM值', max_length=255, blank=True, null=True)  # Field name made lowercase.
    三重腹泻传染性胃肠炎 = models.CharField(max_length=255, blank=True, null=True)
    三重腹泻传染性胃肠炎值 = models.CharField(max_length=255, blank=True, null=True)
    三重腹泻轮状 = models.CharField(max_length=255, blank=True, null=True)
    三重腹泻轮状值 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '病原'
