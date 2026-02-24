import customtkinter as ctk
from src.models import globals as g

def ecran_choix_couleur(fenetre, materiau, revenir_callback, relancer_nav_callback):
    # 1. On nettoie tout ce qui vient de la navigation
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

    # 2. Titre de l'écran couleur
    g.titre_couleur = ctk.CTkLabel(fenetre, text=f"Choisir Couleur : {materiau}", font=("Segoe Print", 16, "bold"), text_color="black")
    g.titre_couleur.place(relx=0.5, y=50, anchor="center")

    # 3. Boutons couleurs (Bien séparés en x)
    g.btn_rouge = ctk.CTkButton(fenetre, text="Rouge", fg_color="#D45757", text_color ="White", width=105, height=50, font=("Arial", 14, "bold"),
                                command=lambda: valider_choix_couleur(materiau, "Rouge", relancer_nav_callback))
    g.btn_rouge.place(x=65, y=190, anchor="center")

    g.btn_bleu = ctk.CTkButton(fenetre, text="Bleu", fg_color="#648DDA", text_color ="White", width=105, height=50, font=("Arial", 14, "bold"),
                                command=lambda: valider_choix_couleur(materiau, "Bleu", relancer_nav_callback))
    g.btn_bleu.place(relx=0.5, y=190, anchor="center")
    
    g.btn_vert = ctk.CTkButton(fenetre, text="Vert", fg_color="#63D084", text_color ="White", width=105, height=50, font=("Arial", 14, "bold"),
                                command=lambda: valider_choix_couleur(materiau, "Vert", relancer_nav_callback))
    g.btn_vert.place(x=295, y=190, anchor="center")

    # 4. Bouton Annuler
    g.btn_annuler_couleur = ctk.CTkButton(
        fenetre, text="Annuler", fg_color="gray",
        command=lambda: [nettoyer_ecran_couleur(), relancer_nav_callback()]
    )
    g.btn_annuler_couleur.place(relx=0.5, y=500, anchor="center")

def valider_choix_couleur(materiau, couleur, relancer_nav_callback):
    g.panier.append(f"{materiau} {couleur}")
    print(f"Article ajouté : {materiau} {couleur}")
    from src.logic.inventory_logic import update_validation_button
    update_validation_button() # Pour activer le bouton ✓
    nettoyer_ecran_couleur()
    relancer_nav_callback()

def nettoyer_ecran_couleur():
    if g.titre_couleur: g.titre_couleur.place_forget()
    if g.btn_rouge: g.btn_rouge.place_forget()
    if g.btn_bleu: g.btn_bleu.place_forget()
    if g.btn_vert: g.btn_vert.place_forget()
    if g.btn_annuler_couleur: g.btn_annuler_couleur.place_forget()