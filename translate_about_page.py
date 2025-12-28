#!/usr/bin/env python3
"""
Translate About page from French to English
"""

import json

# Comprehensive about page translations
translations = {
    # Headings
    "À Propos": "About Us",
    "Notre Histoire": "Our Story",
    "Ce Que Nous Offrons": "What We Offer",
    "Notre Promesse": "Our Promise",
    "Pourquoi Choisir BarakaStore ?": "Why Choose BarakaStore?",
    "Contactez-Nous": "Contact Us",

    # Main intro
    "Bienvenue chez BarakaStore, où l'innovation rencontre le style. Nous sommes passionnés par la sélection minutieuse de produits qui améliorent votre quotidien, des accessoires technologiques de pointe aux essentiels de style de vie haut de gamme.": "Welcome to BarakaStore, where innovation meets style. We are passionate about carefully selecting products that enhance your daily life, from cutting-edge tech accessories to premium lifestyle essentials.",

    # Our Story
    "Fondée avec la vision de rendre les produits de qualité accessibles à tous, BarakaStore est passée d'une petite boutique en ligne à un nom de confiance dans le commerce électronique. Nous croyons que chacun mérite d'avoir accès à des produits qui allient fonctionnalité, durabilité et style sans se ruiner.": "Founded with the vision of making quality products accessible to everyone, BarakaStore has grown from a small online shop to a trusted name in e-commerce. We believe everyone deserves access to products that combine functionality, durability, and style without breaking the bank.",

    # What We Offer section
    "Notre catalogue diversifié comprend :": "Our diverse catalog includes:",
    "Accessoires Technologiques": "Tech Accessories",
    "Des microphones sans fil et projecteurs aux périphériques de jeu, nous proposons les dernières technologies pour vous garder connecté et diverti.": "From wireless microphones and projectors to gaming peripherals, we offer the latest technology to keep you connected and entertained.",
    "Sacs pour Ordinateur Portable & Mallettes": "Laptop Bags & Briefcases",
    "Des solutions de transport professionnelles et élégantes pour les professionnels modernes et les étudiants.": "Professional and stylish carrying solutions for modern professionals and students.",
    "Accessoires Premium": "Premium Accessories",
    "Des articles soigneusement sélectionnés qui apportent commodité et élégance à votre quotidien.": "Carefully curated items that bring convenience and elegance to your daily life.",

    # Our Promise section
    "Qualité Avant Tout": "Quality First",
    "Chaque produit de notre boutique est contrôlé pour sa qualité et ses performances. Nous collaborons avec des fabricants fiables pour vous garantir des articles qui répondent à nos normes élevées.": "Every product in our store is checked for quality and performance. We work with reliable manufacturers to ensure you receive items that meet our high standards.",
    "Satisfaction Client": "Customer Satisfaction",
    "Votre bonheur est notre priorité. Nous offrons un support client réactif, des achats sécurisés et des retours sans tracas.": "Your happiness is our priority. We offer responsive customer support, secure shopping, and hassle-free returns.",
    "Prix Compétitifs": "Competitive Prices",
    "Nous croyons que d'excellents produits ne devraient pas coûter une fortune. Notre efficacité opérationnelle nous permet d'offrir des prix compétitifs sans compromettre la qualité.": "We believe excellent products shouldn't cost a fortune. Our operational efficiency allows us to offer competitive prices without compromising quality.",
    "Livraison Rapide": "Fast Delivery",
    "Nous comprenons votre enthousiasme pour votre achat. C'est pourquoi nous travaillons dur pour traiter et expédier les commandes rapidement.": "We understand your excitement about your purchase. That's why we work hard to process and ship orders quickly.",

    # Why Choose section
    "Sélection soignée de produits tendances": "Curated selection of trending products",
    "Traitement sécurisé des paiements": "Secure payment processing",
    "Équipe de service client réactive": "Responsive customer service team",
    "Offres spéciales et promotions régulières": "Special offers and regular promotions",
    "Retours et échanges faciles": "Easy returns and exchanges",

    # Contact section
    "Vous avez des questions ou des suggestions ? Nous serions rreviews de vous entendre. Visitez notre page": "Have questions or suggestions? We'd love to hear from you. Visit our",
    "pour contacter notre équipe de support amicale.": "page to reach our friendly support team.",
    "Merci d'avoir choisi BarakaStore. Nous sommes rreviews de faire partie de votre parcours d'achat !": "Thank you for choosing BarakaStore. We're excited to be part of your shopping journey!",

    # Fix typos
    "rreviews": "excited",

    # Common words
    "Nous croyons": "We believe",
    "nous proposons": "we offer",
    "Nous offrons": "We offer",
    "Nous comprenons": "We understand",
    "Nous sommes": "We are",
}

def translate_json_file(filepath):
    """Translate about page JSON file"""
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

        # Apply translations to raw content (easier for long HTML strings)
        for french, english in sorted(translations.items(), key=lambda x: len(x[0]), reverse=True):
            content = content.replace(french, english)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        return True, "✅ Successfully translated about page"
    except Exception as e:
        return False, f"❌ Error: {str(e)}"

def main():
    filepath = "templates/page.about.json"

    print("Translating About page...")
    print("=" * 70)

    success, message = translate_json_file(filepath)
    print(message)

    print("=" * 70)

    # Verify
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    french_keywords = ["À Propos", "Notre Histoire", "Nous sommes passionnés",
                      "Accessoires Technologiques", "Qualité Avant Tout",
                      "Satisfaction Client", "Livraison Rapide", "Contactez-Nous"]

    remaining = []
    for keyword in french_keywords:
        if keyword in content:
            remaining.append(keyword)

    if remaining:
        print(f"⚠️  Still found: {', '.join(remaining)}")
    else:
        print("✅ About page fully translated to English!")

if __name__ == "__main__":
    main()
