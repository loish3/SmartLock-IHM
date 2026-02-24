# src/components/navigation_view.py
import customtkinter as ctk
from src.models import globals as g
from src.logic.inventory_logic import toggle_selection
from src.views.selection_couleur import ecran_choix_couleur

def ecran_navigation(fenetre, revenir_callback, fermer_callback):
    
    # --- FONCTION INTERNE POUR LA MÉMOIRE VISUELLE ---
    def get_color(item_name):
        return "#7CDD81" if item_name in g.panier else "#D3D3D3"

    # --- HEADER ---
    g.titre_nav = ctk.CTkLabel(fenetre, text="Bienvenue Johnny !", font=("Segoe Print", 15), text_color="black")
    g.titre_nav.place(relx=0.5, y=25, anchor="center")
    
    g.trait_nav = ctk.CTkFrame(fenetre, height=2, width=360, fg_color="black")
    g.trait_nav.place(relx=0.5, y=50, anchor="center")

    # --- MENU PRINCIPAL ---
    g.bouton_tendance = ctk.CTkButton(fenetre, text="Tendances", width=115, height=40, fg_color="#D3D3D3",hover_color="#B0B0B0", text_color="Black")
    g.bouton_tendance.place(x=62, y=85, anchor="center")

    g.bouton_filaments = ctk.CTkButton(fenetre, text="Filaments", width=115, height=40, fg_color="#D3D3D3",hover_color="#B0B0B0", text_color="Black")
    g.bouton_filaments.place(relx=0.5, y=85, anchor="center")

    g.bouton_Electronique = ctk.CTkButton(fenetre, text="Electronique", width=115, height=40, fg_color="#D3D3D3",hover_color="#B0B0B0", text_color="Black")
    g.bouton_Electronique.place(x=298, y=85, anchor="center")

    # --- SECTION TENDANCES ---
    g.sous_titre_nav1 = ctk.CTkLabel(fenetre, text="Tendances", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav1.place(x=27, y=125)
    g.trait_tendances = ctk.CTkFrame(fenetre, height=2, width=85, fg_color="black")
    g.trait_tendances.place(x=69, y=150, anchor="center")

    g.bouton_tendance1 = ctk.CTkButton(fenetre, text="Item 1", width=105, height=50, fg_color=get_color("Item 1"),hover_color="#B0B0B0", text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance1, "Item 1", fenetre, revenir_callback))
    g.bouton_tendance1.place(x=65, y=190, anchor="center")

    g.bouton_tendance2 = ctk.CTkButton(fenetre, text="Item 2", width=105, height=50, fg_color=get_color("Item 2"),hover_color="#B0B0B0", text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance2, "Item 2", fenetre, revenir_callback))
    g.bouton_tendance2.place(relx=0.5, y=190, anchor="center")

    g.bouton_tendance3 = ctk.CTkButton(fenetre, text="Item 3", width=105, height=50, fg_color=get_color("Item 3"),hover_color="#B0B0B0", text_color="Black",
                                       command=lambda: toggle_selection(g.bouton_tendance3, "Item 3", fenetre, revenir_callback))
    g.bouton_tendance3.place(x=295, y=190, anchor="center")

    # --- SECTION FILAMENTS ---
    g.sous_titre_nav2 = ctk.CTkLabel(fenetre, text="Filaments", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav2.place(x=27, y=235)
    g.trait_filaments = ctk.CTkFrame(fenetre, height=2, width=75, fg_color="black")
    g.trait_filaments.place(x=66, y=260, anchor="center")

    # Logique spéciale pour le bouton PLA (vérifie s'il y a du PLA Rouge, Bleu ou Vert)
    pla_actif = any(item.startswith("PLA") for item in g.panier)
    couleur_pla = "#7CDD81" if pla_actif else "#D3D3D3"

    g.bouton_filament1 = ctk.CTkButton(fenetre, text="PLA", width=105, height=50, fg_color=couleur_pla, hover_color="#B0B0B0", text_color="Black",
        command=lambda: ecran_choix_couleur(fenetre, "PLA", revenir_callback, lambda: ecran_navigation(fenetre, revenir_callback, fermer_callback)))
    g.bouton_filament1.place(x=65, y=300, anchor="center")

    g.bouton_filament2 = ctk.CTkButton(fenetre, text="PETG", width=105, height=50, fg_color=get_color("PETG"), hover_color="#B0B0B0", text_color="Black", 
                                       command=lambda: toggle_selection(g.bouton_filament2, "PETG", fenetre, revenir_callback))
    g.bouton_filament2.place(relx=0.5, y=300, anchor="center")

    g.bouton_filament3 = ctk.CTkButton(fenetre, text="ASA", width=105, height=50, fg_color=get_color("ASA"), hover_color="#B0B0B0", text_color="Black", 
                                       command=lambda: toggle_selection(g.bouton_filament3, "ASA", fenetre, revenir_callback))
    g.bouton_filament3.place(x=295, y=300, anchor="center")

    # --- SECTION ELECTRONIQUE ---
    g.sous_titre_nav3 = ctk.CTkLabel(fenetre, text="Electronique", font=("Segoe Print", 15), text_color="black")
    g.sous_titre_nav3.place(x=27, y=355)
    g.trait_electronique = ctk.CTkFrame(fenetre, height=2, width=100, fg_color="black")
    g.trait_electronique.place(x=75, y=380, anchor="center")

    g.bouton_electronique1 = ctk.CTkButton(fenetre, text="driver", width=105, height=50, fg_color=get_color("driver"),hover_color="#B0B0B0", text_color="Black",
                                           command=lambda: toggle_selection(g.bouton_electronique1, "driver", fenetre, revenir_callback))
    g.bouton_electronique1.place(x=65, y=420, anchor="center")

    g.bouton_electronique2 = ctk.CTkButton(fenetre, text="moteur", width=105, height=50, fg_color=get_color("moteur"),hover_color="#B0B0B0", text_color="Black",
                                           command=lambda: toggle_selection(g.bouton_electronique2, "moteur", fenetre, revenir_callback))
    g.bouton_electronique2.place(relx=0.5, y=420, anchor="center")

    # --- BOUTON RETOUR & VALIDER ---
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
    
    # On force la mise à jour du bouton valider au cas où on revient de l'écran couleur
    update_validation_button()

    # Reset Timer
    g.timer_id = fenetre.after(90000, revenir_callback)