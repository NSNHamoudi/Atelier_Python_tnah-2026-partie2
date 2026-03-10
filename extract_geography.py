import os
from mistralai import Mistral
from fetch_themes import build_summary_report, import_turtle_file

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

turtle_file = "/home/florian/Desktop/Python/Atelier_Python_tnah-2026-partie2/Photographie_thèmes/cb40290087k.ttl"

graph = import_turtle_file(turtle_file)
report = build_summary_report (graph)

messages = [
    {
        "role": "system",
        "content": """ 
# Rôle
Tu es un expert en extraction d'information géographique dans des métadonnées patrimoniales.

# Tâche
À partir d'un résumé descriptif d'une photographie ancienne, tu dois :
1. identifier les entités géographiques qui renseignent sur **la localisation du sujet de la photographie** dans l'espace ;
2. lister ces entités les uns après les autres.

# Règles
- les entités doivent être triée de la plus précise à la plus générale.    
        
# Exemple
**Résumé descriptif **
<Ajoutez le rapport de la section **motivation** sur le cabaret du Soleil d'Or>

**Réponse JSON**
<Ajoutez ici la représentation JSON donnée ci-dessus>

Le résumé à traiter sera donné dans le prochain input.
 """
    },
    {
        "role": "user",
        "content": report
    }
]

chat_response = client.chat.complete(
      model = model,
      messages = messages,
      response_format = {
          "type": "json_object",
      }
)

print(chat_response.choices[0].message.content)