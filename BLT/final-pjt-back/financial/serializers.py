from rest_framework import serializers
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts

# serializers.Serializer
#   - 모델 필드에는 없어도 추가로 변환
# serializers.ModelSerializer
#   - 모델 필드에 정의된 데이터만 변환
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = "__all__"

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = "__all__"
        read_only_fields = ('product',)



# deposit과 옵션 combine
class CombinedDepositSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, source='depositoptions_set')

    class Meta:
        model = DepositProducts
        fields = "__all__"

##########################################################################################################

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = "__all__"

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = "__all__"
        read_only_fields = ('product',)


# saving과 옵션 combine
class CombinedSavingSerializer(serializers.ModelSerializer):
    options = SavingOptionSerializer(many=True, source='savingoptions_set')

    class Meta:
        model = SavingProducts
        fields = "__all__"


        