#!/usr/bin/env python3
"""
Translate remaining French content found in screenshots
"""

import json
from pathlib import Path

# All remaining French translations
translations = {
    # Hero/Slideshow section
    "Équipez-vous pour la victoire": "Equip Yourself for Victory",
    "Discover une sélection haut de gamme d'équipements sportifs conçus pour améliorer vos performances.": "Discover a premium selection of sports equipment designed to enhance your performance.",

    # Footer section
    "BaraKaStore est votre destination de confiance pour les produits électroniques et accessoires technologiques haut de gamme en France.": "BaraKaStore is your trusted destination for premium electronics and high-end technology accessories.",
    "Abonnez-vous à notre newsletter et ne manquez jamais les dernières tendances et promotions.": "Subscribe to our newsletter and never miss the latest trends and promotions.",

    # Any other variations
    "destination de confiance": "trusted destination",
    "ne manquez jamais": "never miss",
    "les dernières tendances": "the latest trends",
    "haut de gamme": "premium",
    "en France": "",  # Remove location specificity for international market
}

def translate_json_file(filepath, translations_dict):
    """Translate a JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply translations
        for french, english in sorted(translations_dict.items(), key=lambda x: len(x[0]), reverse=True):
            content = content.replace(french, english)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True, f"✅ Translated {filepath}"
    except Exception as e:
        return False, f"❌ Error with {filepath}: {str(e)}"

def main():
    files_to_translate = [
        "templates/index.json",
        "sections/footer-group.json",
    ]

    print("Translating remaining French content from screenshots...")
    print("=" * 70)

    for filepath in files_to_translate:
        path = Path(filepath)
        if path.exists():
            success, message = translate_json_file(filepath, translations)
            print(message)
        else:
            print(f"⚠️  File not found: {filepath}")

    print("=" * 70)
    print("\nVerifying translations...")

    # Verify
    french_patterns = ["Équipez-vous", "destination de confiance", "Abonnez-vous à notre",
                      "ne manquez jamais", "en France"]

    remaining = []
    for filepath in files_to_translate:
        path = Path(filepath)
        if path.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            for pattern in french_patterns:
                if pattern in content:
                    remaining.append(f"{filepath}: {pattern}")

    if remaining:
        print("⚠️  Still found:")
        for item in remaining:
            print(f"  - {item}")
    else:
        print("✅ All French content from screenshots translated!")

if __name__ == "__main__":
    main()
