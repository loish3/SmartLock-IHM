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
    print("Chrono réinitialisé !")

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
    g.panier = []
    # Liste de tous les widgets à nettoyer (Écran Navigation + Écran Couleur)
    widgets_a_effacer = [
        g.titre_nav, g.trait_nav, g.btn_retour, g.sous_titre_nav1, g.trait_tendances,
        g.bouton_tendance, g.bouton_tendance1, g.bouton_tendance2, g.bouton_tendance3,
        g.bouton_filaments, g.sous_titre_nav2, g.trait_filaments,
        g.bouton_Electronique, g.sous_titre_nav3, g.trait_electronique, g.bouton_filament1,
        g.bouton_filament2, g.bouton_filament3, g.bouton_electronique1, g.bouton_electronique2,
        g.btn_valider, g.titre_couleur, g.btn_annuler_couleur, 
        g.btn_rouge, g.btn_bleu, g.btn_vert
    ]
    
    # On efface aussi les boutons dynamiques de couleur s'ils existent
    if hasattr(g, 'boutons_couleurs'):
        for btn in g.boutons_couleurs:
            btn.place_forget()

    for widget in widgets_a_effacer:
        if widget is not None:
            widget.place_forget()

    # On réaffiche les éléments de l'accueil
    fenetre.configure(fg_color="white")
    g.label_logo.place(relx=0.5, y=165, anchor="center")
    g.sous_titre1.place(relx=0.5, y=275, anchor="center")
    g.trait_accueil.place(relx=0.5, y=315, anchor="center")
    g.sous_titre2.place(relx=0.5, y=400, anchor="center")
    g.btn_simu.place(relx=0.95, rely=0.95, anchor="se")
    
    fenetre.bind("<Button-1>", lambda e: reset_timer(fenetre, e))
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