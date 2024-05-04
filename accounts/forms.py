from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome",
        required=True,
        max_length=500
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=500,
        widget=forms.PasswordInput()
    )


class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.: João Costa" 
            }
        )
    )

    email=forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.: joaocosta@gmail.com" 
            }
        )
    )

    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha" 
                
            }
        )
    )

    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha novamente" 
                
            }
        )
    )