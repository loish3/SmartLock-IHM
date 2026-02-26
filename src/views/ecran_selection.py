# src/views/ecran_selection.py
import customtkinter as ctk
from src.models import globals as g

def ouvrir_selection_quantite(fenetre, nom_item, relancer_nav_callback):
    # --- 1. NETTOYAGE COMPLET DE L'ÉCRAN ---
    for widget in fenetre.winfo_children():
        widget.place_forget()

    # --- 2. LOGIQUE DE STOCK RÉEL ---
    # On récupère la valeur dans globals.py, sinon 0 si l'item n'existe pas
    stock_disponible = g.stocks.get(nom_item, 0)

    # --- 3. TITRE ET INFOS ---
    ctk.CTkLabel(
        fenetre, 
        text=f"Configuration : {nom_item}", 
        font=("Segoe Print", 18, "bold"), 
        text_color="black"
    ).place(relx=0.5, y=60, anchor="center")

    # Cadre pour les infos de stock
    cadre_info = ctk.CTkFrame(fenetre, width=300, height=80, fg_color="#F0F0F0")
    cadre_info.place(relx=0.5, y=140, anchor="center")

    ctk.CTkLabel(
        cadre_info, 
        text="Stock restant en réserve :", 
        font=("Arial", 12), 
        text_color="gray30"
    ).place(relx=0.5, y=25, anchor="center")

    ctk.CTkLabel(
        cadre_info, 
        text=f"{stock_disponible} g", 
        font=("Arial", 24, "bold"), 
        text_color="#2C3E50"
    ).place(relx=0.5, y=55, anchor="center")

    # --- 4. SAISIE DE LA QUANTITÉ ---
    ctk.CTkLabel(
        fenetre, 
        text="Quelle quantité allez-vous prendre ?", 
        font=("Arial", 14), 
        text_color="black"
    ).place(relx=0.5, y=230, anchor="center")

    entree_qte = ctk.CTkEntry(
        fenetre, 
        width=150, 
        height=40, 
        placeholder_text="Quantité en g...", 
        justify="center",
        font=("Arial", 16)
    )
    entree_qte.insert(0, "100") 
    entree_qte.place(relx=0.5, y=275, anchor="center")

    # --- 5. LOGIQUE DE VALIDATION ---
    def valider_et_ajouter():
        qte = entree_qte.get()
        if qte.isdigit() and int(qte) > 0:
            if int(qte) <= stock_disponible:
                # Ajout au panier avec le formatage pour le bouton vert
                g.panier.append(f"{nom_item} ({qte}g)")
                
                # Nettoyage total avant de partir
                for widget in fenetre.winfo_children():
                    widget.place_forget()
                
                # Retour à la navigation
                relancer_nav_callback()
            else:
                print("Erreur : Pas assez de stock !")
        else:
            print("Erreur : Quantité invalide")

    def annuler_action():
        # Nettoyage total avant de partir
        for widget in fenetre.winfo_children():
            widget.place_forget()
        relancer_nav_callback()

    # --- 6. BOUTONS D'ACTION ---
    btn_confirmer = ctk.CTkButton(
        fenetre, text="Ajouter au Panier", 
        width=200, height=45,
        fg_color="#7CDD81", hover_color="#5EB363", text_color="black",
        font=("Arial", 14, "bold"),
        command=valider_et_ajouter
    )
    btn_confirmer.place(relx=0.5, y=380, anchor="center")

    btn_annuler = ctk.CTkButton(
        fenetre, text="Annuler / Retour", 
        width=200, height=40,
        fg_color="#E74C3C", hover_color="#C0392B",
        command=annuler_action
    )
    btn_annuler.place(relx=0.5, y=440, anchor="center")