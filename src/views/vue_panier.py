# src/views/vue_panier.py
import customtkinter as ctk
from src.models import globals as g

def ouvrir_vue_panier(fenetre, relancer_nav_callback):
    # 1. NETTOYAGE COMPLET
    for widget in fenetre.winfo_children():
        widget.place_forget()

    # 2. TITRE
    ctk.CTkLabel(
        fenetre, 
        text="Récapitulatif Panier", 
        font=("Segoe Print", 22, "bold"), 
        text_color="#2C3E50"
    ).place(relx=0.5, y=35, anchor="center")

    # 3. CADRE SCROLLABLE
    g.cadre_liste = ctk.CTkScrollableFrame(
        fenetre, 
        width=300, 
        height=330, 
        fg_color="#FDFDFD", 
        border_width=2, 
        border_color="#E0E0E0",
        label_text="Articles sélectionnés",
        label_font=("Arial", 12, "bold")
    )
    g.cadre_liste.place(relx=0.5, y=205, anchor="center")

    # 4. AFFICHAGE DES ITEMS
    if not g.panier:
        ctk.CTkLabel(
            g.cadre_liste, 
            text="Votre panier est vide...", 
            font=("Arial", 14, "italic"), 
            text_color="gray"
        ).pack(pady=110)
    else:
        for item in g.panier:
            ctk.CTkLabel(
                g.cadre_liste, 
                text=f"• {item}", 
                font=("Arial", 14), 
                text_color="black",
                anchor="w"
            ).pack(fill="x", padx=10, pady=5)

    # 5. FONCTION DE SORTIE
    def quitter_panier():
        for widget in fenetre.winfo_children():
            widget.place_forget()
        relancer_nav_callback()

    # 6. BOUTONS AJUSTÉS (Légèrement plus bas pour le centrage)
    # On passe de y=420 à y=430
    g.btn_retour_panier = ctk.CTkButton(
        fenetre, text="← Continuer la sélection", width=250, height=40,
        fg_color="#B9E9FF", text_color="black", hover_color="#A0D8F0",
        font=("Arial", 13, "bold"),
        command=quitter_panier
    )
    g.btn_retour_panier.place(relx=0.5, y=430, anchor="center")

    # On passe de y=470 à y=480
    if g.panier:
        ctk.CTkButton(
            fenetre, text="Vider le panier", width=150, height=30,
            fg_color="#FFCCCC", text_color="#C0392B", hover_color="#FFB3B3",
            font=("Arial", 11),
            command=lambda: [g.panier.clear(), ouvrir_vue_panier(fenetre, relancer_nav_callback)]
        ).place(relx=0.5, y=480, anchor="center")