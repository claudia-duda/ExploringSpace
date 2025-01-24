from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
from django.contrib.auth.decorators import login_required

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
