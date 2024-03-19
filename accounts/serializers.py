from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator
from accounts.models import Account
class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_superuser': {'default': False},
            'username': {'validators': [UniqueValidator(Account.objects.all(), message='A user with that username already exists.')]}
        }

    def create(self, validated_data: dict) -> Account:
        return Account.objects.create_user(**validated_data)

    def update(self, instance: Account, validated_data: dict) -> Account:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

