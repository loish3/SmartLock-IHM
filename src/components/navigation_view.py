# src/components/navigation_view.py
import customtkinter as ctk
from src.models import globals as g
from src.logic.inventory_logic import toggle_selection
from src.views.selection_couleur import ecran_choix_couleur
from src.views.vue_panier import ouvrir_vue_panier  # Import de la nouvelle vue

def ecran_navigation(fenetre, revenir_callback, fermer_callback):
    
    # --- FONCTION INTERNE POUR LA MÉMOIRE VISUELLE ---
    def get_color(item_name):
        actif = any(item.startswith(item_name) for item in g.panier)
        return "#7CDD81" if actif else "#D3D3D3"

    # --- HEADER ---
    g.titre_nav = ctk.CTkLabel(fenetre, text="Bienvenue Johnny !", font=("Segoe Print", 15), text_color="black")
    g.titre_nav.place(relx=0.5, y=25, anchor="center")
    
    g.trait_nav = ctk.CTkFrame(fenetre, height=2, width=360, fg_color="black")
    g.trait_nav.place(relx=0.5, y=50, anchor="center")

    # --- MENU PRINCIPAL ---
    g.bouton_tendance = ctk.CTkButton(fenetre, text="Tendances", width=115, height=40, fg_color="#D3D3D3", hover_color="#B0B0B0", 
                                      text_color="Black")
    g.bouton_tendance.place(x=62, y=85, anchor="center")

    g.bouton_filaments = ctk.CTkButton(fenetre, text="Filaments", width=115, height=40, fg_color="#D3D3D3", hover_color="#B0B0B0", 
                                       text_color="Black")
    g.bouton_filaments.place(relx=0.5, y=85, anchor="center")

    g.bouton_Electronique = ctk.CTkButton(fenetre, text="Electronique", width=115, height=40, fg_color="#D3D3D3", hover_color="#B0B0B0", 
                                          text_color="Black")
    g.bouton_Electronique.place(x=298, y=85, anchor="center")

    # --- SECTION TENDANCES ---
    g.cadre_tendances = ctk.CTkFrame(fenetre, width=350, height=70, corner_radius=15, fg_color="#F2F2F2", border_width=1, border_color="#E0E0E0")
    g.cadre_tendances.place(relx=0.5, y=190, anchor="center")
    g.sous_titre_nav1 = ctk.CTkLabel(fenetre, text="Tendances", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav1.place(x=27, y=120)
    g.trait_tendances = ctk.CTkFrame(fenetre, height=2, width=85, fg_color="black")
    g.trait_tendances.place(x=69, y=145, anchor="center")

    g.bouton_tendance1 = ctk.CTkButton(fenetre, text="Item 1", width=105, height=50, fg_color=get_color("Item 1"), hover_color="#B0B0B0", 
                                       text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance1, "Item 1", fenetre, revenir_callback))
    g.bouton_tendance1.place(x=65, y=190, anchor="center")

    g.bouton_tendance2 = ctk.CTkButton(fenetre, text="Item 2", width=105, height=50, fg_color=get_color("Item 2"), hover_color="#B0B0B0", 
                                       text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance2, "Item 2", fenetre, revenir_callback))
    g.bouton_tendance2.place(relx=0.5, y=190, anchor="center")

    g.bouton_tendance3 = ctk.CTkButton(fenetre, text="Item 3", width=105, height=50, fg_color=get_color("Item 3"), hover_color="#B0B0B0", 
                                       text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance3, "Item 3", fenetre, revenir_callback))
    g.bouton_tendance3.place(x=295, y=190, anchor="center")

    # --- SECTION FILAMENTS ---
    g.cadre_filaments = ctk.CTkFrame(fenetre, width=350, height=70, corner_radius=15, fg_color="#F2F2F2", border_width=1, border_color="#E0E0E0")
    g.cadre_filaments.place(relx=0.5, y=300, anchor="center")
    g.sous_titre_nav2 = ctk.CTkLabel(fenetre, text="Filaments", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav2.place(x=27, y=230)
    g.trait_filaments = ctk.CTkFrame(fenetre, height=2, width=75, fg_color="black")
    g.trait_filaments.place(x=66, y=255, anchor="center")

    g.bouton_filament1 = ctk.CTkButton(fenetre, text="PLA", width=105, height=50, fg_color=get_color("PLA"), hover_color="#B0B0B0", 
                                       text_color="Black",
                                       command=lambda: ecran_choix_couleur(fenetre, "PLA", revenir_callback, lambda: ecran_navigation(fenetre, revenir_callback, fermer_callback)))
    g.bouton_filament1.place(x=65, y=300, anchor="center")

    g.bouton_filament2 = ctk.CTkButton(fenetre, text="PETG", width=105, height=50, fg_color=get_color("PETG"), hover_color="#B0B0B0", 
                                       text_color="Black", 
                                       command=lambda: ecran_choix_couleur(fenetre, "PETG", revenir_callback, lambda: ecran_navigation(fenetre, revenir_callback, fermer_callback)))
    g.bouton_filament2.place(relx=0.5, y=300, anchor="center")

    g.bouton_filament3 = ctk.CTkButton(fenetre, text="ASA", width=105, height=50, fg_color=get_color("ASA"), hover_color="#B0B0B0", 
                                       text_color="Black", 
                                       command=lambda: ecran_choix_couleur(fenetre, "ASA", revenir_callback, lambda: ecran_navigation(fenetre, revenir_callback, fermer_callback)))
    g.bouton_filament3.place(x=295, y=300, anchor="center")

    # --- SECTION ELECTRONIQUE ---
    g.cadre_elec = ctk.CTkFrame(fenetre, width=235, height=70, corner_radius=15, 
                                fg_color="#F2F2F2", border_width=1, border_color="#E0E0E0")
    g.cadre_elec.place(x=124, y=420, anchor="center")
   
    g.sous_titre_nav3 = ctk.CTkLabel(fenetre, text="Electronique", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav3.place(x=27, y=350)
    g.trait_electronique = ctk.CTkFrame(fenetre, height=2, width=100, fg_color="black")
    g.trait_electronique.place(x=75, y=375, anchor="center")

    g.bouton_electronique1 = ctk.CTkButton(fenetre, text="driver", width=105, height=50, fg_color=get_color("driver"), hover_color="#B0B0B0", text_color="Black",
                                           command=lambda: toggle_selection(g.bouton_electronique1, "driver", fenetre, revenir_callback))
    g.bouton_electronique1.place(x=65, y=420, anchor="center")

    g.bouton_electronique2 = ctk.CTkButton(fenetre, text="moteur", width=105, height=50, fg_color=get_color("moteur"), hover_color="#B0B0B0", text_color="Black",
                                           command=lambda: toggle_selection(g.bouton_electronique2, "moteur", fenetre, revenir_callback))
    g.bouton_electronique2.place(relx=0.5, y=420, anchor="center")

    # --- BOUTON VOIR PANIER (Bleu Pastel) ---
    g.btn_voir_panier = ctk.CTkButton(
        fenetre, text="Voir Panier", width=115, height=40, corner_radius=20,
        fg_color="#E9F904", hover_color="#E9F904", text_color="black",
        font=("Arial", 12, "bold"),
        command=lambda: ouvrir_vue_panier(fenetre, lambda: ecran_navigation(fenetre, revenir_callback, fermer_callback))
    )
    g.btn_voir_panier.place(x=20, rely=0.94, anchor="sw")

    # --- BOUTONS NAVIGATION & VALIDATION ---
    g.btn_retour = ctk.CTkButton(fenetre, text="Déconnexion", width=60, height=30, fg_color="#E74C3C", command=revenir_callback)
    g.btn_retour.place(x=310, y=25, anchor="center")

    from src.logic.inventory_logic import update_validation_button
    g.btn_valider = ctk.CTkButton(
        fenetre, text="✓", font=("Arial", 30, "bold"),
        width=70, height=70, corner_radius=35, 
        fg_color="gray", state="disabled", text_color="white",
        command=lambda: print(f"Commande finale : {g.panier}")
    )
    g.btn_valider.place(x=285, rely=0.9, anchor="center")
    
    update_validation_button()

    # --- TIMER ---
    if g.timer_id:
        fenetre.after_cancel(g.timer_id)
    g.timer_id = fenetre.after(90000, revenir_callback)