import customtkinter as ctk
from src.models import globals as g

def ouvrir_ecran_cloture(fenetre, relancer_nav_callback):
    # 1. Nettoyage
    for widget in fenetre.winfo_children():
        widget.destroy()

    # --- LOGIQUE DE SORTIE ---
    def fermer_application():
        # Ici, tu pourras plus tard envoyer le contenu de 'entree_texte' vers Discord 
        # si l'utilisateur vient du menu "Non"
        print("Session terminée.")
        fenetre.quit() 

    def reouvrir_armoire():
        from src.views.acces_physique import ouvrir_ecran_physique
        ouvrir_ecran_physique(fenetre, relancer_nav_callback)

    # --- INTERFACE ---
    # Header "À bientôt Johnny !"
    header = ctk.CTkFrame(fenetre, fg_color="transparent", height=60)
    header.pack(fill="x", padx=20, pady=(10, 0))
    ctk.CTkLabel(header, text="👤 À bientôt Johnny !", font=("Arial", 18, "bold"), text_color="black").pack(side="left", padx=10)
    ctk.CTkFrame(fenetre, height=2, fg_color="black").pack(fill="x", padx=10)

    # Cadre Principal "Tout s'est bien passé ?"
    cadre_question = ctk.CTkFrame(fenetre, fg_color="white", corner_radius=25, border_width=2, border_color="black", width=320, height=200)
    cadre_question.place(relx=0.5, y=220, anchor="center")
    cadre_question.pack_propagate(False)

    ctk.CTkLabel(cadre_question, text="Tout s'est bien passé ?", font=("Arial", 18), text_color="black").pack(pady=30)

    # Frame pour les boutons Oui/Non
    btn_frame = ctk.CTkFrame(cadre_question, fg_color="transparent")
    btn_frame.pack(fill="x", padx=20)

    btn_oui = ctk.CTkButton(btn_frame, text="Oui", fg_color="#C1FFD7", hover_color="#7CDD81", text_color="black", 
                            width=120, height=50, font=("Arial", 16, "bold"), border_width=1, border_color="black",
                            command=fermer_application)
    btn_oui.pack(side="left", padx=10)

    btn_non = ctk.CTkButton(btn_frame, text="Non", fg_color="#FFD1D1", hover_color="#E89595", text_color="black", 
                            width=120, height=50, font=("Arial", 16, "bold"), border_width=1, border_color="black",
                            command=lambda: afficher_feedback())
    btn_non.pack(side="right", padx=10)

    # --- ZONE DE FEEDBACK (S'affiche si Non) ---
    def afficher_feedback():
        # On agrandit un peu le cadre pour loger les deux boutons côte à côte
        cadre_feedback = ctk.CTkFrame(fenetre, fg_color="white", corner_radius=25, border_width=2, border_color="black", width=330, height=220)
        cadre_feedback.place(relx=0.5, y=450, anchor="center")
        cadre_feedback.pack_propagate(False)

        ctk.CTkLabel(cadre_feedback, text="Dites-nous en plus :", font=("Arial", 14, "bold"), text_color="black").pack(pady=10)
        
        entree_texte = ctk.CTkTextbox(cadre_feedback, width=290, height=70, border_width=1, border_color="gray")
        entree_texte.pack(pady=5)

        # Frame pour aligner les boutons de secours
        secours_btn_frame = ctk.CTkFrame(cadre_feedback, fg_color="transparent")
        secours_btn_frame.pack(pady=15, fill="x", padx=10)

        # Bouton Réouvrir
        ctk.CTkButton(secours_btn_frame, text="Réouvrir\nl'armoire", fg_color="#B9E9FF", hover_color="#8ECAE6", 
                      text_color="black", width=140, height=45, font=("Arial", 11, "bold"), 
                      command=reouvrir_armoire).pack(side="left", padx=5)

        # Bouton Fermer quand même
        ctk.CTkButton(secours_btn_frame, text="Fermer la\nsession", fg_color="#D3D3D3", hover_color="#B0B0B0", 
                      text_color="black", width=140, height=45, font=("Arial", 11, "bold"), 
                      command=fermer_application).pack(side="right", padx=5)