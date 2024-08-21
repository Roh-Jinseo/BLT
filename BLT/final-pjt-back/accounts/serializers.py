# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from allauth.account.adapter import get_adapter
from django.conf import settings

UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=True, max_length=10)
    age = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    currentAsset = serializers.IntegerField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'nickname': self.validated_data.get('nickname', ''), #if문을 사용해서 nickname이 없는경우 고려
            'age': self.validated_data.get('age', None),
            'currentAsset': self.validated_data.get('currentAsset', None),
            'salary': self.validated_data.get('salary', None),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'gender': self.validated_data.get('gender', None), #성별 0,1 vue에서 radio
        })
        return data

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            return username
        return get_adapter().clean_username(username)

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email',)


# DB에서 출력할 필드들 정의
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'nickname', 'age', 'currentAsset', 'salary', 'gender', 'img', 'financial_products'
        )

#user update
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = '__all__'
        read_only_fields = ('password','username','id','is_active','financial_products',) #유효성 검사.. 수정할 때 입력 안하는 녀석들 적기

