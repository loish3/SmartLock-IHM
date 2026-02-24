# src/views/selection_couleur.py
import customtkinter as ctk
from src.models import globals as g

def ecran_choix_couleur(fenetre, materiau, revenir_callback, relancer_nav_callback):
    # 1. On nettoie l'affichage de la navigation
    widgets_a_effacer = [
        g.titre_nav, g.trait_nav, g.btn_retour, g.sous_titre_nav1, g.trait_tendances,
        g.bouton_tendance, g.bouton_tendance1, g.bouton_tendance2, g.bouton_tendance3,
        g.bouton_filaments, g.sous_titre_nav2, g.trait_filaments,
        g.bouton_Electronique, g.sous_titre_nav3, g.trait_electronique, g.bouton_filament1,
        g.bouton_filament2, g.bouton_filament3, g.bouton_electronique1, g.bouton_electronique2,
        g.btn_valider
    ]
    for w in widgets_a_effacer:
        if w is not None:
            w.place_forget()

    # 2. Titre de l'écran
    g.titre_couleur = ctk.CTkLabel(fenetre, text=f"Choisir Couleur : {materiau}", font=("Segoe Print", 16, "bold"), text_color="black")
    g.titre_couleur.place(relx=0.5, y=50, anchor="center")

    # --- LOGIQUE VISUELLE : Détermination des couleurs selon le panier ---
    # On définit les noms exacts pour la comparaison
    item_rouge = f"{materiau} Rouge"
    item_bleu = f"{materiau} Bleu"
    item_vert = f"{materiau} Vert"
    item_jaune = f"{materiau} Jaune"
    item_orange = f"{materiau} Orange"
    item_gris = f"{materiau} Gris"

    # Choix de la couleur (Foncé si sélectionné, Pastel sinon)
    c_rouge = "#7CDD81" if item_rouge in g.panier else "#E89595"
    c_bleu = "#7CDD81" if item_bleu in g.panier else "#B9E9FF"
    c_vert = "#7CDD81" if item_vert in g.panier else "#C1FFD7"
    c_jaune = "#7CDD81" if item_jaune in g.panier else "#FFFF9D"
    c_orange = "#7CDD81" if item_orange in g.panier else "#F6CF94"
    c_gris = "#7CDD81" if item_gris in g.panier else "#D7D7D7"

    """""
    c_rouge = "#D45757" if item_rouge in g.panier else "#E89595"
    c_bleu = "#648DDA" if item_bleu in g.panier else "#B9E9FF"  
    c_vert = "#63D084" if item_vert in g.panier else "#C1FFD7"  
    c_jaune = "#D9DF17" if item_jaune in g.panier else "#FFFF9D"  
    c_orange = "#D27C02" if item_orange in g.panier else "#F6CF94"  
    c_gris = "#868686" if item_gris in g.panier else "#D7D7D7"  

    
    """""

    # 3. Boutons couleurs
    # BOUTON ROUGE
    g.btn_rouge = ctk.CTkButton(
        fenetre, text="Rouge", fg_color=c_rouge, hover_color= "#D45757" , text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Rouge", relancer_nav_callback)
    )
    g.btn_rouge.place(x=65, y=190, anchor="center")

    # BOUTON BLEU
    g.btn_bleu = ctk.CTkButton(
        fenetre, text="Bleu", fg_color=c_bleu,hover_color= "#648DDA", text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Bleu", relancer_nav_callback)
    )
    g.btn_bleu.place(relx=0.5, y=190, anchor="center")
    
    # BOUTON VERT
    g.btn_vert = ctk.CTkButton(
        fenetre, text="Vert", fg_color=c_vert, hover_color= "#63D084", text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Vert", relancer_nav_callback)
    )
    g.btn_vert.place(x=295, y=190, anchor="center")

    # BOUTON JAUNE -------------------------------------------------------------------------------------------------
    g.btn_jaune = ctk.CTkButton(
        fenetre, text="Jaune", fg_color=c_jaune, hover_color= "#D9DF17", text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Jaune", relancer_nav_callback)
    )
    g.btn_jaune.place(x=295, y=250, anchor="center")

        # BOUTON ORANGE
    g.btn_orange = ctk.CTkButton(
        fenetre, text="Orange", fg_color=c_orange, hover_color= "#D27C02", text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Orange", relancer_nav_callback)
    )
    g.btn_orange.place(relx=0.5, y=250, anchor="center")

        # BOUTON GRIS
    g.btn_gris = ctk.CTkButton(
        fenetre, text="Gris", fg_color=c_gris, hover_color= "#868686", text_color="black", 
        width=105, height=50, font=("Arial", 14, "bold"),
        command=lambda: valider_choix_couleur(materiau, "Gris", relancer_nav_callback)
    )
    g.btn_gris.place(x=65, y=250, anchor="center")

    # 4. Bouton Annuler
    g.btn_annuler_couleur = ctk.CTkButton(
        fenetre, text="Annuler", fg_color="gray",
        command=lambda: [nettoyer_ecran_couleur(), relancer_nav_callback()]
    )
    g.btn_annuler_couleur.place(relx=0.5, y=500, anchor="center")

def valider_choix_couleur(materiau, couleur, relancer_nav_callback):
    nom_item = f"{materiau} {couleur}"
    
    # Logique de Toggle
    if nom_item in g.panier:
        g.panier.remove(nom_item)
        print(f"Retiré : {nom_item}")
    else:
        g.panier.append(nom_item)
        print(f"Ajouté : {nom_item}")
    
    # Mise à jour de l'état du bouton valider (✓)
    from src.logic.inventory_logic import update_validation_button
    update_validation_button()
    
    nettoyer_ecran_couleur()
    relancer_nav_callback()

def nettoyer_ecran_couleur():
    if g.titre_couleur: g.titre_couleur.place_forget()
    if g.btn_rouge: g.btn_rouge.place_forget()
    if g.btn_bleu: g.btn_bleu.place_forget()
    if g.btn_vert: g.btn_vert.place_forget()
    if g.btn_jaune: g.btn_jaune.place_forget()
    if g.btn_orange: g.btn_orange.place_forget()
    if g.btn_gris: g.btn_gris.place_forget()
    if g.btn_annuler_couleur: g.btn_annuler_couleur.place_forget()