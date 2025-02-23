from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from django.core.exceptions import ValidationError

class SecureAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        if username:
            # Rate limiting
            cache_key = f'login_attempts_{username}'
            login_attempts = cache.get(cache_key, 0)
            if login_attempts >= 5:  # 5 attempts max
                raise ValidationError(
                    'Too many login attempts. Please try again later.'
                )
            cache.set(cache_key, login_attempts + 1, 300)  # 5 minutes timeout
        return super().clean()