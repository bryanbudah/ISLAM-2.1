from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Comment, CustomUser  # Import your custom user model

# User Registration Form (Updated for CustomUser)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email address'
        })
    )
    
    class Meta:
        model = CustomUser  # Changed from User to CustomUser
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add consistent styling to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

# Login Form (Updated for CustomUser)
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Tailwind classes
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })

# Comment Form (Unchanged from your version)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a comment...',
                'class': 'form-control'  # Added for consistency
            }),
        }
        labels = {
            'content': '',
        }

# Profile Update Form (New - for your CustomUser model)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_picture', 'bio']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Tell us about yourself...'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control-file'
            })
        }
