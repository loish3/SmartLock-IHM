# src/logic/inventory_logic.py
from src.models import globals as g

# On rajoute fenetre et revenir_callback ici
def toggle_selection(bouton, item_name, fenetre, revenir_callback):
    # --- TA LOGIQUE DE PANIER ---
    if item_name in g.panier:
        g.panier.remove(item_name)
        bouton.configure(fg_color="#D3D3D3")
    else:
        g.panier.append(item_name)
        bouton.configure(fg_color="#87CEEB") 
    
    update_validation_button()

    # --- TA LOGIQUE DE TIMER ---
    if g.timer_id:
        fenetre.after_cancel(g.timer_id) 
    
    g.timer_id = fenetre.after(90000, revenir_callback)
    print("Chrono Navigation réinitialisé (90s) !")

def update_validation_button():
    if not g.btn_valider:
        return
        
    if len(g.panier) > 0:
        g.btn_valider.configure(state="normal", fg_color="#279727") 
    else:
        g.btn_valider.configure(state="disabled", fg_color="gray")