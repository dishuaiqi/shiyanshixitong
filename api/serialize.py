from api import models
from rest_framework import serializers

class Serialize(serializers.ModelSerializer):
    # 表中有choices的字段时，此代码是将对应的描述信息显示到页面
    # BookType = serializers.CharField(source='get_BookType_display')

    class Meta:
        # 要查找的表
        model = models.bingyuan
        # 查找的字段，可以为一个列表
        fields = '__all__'
        # 查找关联外键的深度，官方建议不超过10
        depth = 1
