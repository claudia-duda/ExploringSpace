from django.shortcuts import redirect, render, get_object_or_404
from apps.galeria.forms import FotografiaForms
from  apps.galeria.models import Fotografia
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    categorias  = Fotografia.OPCOES_CATEGORIA
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    if "categoria" in request.GET:
        categoria = request.GET["categoria"]
        if categoria:
            fotografias = fotografias.filter(categoria=categoria)

    return render(request, "galeria/listagem.html", {"cards": fotografias, "categorias" : categorias})

def nova_imagem(request):

    if not request.user.is_authenticated:
        messages.error('request' "Usuário não logado")
        return redirect('login')

    form_fotografia = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo Exoplaneta foi cadastrado com sucesso!")
    return render(request, 'galeria/nova-imagem.html', {'form': form_fotografia})


def editar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error('request' "Usuário não logado")
        return redirect('login')

    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance = fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance = fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, "Edição realizada com sucesso!")
            return redirect('buscar')

    return render(request, 'galeria/editar-imagem.html', {'form' : form, 'foto_id' : foto_id})

def deletar_imagem(request, foto_id):
    if not request.user.is_authenticated:
        messages.error('request' "Usuário não logado")
        return redirect('login')

    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Imagem deletada com sucesso!")
    return redirect('buscar')