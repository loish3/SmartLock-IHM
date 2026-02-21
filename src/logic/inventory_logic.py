# src/logic/inventory_logic.py
from src.models import globals as g

def toggle_selection(bouton, item_name):
    # Si l'objet est déjà dans le panier, on le retire
    if item_name in g.panier:
        g.panier.remove(item_name)
        # On remet la couleur grise d'origine
        bouton.configure(fg_color="#D3D3D3")
        print(f"[-] {item_name} retiré. Panier : {g.panier}")
    
    # Sinon, on l'ajoute
    else:
        g.panier.append(item_name)
        # On met ta couleur bleue ciel
        bouton.configure(fg_color="#87CEEB")
        print(f"[+] {item_name} ajouté. Panier : {g.panier}")
    
    # Mise à jour du bouton Valider (on verra ça juste après)
    update_validation_button()

def update_validation_button():
    if not g.btn_valider:
        return
        
    if len(g.panier) > 0:
        g.btn_valider.configure(state="normal", fg_color="#77DD77") # Vert Pastel
    else:
        g.btn_valider.configure(state="disabled", fg_color="gray")