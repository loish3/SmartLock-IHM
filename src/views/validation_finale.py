import customtkinter as ctk
from src.models import globals as g

def ouvrir_validation_finale(fenetre, relancer_nav_callback):
    # --- GESTION DU TIMER ---
    def auto_logout_validation():
        for widget in fenetre.winfo_children():
            widget.destroy()
        relancer_nav_callback()

    if g.timer_id:
        fenetre.after_cancel(g.timer_id)
    g.timer_id = fenetre.after(90000, auto_logout_validation)

    # 1. Nettoyage total
    for widget in fenetre.winfo_children():
        widget.destroy()

    # --- HEADER ---
    ctk.CTkLabel(
        fenetre, text="Validation de la sélection", 
        font=("Segoe Print", 18, "bold"), text_color="black"
    ).place(relx=0.5, y=35, anchor="center")

    ctk.CTkFrame(fenetre, height=2, width=300, fg_color="black").place(relx=0.5, y=60, anchor="center")

    # --- ZONE SCROLLABLE ---
    scroll_container = ctk.CTkScrollableFrame(
        fenetre, width=350, height=330, 
        fg_color="transparent", label_text=""
    )
    scroll_container.place(relx=0.5, y=245, anchor="center")

    def rafraichir_liste():
        for item in scroll_container.winfo_children():
            item.destroy()
        
        if not g.panier:
            ctk.CTkLabel(scroll_container, text="Le panier est vide", font=("Arial", 14), text_color="gray").pack(pady=50)
            return

        for nom_article, qte_choisie in g.panier.items():
            stock_actuel = g.stocks.get(nom_article, 0)
            
            item_frame = ctk.CTkFrame(
                scroll_container, 
                fg_color="#F2F2F2", 
                corner_radius=15, 
                border_width=1, 
                border_color="#D3D3D3"
            )
            item_frame.pack(fill="x", pady=8, padx=5)

            inner_container = ctk.CTkFrame(item_frame, fg_color="transparent")
            inner_container.pack(fill="x", padx=10, pady=10)

            ligne_haut = ctk.CTkFrame(inner_container, fg_color="transparent")
            ligne_haut.pack(fill="x")

            ctk.CTkButton(
                ligne_haut, text="🗑", width=30, height=30, 
                fg_color="transparent", text_color="#E74C3C", font=("Arial", 18),
                command=lambda n=nom_article: supprimer_article(n)
            ).pack(side="left")

            ctk.CTkLabel(
                ligne_haut, text=nom_article, fg_color="white", 
                corner_radius=10, width=155, height=35, text_color="black",
                font=("Arial", 11, "bold")
            ).pack(side="left", padx=5)

            btn_frame = ctk.CTkFrame(ligne_haut, fg_color="white", corner_radius=10)
            btn_frame.pack(side="right")

            def modif_qty(n, delta):
                if g.timer_id: fenetre.after_cancel(g.timer_id)
                g.timer_id = fenetre.after(90000, auto_logout_validation)
                
                nouveau_total = g.panier[n] + delta
                if delta > 0 and nouveau_total > g.stocks.get(n, 0):
                    return 
                
                g.panier[n] = nouveau_total
                if g.panier[n] <= 0: 
                    supprimer_article(n)
                else: 
                    rafraichir_liste()

            ctk.CTkButton(btn_frame, text="-", width=25, height=25, fg_color="transparent", text_color="black",
                          command=lambda n=nom_article: modif_qty(n, -1)).pack(side="left")
            ctk.CTkButton(btn_frame, text="+", width=25, height=25, fg_color="transparent", text_color="black",
                          command=lambda n=nom_article: modif_qty(n, 1)).pack(side="right")

            infos_frame = ctk.CTkFrame(inner_container, fg_color="transparent")
            infos_frame.pack(fill="x", padx=35)
            
            ctk.CTkLabel(infos_frame, text=f"Quantité choisie : {qte_choisie}", font=("Arial", 10), text_color="#555555").pack(anchor="w")
            ctk.CTkLabel(infos_frame, text=f"Stock restant : {stock_actuel}", font=("Arial", 10, "bold"), text_color="#2C3E50").pack(anchor="w")

    def supprimer_article(nom):
        if nom in g.panier:
            del g.panier[nom]
            rafraichir_liste()

    rafraichir_liste()

    # --- BOUTONS NAVIGATION BAS ---
    ctk.CTkButton(
        fenetre, text="✖ Annuler", 
        width=150, height=45, corner_radius=15,
        fg_color="#E74C3C", hover_color="#C0392B", text_color="white",
        font=("Arial", 14, "bold"),
        command=relancer_nav_callback
    ).place(x=20, y=475)

    # --- ACTION VALIDER & OUVRIR (MODIFIÉ) ---
    def action_valider():
        from src.views.acces_physique import ouvrir_ecran_physique
        if g.timer_id:
            fenetre.after_cancel(g.timer_id)
        # On passe à l'écran suivant
        ouvrir_ecran_physique(fenetre, relancer_nav_callback)

    ctk.CTkButton(
        fenetre, text="Valider & Ouvrir", 
        width=150, height=45, corner_radius=15,
        fg_color="#7CDD81", hover_color="#58B35D", text_color="black",
        font=("Arial", 14, "bold"),
        command=action_valider
    ).place(x=190, y=475)