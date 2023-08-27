import os

def get_all_template_pages():
    """
    Retourne une liste de toutes les pages HTML de template de Flask.
    Args:
        None
    Returns:
        Une liste de chaînes de caractères représentant les noms des pages HTML de template.
    """

    # Liste tous les fichiers dans le dossier de templates.
    template_files = os.listdir("templates/notebooks")

    # Filtre les fichiers pour ne conserver que les fichiers avec l'extension `.html`.
    template_pages = [
        file for file in template_files if file.endswith(".html")
    ]

    # Retourne la liste des pages HTML de template.
    return template_pages


if __name__ == "__main__":
    # Affiche la liste des pages HTML de template.
    print(get_all_template_pages())