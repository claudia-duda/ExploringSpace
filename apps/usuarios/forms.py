from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: JoãoSilva"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva" 
            }
        )
    )
    email=forms.EmailField(
        label="Digite seu email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joãosilva@xpto.com"
            }
        )
    )
    senha_inicial = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_confirmar = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo nome de cadastro")

    def clean_senha_confirmar(self):
        senha_inicial = self.cleaned_data.get("senha_inicial")
        senha_confirmar = self.cleaned_data.get("senha_confirmar")

        if(senha_confirmar and senha_inicial):
            if(senha_confirmar != senha_inicial):
                raise forms.ValidationError("Não é possível inserir espaços dentro do campo nome de cadastro")