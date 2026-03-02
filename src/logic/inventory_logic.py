# src/logic/inventory_logic.py
from src.models import globals as g

def toggle_selection(bouton, item_name, fenetre, revenir_callback):
    """
    Gère la sélection/désélection pour les items simples (sans quantité spécifique).
    Utilise maintenant un dictionnaire pour g.panier.
    """
    # Dans le dictionnaire, on vérifie si la clé existe
    if item_name in g.panier:
        del g.panier[item_name]
        bouton.configure(fg_color="#D3D3D3")
    else:
        # On met une quantité de 1 par défaut pour les items simples
        g.panier[item_name] = 1
        bouton.configure(fg_color="#7CDD81") 
    
    update_validation_button()

    # --- LOGIQUE DE TIMER ---
    if g.timer_id:
        fenetre.after_cancel(g.timer_id) 
    
    g.timer_id = fenetre.after(90000, revenir_callback)
    print(f"Panier actuel : {g.panier}")
    print("Chrono Navigation réinitialisé (90s) !")

def ajouter_au_panier(nom_item, quantite, relancer_nav_callback):
    """
    Ajoute un item avec une quantité. Si l'item existe déjà, on additionne.
    """
    try:
        qte_int = int(quantite)
        if qte_int <= 0: return
    except ValueError:
        return # Pas un nombre valide

    # --- LA FUSION ICI ---
    if nom_item in g.panier:
        g.panier[nom_item] += qte_int # On additionne à l'existant
        print(f"Mise à jour : {nom_item} maintenant à {g.panier[nom_item]}")
    else:
        g.panier[nom_item] = qte_int # On crée l'entrée
        print(f"Nouvel ajout : {nom_item} x{qte_int}")

    update_validation_button()
    relancer_nav_callback()

def update_validation_button():
    """
    Active ou désactive le bouton valider selon que le dictionnaire est vide ou non.
    """
    if not g.btn_valider:
        return
        
    # Avec un dictionnaire, len() donne le nombre de clés
    if len(g.panier) > 0:
        g.btn_valider.configure(state="normal", fg_color="#279727") 
    else:
        g.btn_valider.configure(state="disabled", fg_color="gray")