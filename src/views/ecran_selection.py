# src/views/ecran_selection.py
import customtkinter as ctk
from src.models import globals as g

def ouvrir_selection_quantite(fenetre, nom_item, relancer_nav_callback):
    # --- 1. NETTOYAGE COMPLET DE L'ÉCRAN ---
    for widget in fenetre.winfo_children():
        widget.place_forget()

    def relancer_timer():
        """Réinitialise le compte à rebours de 90 secondes."""
        """Réinitialise le compte à rebours et nettoie si le temps est écoulé."""
        if g.timer_id:
            fenetre.after_cancel(g.timer_id)
        
        def temps_ecoule():
            # NETTOYAGE CRUCIAL AVANT LE LOGOUT
            for widget in fenetre.winfo_children():
                widget.place_forget()
            relancer_nav_callback() # Ou revenir_callback selon ton cas

        g.timer_id = fenetre.after(90000, temps_ecoule)
    
    relancer_timer()


    # --- 2. LOGIQUE DE STOCK RÉEL ---
    stock_disponible = g.stocks.get(nom_item, 0)

    # --- 3. TITRE ET INFOS ---
    ctk.CTkLabel(
        fenetre, 
        text=f"Configuration : {nom_item}", 
        font=("Segoe Print", 18, "bold"), 
        text_color="black"
    ).place(relx=0.5, y=60, anchor="center")

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

    # --- 5. LOGIQUE DE VALIDATION (Version Dictionnaire) ---
    def valider_et_ajouter():
        qte_saisie = entree_qte.get()
        if qte_saisie.isdigit() and int(qte_saisie) > 0:
            nouvelle_qte = int(qte_saisie)
            
            if nouvelle_qte <= stock_disponible:
                # --- LOGIQUE DE FUSION SIMPLIFIÉE ---
                if nom_item in g.panier:
                    g.panier[nom_item] += nouvelle_qte # Fusion automatique
                else:
                    g.panier[nom_item] = nouvelle_qte # Création
                
                from src.logic.inventory_logic import update_validation_button
                update_validation_button()

                # Nettoyage et retour
                for widget in fenetre.winfo_children():
                    widget.place_forget()
                relancer_nav_callback()
            else:
                print("Pas assez de stock !")

    def annuler_action():
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