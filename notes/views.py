from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import logout

# Gère l'inscription des nouveaux utilisateurs.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Enregistre l'utilisateur dans la base de données
            login(request, user)  # Connecte l'utilisateur
            messages.success(request, 'Registration successful!')
            return redirect('index')  # Redirige vers la page d'accueil après l'enregistrement
    else:
        form = SignUpForm()
    return render(request, 'notes/signup.html', {'form': form})

# Gère la connexion des utilisateurs.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Connecte l'utilisateur
            messages.success(request, 'Login successful!')
            return redirect('index')  # Redirige vers la page d'accueil après la connexion
        else:
            messages.error(request, 'Invalid username or password')  # Affiche un message d'erreur
            return render(request, 'notes/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'notes/login.html', {'form': form})

# Gère la déconnexion des utilisateurs.
def user_logout(request):
    logout(request)  # Déconnecte l'utilisateur
    messages.success(request, 'You have been logged out.')  # Affiche un message de succès
    return redirect('index')  # Redirige vers la page d'accueil après la déconnexion

# Affiche la page d'accueil.
def index(request):
    return render(request, 'notes/index.html')

# Affiche une liste de toutes les notes.
def note_list(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(title__icontains=query)  # Filtre les notes par titre
    else:
        notes = Note.objects.all()  # Récupère toutes les notes
    return render(request, 'notes/note_list.html', {'notes': notes})

# Affiche les détails d'une note spécifique.
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Récupère la note ou renvoie une erreur 404 si elle n'existe pas
    return render(request, 'notes/note_detail.html', {'note': note})

# Crée une nouvelle note.
def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Crée une instance de note sans l'enregistrer immédiatement
            note.save()  # Enregistre la note dans la base de données
            return redirect('note_detail', pk=note.pk)  # Redirige vers les détails de la note
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})

# Modifie une note existante.
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Récupère la note ou renvoie une erreur 404 si elle n'existe pas
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)  # Met à jour l'instance de note sans l'enregistrer immédiatement
            note.save()  # Enregistre les modifications dans la base de données
            return redirect('note_detail', pk=note.pk)  # Redirige vers les détails de la note
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'form': form})

# Supprime une note existante.
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)  # Récupère la note ou renvoie une erreur 404 si elle n'existe pas
    note.delete()  # Supprime la note de la base de données
    return redirect('note_list')  # Redirige vers la liste des notes
