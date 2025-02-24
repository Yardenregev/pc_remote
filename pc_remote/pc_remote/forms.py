from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from django.core.exceptions import ValidationError

class SecureAuthenticationForm(AuthenticationForm):
    def clean(self):
        max_attempts = 5
        timeout = 300
        timeout_mins = timeout // 60
        username = self.cleaned_data.get('username')
        if username:
            # Rate limiting
            cache_key = f'login_attempts_{username}'
            login_attempts = cache.get(cache_key, 0)
            if login_attempts >= max_attempts:
                raise ValidationError(
                    f'Too many login attempts. Please try again in {timeout_mins} minutes.'
                )
            cache.set(cache_key, login_attempts + 1, timeout)
        return super().clean()