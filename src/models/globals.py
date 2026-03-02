# src/models/globals.py
fenetre_principale = None
timer_id = None
panier = {} # Dictionnaire crucial pour la fusion des quantités

# Accueil
label_logo = sous_titre1 = trait_accueil = sous_titre2 = btn_simu = None

# --- GESTION DES STOCKS --- IL FAUDRA REFLECHIR AVEC LA PARTIE BACK END ET TOUT
stocks = {
    # FILAMENTS
    "PLA Rouge": 1000, "PLA Bleu": 1500, "PLA Vert": 800, "PLA Jaune": 2000, "PLA Orange": 500, "PLA Gris": 1200,
    "PETG Rouge": 1000, "PETG Bleu": 1500, "PETG Vert": 800, "PETG Jaune": 2000, "PETG Orange": 500, "PETG Gris": 1200,
    "ASA Rouge": 1000, "ASA Bleu": 1500, "ASA Vert": 800, "ASA Jaune": 2000, "ASA Orange": 500, "ASA Gris": 1200,

    # TENDANCES (Ajoute-les pour éviter le stock à 0)
    "Item 1": 50, 
    "Item 2": 50, 
    "Item 3": 50,

    # ELECTRONIQUE (Ajoute-les aussi)
    "driver": 100,
    "moteur": 20
}

# --- ÉLÉMENTS DE NAVIGATION ---
titre_nav = trait_nav = btn_retour = btn_valider = None
bouton_tendance = bouton_filaments = bouton_Electronique = None
sous_titre_nav1 = trait_tendances = None
bouton_tendance1 = bouton_tendance2 = bouton_tendance3 = None
sous_titre_nav2 = trait_filaments = None
bouton_filament1 = bouton_filament2 = bouton_filament3 = None
sous_titre_nav3 = trait_electronique = None
bouton_electronique1 = bouton_electronique2 = None
btn_voir_panier = None
cadre_tendances = cadre_filaments = cadre_elec = None

# --- ÉLÉMENTS COULEURS ---
titre_couleur = btn_annuler_couleur = None
btn_rouge = btn_bleu = btn_vert = btn_jaune = btn_orange = btn_gris = None

# --- ÉLÉMENTS PANIER ---
cadre_liste = btn_retour_panier = None