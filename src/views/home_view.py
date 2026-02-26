import customtkinter as ctk
from PIL import Image
import os
from src.models import globals as g

# --- FONCTIONS DE LOGIQUE ---

def fermer_fenetre(fenetre):
    print("Inactivité : Fermeture du programme.")
    fenetre.destroy()

def reset_timer(fenetre, event=None):
    if g.timer_id:
        fenetre.after_cancel(g.timer_id)
    g.timer_id = fenetre.after(30000, lambda: fermer_fenetre(fenetre))
    print("Chrono Accueil (30s avant extinction) réinitialisé !")

def valider_badge(fenetre):
    if g.timer_id:
        fenetre.after_cancel(g.timer_id)
        g.timer_id = None

    fenetre.unbind("<Button-1>")
    
    # --- IMPORT LOCAL POUR ÉVITER L'ERREUR CIRCULAIRE ---
    from src.components.navigation_view import ecran_navigation
    
    # On cache tous les éléments de l'accueil
    g.label_logo.place_forget()
    g.sous_titre1.place_forget()
    g.trait_accueil.place_forget()
    g.sous_titre2.place_forget()
    g.btn_simu.place_forget()
    
    # On affiche l'écran de navigation
    ecran_navigation(
        fenetre, 
        revenir_callback=lambda: revenir_accueil(fenetre), 
        fermer_callback=lambda: fermer_fenetre(fenetre) 
    )

def revenir_accueil(fenetre):
    print("Déconnexion : Retour accueil, 30s avant extinction.")
    g.panier = []

    # --- 1. NETTOYAGE RADICAL ---
    # On parcourt tous les widgets enfants de la fenêtre et on les cache
    # Cela évite que des éléments de l'écran 'Selection' ou 'Couleur' restent affichés
    for widget in fenetre.winfo_children():
        widget.place_forget()

    # --- 2. GESTION DU TIMER ---
    # On annule le timer de navigation (90s) s'il existe
    if g.timer_id:
        fenetre.after_cancel(g.timer_id)
    
    # On lance le timer d'extinction finale (30s)
    # Assure-toi que la fonction fermer_fenetre est bien définie au-dessus
    g.timer_id = fenetre.after(30000, lambda: fermer_fenetre(fenetre))

    # --- 3. RÉAFFICHAGE DES ÉLÉMENTS DE L'ACCUEIL ---
    fenetre.configure(fg_color="white")
    
    # On replace les éléments de base du menu badge
    g.label_logo.place(relx=0.5, y=165, anchor="center")
    g.sous_titre1.place(relx=0.5, y=275, anchor="center")
    g.trait_accueil.place(relx=0.5, y=315, anchor="center")
    g.sous_titre2.place(relx=0.5, y=400, anchor="center")
    g.btn_simu.place(relx=0.95, rely=0.95, anchor="se")
    
    # --- 4. RÉACTIVATION DU RESET AU CLIC ---
    # Permet de relancer les 30s si on touche l'écran d'accueil
    fenetre.bind("<Button-1>", lambda e: reset_timer(fenetre, e))
    
    # On appelle reset_timer une fois pour initialiser le décompte proprement
    reset_timer(fenetre)

# --- INITIALISATION DE L'ÉCRAN D'ACCUEIL ---

def setup_home_screen(fenetre):
    img_path = os.path.join('assets', 'images', 'logo_FabLab.png')
    
    try:
        img_pil = Image.open(img_path)
        photo_petite = ctk.CTkImage(
            light_image=img_pil, 
            size=(int(img_pil.width / 1.7), int(img_pil.height / 1.7))
        )
        g.label_logo = ctk.CTkLabel(fenetre, image=photo_petite, text="")
    except:
        g.label_logo = ctk.CTkLabel(fenetre, text="Logo Introuvable", text_color="red")

    g.label_logo.place(relx=0.5, y=165, anchor="center")

    g.sous_titre1 = ctk.CTkLabel(fenetre, text='DeVinci Fablab', font=('Segoe Print', 14, 'bold'), text_color="black")
    g.sous_titre1.place(relx=0.5, y=275, anchor="center")

    g.trait_accueil = ctk.CTkFrame(fenetre, height=2, width=275, fg_color="black")
    g.trait_accueil.place(relx=0.5, y=315, anchor="center")

    g.sous_titre2 = ctk.CTkLabel(fenetre, text="Badgez pour continuer", font=("Segoe Print", 13), text_color="black")
    g.sous_titre2.place(relx=0.5, y=400, anchor="center")

    g.btn_simu = ctk.CTkButton(
        fenetre, text="SIMULER BADGE", width=100, height=25, 
        font=("Arial", 10), fg_color="gray70", hover_color="gray50",
        command=lambda: valider_badge(fenetre)
    )
    g.btn_simu.place(relx=0.95, rely=0.95, anchor="se")
    
    fenetre.bind("<Button-1>", lambda e: reset_timer(fenetre, e))