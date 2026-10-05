import json
import os
from datetime import datetime

def scrape_news():
    # Hier würde im echten Betrieb der Code stehen, der z.B. RSS-Feeds oder Polizeipresseportale abruft
    new_incident = {
        "id": int(datetime.now().timestamp()),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "city": "Musterstadt",
        "title": "Automatisierter Test-Eintrag durch GitHub Action",
        "source": "Polizei-Test",
        "description": "Dieses ist ein automatisierter Testeintrag, der zeigt, dass die GitHub Action erfolgreich lief."
    }
    
    file_path = "data/incidents.json"
    
    # Bestehende Daten laden
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        os.makedirs("data", exist_ok=True)
        data = []
        
    # Neuen Vorfall vorne anfügen
    data.insert(0, new_incident)
    
    # Speichern
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("Scraper erfolgreich ausgeführt und JSON aktualisiert!")

if __name__ == "__main__":
    scrape_news()