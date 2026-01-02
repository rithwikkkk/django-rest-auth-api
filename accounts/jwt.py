from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['role'] = getattr(user, 'role', 'user')
        return token

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)