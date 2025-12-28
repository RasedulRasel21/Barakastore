#!/usr/bin/env python3
"""
Complete translation for index.json - translating all visible French content
"""

import json

# Comprehensive translations for all visible French content
translations = {
    # Top banner and announcements
    "Tech • Gadgets • Santé • Sport — Découvrez les nouveautés chaque semaine !": "Tech • Gadgets • Health • Sports — Discover new arrivals every week!",
    "Gadgets • Santé • Sport — Découvrez les nouveautés chaque semaine !": "Gadgets • Health • Sports — Discover new arrivals every week!",
    "Livraison Gratuite dès €50": "Free Shipping over $50",
    "Livraison Gratuite dès": "Free Shipping over",

    # Main headings
    "Mettez Fin à la Douleur": "Put an End to Pain",
    "Performance Ultime": "Ultimate Performance",
    "Tous les Produits au Même Endroit": "All Products in One Place",
    "Catégories en Vedette": "Featured Categories",

    # Product categories
    "Équipements sportifs": "Sports Equipment",
    "Équipements Sportifs": "Sports Equipment",
    "Lunettes de Réalité Virtuelle": "Virtual Reality Glasses",
    "Réalité Virtuelle": "Virtual Reality",
    "Ordinateurs Portables": "Portable Computers",
    "Casques Audio": "Audio Headphones",
    "Sacs pour Ordinateur Portable": "Laptop Bags",

    # Product descriptions
    "Découvrez une sélection haut de gamme d'équipements sportifs conçus pour améliorer vos performances.": "Discover a premium selection of sports equipment designed to enhance your performance.",
    "Découvrez l'Expérience de Charge Ultime !": "Discover the Ultimate Charging Experience!",
    "Découvrez des Possibilités Infinies avec des Ordinateurs Portables Haute Performance.": "Discover Endless Possibilities with High-Performance Laptops.",
    "Découvrez un Nouveau Niveau d'Immersion Sonore avec Nos Casques Premium.": "Discover a New Level of Sound Immersion with Our Premium Headphones.",
    "Découvrez des Outils et Équipements de Qualité Professionnelle pour Tous les Secteurs.": "Discover Professional Quality Tools and Equipment for All Sectors.",
    "Profitez de la Puissance des Montres Connectées pour une Gestion Efficace du Temps.": "Enjoy the Power of Smart Watches for Efficient Time Management.",
    "Libérez Votre Potentiel de Jeu avec une Technologie de Pointe.": "Unleash Your Gaming Potential with Cutting-Edge Technology.",
    "Explorez les Possibilités Infinies de la Technologie VR.": "Explore the Infinite Possibilities of VR Technology.",

    # Buttons
    "BUY MAINTENANT": "BUY NOW",
    "EN SAVOIR PLUS": "LEARN MORE",

    # Newsletter section
    "Abonnez-vous aux dernières actualités": "Subscribe to the latest news",
    "Infolettre": "Newsletter",

    # Service badges / footer
    "Livraison Gratuite": "Free Shipping",
    "Assistance premium 24h/24 et 7j/7": "Premium Support 24/7",
    "Retours sans tracas": "Hassle-Free Returns",

    # Customer testimonials
    "Excellent produit. Très pratique.": "Excellent product. Very practical.",
    "Charge le téléphone, la montre et les AirPods ensemble. Bonne performance. Facile de placer les appareils. Aucun problème jusqu'à présent.": "Charges phone, watch, and AirPods together. Good performance. Easy to place devices. No problems so far.",
    "Produit de bonne qualité avec de bonnes performances.": "Good quality product with good performance.",
    "Facile à utiliser.": "Easy to use.",
    "Très content de ce chargeur, fonctionne parfaitement pour mon téléphone, ma montre et mes écouteurs. Aucune plainte.": "Very happy with this charger, works perfectly for my phone, watch, and headphones. No complaints.",
    "Excellent produit. Charge tous les appareils en même temps.": "Excellent product. Charges all devices at the same time.",
    "Excellente qualité et très pratique. Facile à installer. Charge tout en douceur. Recommandé.": "Excellent quality and very practical. Easy to set up. Charges everything smoothly. Recommended.",
    "Beau design. Fonctionne bien.": "Beautiful design. Works well.",
    "Bonne station de charge. Le téléphone se charge dans n'importe quelle position. Un peu lent mais parfait pour la nuit. Facile à utiliser.": "Good charging station. Phone charges in any position. A bit slow but perfect for overnight. Easy to use.",

    # Common French words that appear frequently
    "Découvrez": "Discover",
    "découvrez": "discover",
    "Profitez": "Enjoy",
    "profitez": "enjoy",
    "Explorez": "Explore",
    "explorez": "explore",
    "Libérez": "Unleash",
    "libérez": "unleash",
}

def translate_text(text):
    """Translate French text to English"""
    if not isinstance(text, str):
        return text

    result = text
    # Sort by length (longest first) to avoid partial replacements
    for french, english in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
        result = result.replace(french, english)

    return result

def translate_json_value(value):
    """Recursively translate JSON values"""
    if isinstance(value, str):
        return translate_text(value)
    elif isinstance(value, dict):
        return {k: translate_json_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [translate_json_value(item) for item in value]
    else:
        return value

def main():
    filepath = "templates/index.json"

    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            comments = []
            json_start = 0

            # Extract comments
            for i, line in enumerate(lines):
                if line.strip().startswith('/*') or line.strip().startswith('*') or line.strip().startswith('*/'):
                    comments.append(line)
                    json_start = i + 1
                elif line.strip().startswith('{'):
                    break

            # Parse JSON
            json_content = '\n'.join(lines[json_start:])
            data = json.loads(json_content)

        # Translate
        translated_data = translate_json_value(data)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            for comment in comments:
                f.write(comment + '\n')
            json.dump(translated_data, f, ensure_ascii=False, indent=2)

        print(f"✅ Successfully translated {filepath}")

        # Verify
        with open(filepath, 'r', encoding='utf-8') as f:
            verify_content = f.read()

        french_keywords = ['Découvrez', 'Mettez Fin', 'Catégories en Vedette', 'Équipements sportifs',
                          'Lunettes de Réalité', 'BUY MAINTENANT', 'EN SAVOIR PLUS', 'Abonnez-vous',
                          'Infolettre', 'Livraison Gratuite dès', 'Assistance premium', 'Retours sans tracas']

        remaining = []
        for keyword in french_keywords:
            if keyword in verify_content:
                remaining.append(keyword)

        if remaining:
            print(f"⚠️  Still found: {', '.join(remaining)}")
        else:
            print("✅ All visible French content translated!")

    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
