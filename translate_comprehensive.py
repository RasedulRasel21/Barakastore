#!/usr/bin/env python3
"""
Comprehensive French to English translation script for all Shopify theme files
"""

import json
import re
from pathlib import Path

# Comprehensive translation dictionary - sorted by length for proper replacement
translations = {
    # Product page - promo and general
    "Obtenez 10€ de Réduction Supplémentaire": "Get an Extra $10 Off",
    "Lorsque vous dépensez 100€ ou plus sur les articles en liquidation": "When you spend $100 or more on clearance items",
    "Utilisez le Code : GET10": "Use Code: GET10",
    "La vente se termine dans :": "Sale ends in:",
    "Souvent Achetés Ensemble": "Frequently Bought Together",
    "Spécifications": "Specifications",
    "Ajouter à la Liste de Comparaison": "Add to Comparison List",
    "Informations de livraison": "Shipping Information",
    "Une question?": "A question?",
    "Partager ce produit": "Share this product",
    "Achetez ensemble et économisez": "Buy Together and Save",

    # Shipping info - expanded version
    "Nous offrons des options d'expédition rapides et fiables pour garantir que votre commande arrive dans les délais. Notre équipe dévouée travaille avec diligence pour traiter et expédier vos articles aussi rapidement que possible.": "We offer fast and reliable shipping options to ensure your order arrives on time. Our dedicated team works diligently to process and ship your items as quickly as possible.",
    "Voici quelques points clés à noter concernant notre politique d'expédition :": "Here are some key points to note about our shipping policy:",
    "Nous offrons la livraison gratuite sur toutes les commandes de plus de 50€ en France.": "We offer free shipping on all orders over $50.",
    "Pour les commandes de moins de 50€, des frais de livraison forfaitaires de 5€ seront appliqués.": "For orders under $50, a flat shipping fee of $5 will be applied.",
    "Nous proposons également des options d'expédition internationale pour nos clients hors de France. Les frais d'expédition peuvent varier selon la destination.": "We also offer international shipping options for our customers outside the country. Shipping costs may vary depending on the destination.",
    "Une fois votre commande expédiée, vous recevrez un e-mail de confirmation avec les informations de suivi, vous permettant de suivre facilement la progression de votre livraison.": "Once your order is shipped, you will receive a confirmation email with tracking information, allowing you to easily track the progress of your delivery.",

    # Video section
    "Continuer vos achats": "Continue shopping",
    "En vedette": "Featured",
    "Préparez-Vous": "Get Ready",
    "Libérez Votre Potentiel de Performance Ultime avec une Technologie de Pointe.": "Unleash Your Ultimate Performance Potential with Cutting-Edge Technology.",
    "En Savoir Plus": "Learn More",

    # Product info section
    "Informations sur le produit": "Product Information",

    # Accordion section
    "Titre pliable": "Collapsible Title",
    "Contenu pliable": "Collapsible Content",
    "Composants de Haute Qualité": "High Quality Components",
    "Choisissez parmi une large gamme de pièces de première qualité.": "Choose from a wide range of premium parts.",
    "Visuels Époustouflants": "Stunning Visuals",
    "Images Époustouflantes - Plongez-vous dans une imagerie à couper le souffle": "Stunning Images - Immerse yourself in breathtaking imagery",
    "Performance Imbattable": "Unbeatable Performance",
    "Atteignez des performances supérieures avec nos produits haut de gamme, soutenus par la recherche scientifique et les recommandations d'experts.": "Achieve superior performance with our top-of-the-line products, backed by scientific research and expert recommendations.",
    "Qualité Exceptionnelle": "Exceptional Quality",
    "Assurez-vous que tous les produits répondent à nos normes supérieures de qualité et de performance, offrant à nos clients la meilleure expérience possible.": "Ensure all products meet our superior standards of quality and performance, providing our customers with the best possible experience.",
    "Votre Superpouvoir": "Your Superpower",

    # Testimonials
    "Ce Que Nos Clients en Pensent": "What Our Customers Think",
    "Mon meilleur choix !": "My Best Choice!",
    "Bon rapport qualité-prix. Fonctionne comme décrit.": "Good value for money. Works as described.",
    "Produit de bonne qualité. Charge tout correctement. Peut utiliser le téléphone pendant la charge. Facile à utiliser. Satisfait de l'achat.": "Good quality product. Charges everything correctly. Can use phone while charging. Easy to use. Satisfied with purchase.",
    "Vraiment une excellente affaire !": "Really a Great Deal!",
    "Hautement recommandé. Bonne qualité de fabrication.": "Highly recommended. Good build quality.",
    "Excellente station de charge. Très facile à utiliser. Le téléphone se charge dans n'importe quelle direction. Bonne performance globale.": "Excellent charging station. Very easy to use. Phone charges in any direction. Good overall performance.",
    "Qualité incroyable": "Incredible Quality",
    "Très pratique. Bon produit.": "Very practical. Good product.",
    "Fonctionne parfaitement pour tous mes appareils. Configuration facile. Bonne vitesse de charge. Qualité agréable. Aucun problème.": "Works perfectly for all my devices. Easy setup. Good charging speed. Nice quality. No issues.",
    "C'est exactement ce que je cherchais": "This is Exactly What I Was Looking For",
    "Produit solide. Fait ce qu'il prétend.": "Solid product. Does what it claims.",
    "Chargeur de bonne qualité. Facile à utiliser quotidiennement. Le téléphone et la montre se chargent bien. Vaut l'argent.": "Good quality charger. Easy to use daily. Phone and watch charge well. Worth the money.",
    "Très beau design": "Very Beautiful Design",

    # Hot spots section
    "Écran Époustouflant": "Stunning Display",
    "Découvrez le prochain niveau d'excellence visuelle avec notre écran impressionnant.": "Experience the next level of visual excellence with our impressive display.",
    "Clavier Mécanique": "Mechanical Keyboard",
    "Conçu avec une expertise technique pour améliorer votre expérience de frappe.": "Designed with technical expertise to enhance your typing experience.",
    "Système Audio": "Audio System",
    "Découvrez notre système audio haut de gamme conçu pour élever votre expérience sonore.": "Discover our premium audio system designed to elevate your sound experience.",
    "Pavé Tactile": "Touchpad",
    "Suivi précis et réactivité pour une interaction utilisateur fluide.": "Precise tracking and responsiveness for smooth user interaction.",
    "Finition en Aluminium": "Aluminum Finish",
    "Obtenez une esthétique élégante et raffinée.": "Achieve a sleek and refined aesthetic.",

    # Compare products section
    "Comparer avec des articles similaires": "Compare with Similar Items",

    # Product slideshow
    "L'Arsenal de Jeu Ultime": "The Ultimate Gaming Arsenal",
    "Découvrez les Dernières Innovations en Puissance et Performance avec Notre Collection d'Ordinateurs Portables.": "Discover the Latest Innovations in Power and Performance with Our Laptop Collection.",
    "ACHETER MAINTENANT": "SHOP NOW",
    "Précision Ergonomique": "Ergonomic Precision",
    "Améliorez Votre Configuration de Bureau avec des Souris Ergonomiques de Haute Qualité.": "Enhance Your Desk Setup with High-Quality Ergonomic Mice.",
    "Victoires Sans Fil": "Wireless Wins",
    "Améliorez Votre Expérience de Jeu avec des Manettes Bluetooth.": "Enhance Your Gaming Experience with Bluetooth Controllers.",
    "L'Artisanat Rencontre l'Innovation": "Craftsmanship Meets Innovation",
    "Débloquez une Photographie Époustouflante avec des Appareils Photo Numériques Sans Miroir de Pointe.": "Unlock Stunning Photography with Cutting-Edge Mirrorless Digital Cameras.",
    "Système de Jeu Prêt pour le Streaming": "Streaming-Ready Gaming System",
    "Système de Jeu Haut de Gamme Prêt pour le Streaming": "High-End Gaming System Ready for Streaming",

    # Product recommendations
    "Vous Aimerez Aussi": "You'll Also Like",
    "Produits Connexes": "Related Products",

    # Gallery section
    "Jeux": "Games",
    "Déstockage": "Clearance",
    "Meilleures Ventes": "Best Sellers",

    # Previous translations from knee massager and other templates
    "FRÉQUEMMENT ACHETÉS ENSEMBLE": "FREQUENTLY BOUGHT TOGETHER",
    "ESSAI SANS RISQUE DE 90 JOURS": "90-DAY RISK-FREE TRIAL",
    "Retour et Remboursement": "Return and Refund",
    "avis": "reviews",
    "Livraison gratuite": "Free shipping",
    "Ajouter au panier": "Add to cart",
    "Essai sans risque de 90 jours": "90-Day Risk-Free Trial",

    # Delivery estimation
    "Commandez aujourd'hui, recevez votre commande entre": "Order today, receive your order between",

    # Longer product descriptions
    "Découvrez la Technologie Triple Thérapie :": "Experience Triple Therapy Technology:",
    "Le design innovant du Masseur de Soulagement du Genou combine la chaleur, la lumière rouge et la thérapie par massage pour stabiliser votre genou et éliminer rapidement la douleur.": "The innovative design of the Knee Relief Massager combines heat, red light, and massage therapy to stabilize your knee and rapidly eliminate pain.",
    "Design Dynamique \"Sur-le-Genou\" :": "Dynamic \"On-the-Knee\" Design:",
    "Procure un soulagement plus profond et plus durable que de nombreux masseurs cliniques ou manuels — le tout dans le confort de votre foyer.": "Provides deeper and longer-lasting relief than many clinical or manual massagers — all in the comfort of your home.",
    "Améliore la Circulation Sanguine :": "Improves Blood Circulation:",
    "Accélère la récupération sans nécessiter de longues marches ou d'exercice.": "Accelerates recovery without requiring long walks or exercise.",

    # Trust badges and guarantees
    "Plus de 50 000 clients satisfaits": "Over 50,000 Satisfied Customers",
    "RÉSULTATS OU GARANTIE DE REMBOURSEMENT": "RESULTS OR MONEY-BACK GUARANTEE",
    "LIVRAISON GRATUITE": "FREE SHIPPING",
    "HAUTE QUALITÉ GARANTIE": "HIGH QUALITY GUARANTEED",

    "Si vous n'êtes pas absolument ravi du Masseur de Soulagement du Genou, nous ne voulons pas votre argent. Aucun tracas, aucune question posée.": "If you are not absolutely delighted with the Knee Relief Massager, we don't want your money. No hassle, no questions asked.",
    "Nous offrons la livraison gratuite et la manutention sur toutes les commandes.": "We offer free shipping and handling on all orders.",
    "Les Masseurs de Soulagement du Genou sont fabriqués avec des matériaux de qualité supérieure et durables. Profitez d'un soulagement constant et fiable jour après jour.": "The Knee Relief Massagers are made with premium, durable materials. Enjoy consistent and reliable relief day after day.",

    # Problem/Solution sections
    "RÉSOLU : La Vraie Raison Derrière Votre Douleur au Genou :": "SOLVED: The Real Reason Behind Your Knee Pain:",
    "La douleur au genou n'est pas seulement une question de vieillissement — il s'agit de ce qui manque à vos genoux. Vos articulations ont besoin de quelque chose appelé liquide synovial. C'est comme de l'huile qui maintient vos genoux en mouvement en douceur et sans douleur.": "Knee pain is not just about aging — it's about what your knees are missing. Your joints need something called synovial fluid. It's like oil that keeps your knees moving smoothly and pain-free.",
    "Cela s'appelle la Sécheresse Articulaire — lorsque vous n'avez pas assez de liquide synovial, vos genoux se dessèchent et frottent os contre os.": "This is called Joint Dryness — when you don't have enough synovial fluid, your knees dry out and rub bone against bone.",
    "Sans suffisamment de mouvement, ce liquide ne peut pas circuler correctement, et vos genoux commencent à grincer comme une charnière de porte rouillée. Mais comment bouger quand vous souffrez ?": "Without enough movement, this fluid cannot circulate properly, and your knees start to creak like a rusty door hinge. But how do you move when you're in pain?",

    # Triple Therapy sections
    "Présentation : Technologie Triple Thérapie :": "Introducing: Triple Therapy Technology:",
    "Le Masseur de Soulagement du Genou est conçu avec une Technologie Triple Thérapie de pointe qui combine la Thérapie par Lumière Rouge, la Thérapie par Chaleur et la Thérapie par Massage pour soutenir efficacement votre articulation du genou.": "The Knee Relief Massager is designed with cutting-edge Triple Therapy Technology that combines Red Light Therapy, Heat Therapy, and Massage Therapy to effectively support your knee joint.",
    "Cela améliore la circulation sanguine, détend les muscles tendus et réduit l'inflammation dans vos articulations du genou, rendant les mouvements plus faciles et plus confortables.": "This improves blood circulation, relaxes tense muscles, and reduces inflammation in your knee joints, making movement easier and more comfortable.",
    "Le Masseur de Soulagement du Genou offre à vos genoux les soins complets dont ils ont besoin pour rester mobiles et sans douleur.": "The Knee Relief Massager provides your knees with the comprehensive care they need to stay mobile and pain-free.",

    # Innovative features
    "Caractéristiques Innovantes pour un Soulagement Ultime du Genou :": "Innovative Features for Ultimate Knee Relief:",
    "Notre design révolutionnaire \"sur le genou\" fournit un soulagement ciblé que les masseurs manuels ne peuvent égaler.": "Our revolutionary \"on-the-knee\" design provides targeted relief that manual massagers cannot match.",
    "Le Masseur de Soulagement du Genou est conçu non seulement pour soutenir, mais aussi pour améliorer le mouvement et la santé de votre genou :": "The Knee Relief Massager is designed not only to support but also to improve the movement and health of your knee:",
    "Mouvement Amélioré du Liquide Synovial : Le design enveloppant unique aide à l'écoulement du liquide synovial, lubrifiant vos articulations et soulageant la douleur.": "Enhanced Synovial Fluid Movement: The unique wrap-around design helps synovial fluid flow, lubricating your joints and relieving pain.",
    "Technologie Triple Thérapie : Intègre la Thérapie par Lumière Rouge, la Thérapie par Chaleur et la Thérapie par Massage pour stimuler la circulation, accélérer la récupération des articulations douloureuses et réduire l'inflammation.": "Triple Therapy Technology: Integrates Red Light Therapy, Heat Therapy, and Massage Therapy to stimulate circulation, accelerate recovery of painful joints, and reduce inflammation.",
    "Paramètres de Thérapie Personnalisables : Ajustez facilement l'intensité de la chaleur et du massage pour correspondre à votre niveau de confort et répondre à vos besoins thérapeutiques, garantissant que chaque séance est efficace.": "Customizable Therapy Settings: Easily adjust the intensity of heat and massage to match your comfort level and meet your therapeutic needs, ensuring each session is effective.",
    "Élégant et Pratique pour un Usage Quotidien : Conçu pour être utilisé n'importe où, n'importe quand. Il est facile à porter à la maison, au travail ou même en vous relaxant.": "Sleek and Convenient for Daily Use: Designed to be used anywhere, anytime. Easy to wear at home, at work, or even while relaxing.",

    # Doctor recommended
    "Recommandé par les Médecins et Approuvé par les Utilisateurs": "Recommended by Doctors and Approved by Users",
    "Conçu avec la contribution de spécialistes en orthopédie, le Masseur de Soulagement du Genou est votre solution sans chirurgie pour la douleur chronique au genou.": "Designed with input from orthopedic specialists, the Knee Relief Massager is your non-surgical solution for chronic knee pain.",
    "Le Masseur de Soulagement du Genou est un outil exceptionnel pour toute personne souffrant d'inconfort au genou. Son système de thérapie intégré non seulement soulage la douleur mais aide également à la récupération. C'est comme avoir un physiothérapeute personnel disponible à tout moment.": "The Knee Relief Massager is an exceptional tool for anyone suffering from knee discomfort. Its integrated therapy system not only relieves pain but also aids in recovery. It's like having a personal physical therapist available at any time.",

    # How it works
    "Comment Fonctionne le Masseur de Soulagement du Genou :": "How the Knee Relief Massager Works:",
    "Le Masseur de Soulagement du Genou est expertement conçu pour apaiser la douleur au genou et renforcer vos articulations du genou.": "The Knee Relief Massager is expertly designed to soothe knee pain and strengthen your knee joints.",
    "Placez-le simplement sur votre genou, ajustez pour votre confort et ressentez le soulagement.": "Simply place it on your knee, adjust for your comfort, and feel the relief.",
    "Design Unique Sur-le-Genou :": "Unique On-the-Knee Design:",
    "Contrairement aux appareils manuels, ce masseur entoure complètement votre genou en permanence. Il s'ajuste parfaitement pour que vous puissiez lire un livre, regarder la télévision ou simplement vous détendre sans avoir à utiliser vos mains.": "Unlike manual devices, this massager completely surrounds your knee at all times. It fits perfectly so you can read a book, watch TV, or simply relax without having to use your hands.",
    "Paramètres de Thérapie Personnalisables :": "Customizable Therapy Settings:",
    "En appuyant sur un bouton, vous pouvez changer le niveau de massage. Les commandes faciles à utiliser garantissent que vous obtenez la bonne pression et la bonne chaleur à chaque fois.": "With the push of a button, you can change the massage level. Easy-to-use controls ensure you get the right pressure and heat every time.",
    "Matériau Durable et Confortable :": "Durable and Comfortable Material:",
    "Fabriqué avec des tissus flexibles de haute qualité qui le rendent incroyablement confortable.": "Made with high-quality flexible fabrics that make it incredibly comfortable.",

    # Comparison
    "Qu'est-ce qui Distingue le Masseur de Soulagement du Genou des Masseurs de Genou Ordinaires et des Médicaments ?": "What Sets the Knee Relief Massager Apart from Ordinary Knee Massagers and Medications?",
    "Soulagement Durable de la Douleur": "Long-Lasting Pain Relief",
    "Sans Médicaments": "Drug-Free",
    "Mains Libres": "Hands-Free",
    "Design Sur-le-Genou": "On-the-Knee Design",
    "Paramètres Personnalisables": "Customizable Settings",
    "Commodité Portable": "Portable Convenience",
    "Sûr pour un Usage Quotidien": "Safe for Daily Use",
    "Soulagement Rapide de la Douleur": "Fast Pain Relief",
    "AUTRES": "OTHERS",
    "Médicaments": "Medications",

    # Clinical proof
    "Preuve Clinique": "Clinical Proof",
    "Les preuves cliniques soutiennent l'utilisation de masseurs pour genoux pour un soulagement temporaire de la douleur et une mobilité articulaire améliorée. Les masseurs qui combinent chaleur, vibration et thérapie par massage se sont révélés efficaces pour réduire les symptômes de l'arthrose du genou en améliorant la circulation et en soulageant la douleur.": "Clinical evidence supports the use of knee massagers for temporary pain relief and improved joint mobility. Massagers that combine heat, vibration, and massage therapy have been shown to be effective in reducing symptoms of knee osteoarthritis by improving circulation and relieving pain.",
    "Cette approche complète aide à gérer efficacement la douleur au genou, conduisant à une amélioration de la qualité de vie et du bien-être. Ces appareils offrent une alternative non invasive pour gérer la douleur au genou sans nécessiter de médicaments continus ou d'interventions chirurgicales.": "This comprehensive approach helps effectively manage knee pain, leading to improved quality of life and well-being. These devices offer a non-invasive alternative for managing knee pain without requiring ongoing medications or surgical interventions.",

    # Imagine section
    "Imaginez un Jour Sans Douleur au Genou": "Imagine a Day Without Knee Pain",
    "Imaginez vous réveiller rajeuni, libéré de l'inconfort persistant au genou qui vous ralentissait. Le Masseur de Soulagement du Genou a été conçu pour vous offrir exactement cela.": "Imagine waking up refreshed, free from the persistent knee discomfort that was slowing you down. The Knee Relief Massager was designed to give you exactly that.",

    # How to use steps
    "Comment Utiliser le Masseur de Soulagement du Genou": "How to Use the Knee Relief Massager",
    "Étape 1": "Step 1",
    "Placez le masseur autour de votre genou et fixez-le.": "Place the massager around your knee and secure it.",
    "Étape 2": "Step 2",
    "Ajustez les paramètres pour un traitement confortable mais efficace afin de stabiliser votre genou.": "Adjust the settings for comfortable yet effective treatment to stabilize your knee.",
    "Étape 3": "Step 3",
    "Vaquez à vos occupations quotidiennes en profitant d'un mouvement sans douleur.": "Go about your daily activities enjoying pain-free movement.",
    "Étape 4": "Step 4",
    "Utilisez-le pendant toute activité, de la marche au repos, garantissant un soutien continu du genou.": "Use it during any activity, from walking to resting, ensuring continuous knee support.",

    # Testimonials (additional)
    "Après avoir utilisé le masseur pour soulager mes douleurs au genou, mes douleurs ont considérablement diminué et je peux marcher beaucoup plus longtemps. Ça a changé ma vie !": "After using the massager to relieve my knee pain, my pain has significantly decreased and I can walk much longer. It changed my life!",
    "Travailler dans le bâtiment est éprouvant pour mes genoux. Le masseur de genoux m'a apporté le soulagement dont j'avais besoin pour supporter les longues journées de travail sans douleur. C'est un produit fantastique !": "Working in construction is hard on my knees. The knee massager provided me with the relief I needed to endure long workdays without pain. It's a fantastic product!",
    "Je souffre de douleurs chroniques au genou depuis des années, et rien ne semblait me soulager jusqu'à ce que j'essaie le masseur de genoux. Il est facile à utiliser et a considérablement amélioré mon quotidien.": "I have suffered from chronic knee pain for years, and nothing seemed to help until I tried the knee massager. It's easy to use and has significantly improved my daily life.",

    # Pricing CTA
    "Commandez Aujourd'hui et Obtenez des Paires GRATUITES Tant qu'il y a du Stock": "Order Today and Get FREE Pairs While Supplies Last",
    "Offre à durée limitée": "Limited Time Offer",
    "Profitez de la réduction maintenant": "Take Advantage of the Discount Now",
    "Essayez Vos Masseurs de Genou MAINTENANT Sans Risque Avec Notre Meilleure Offre !": "Try Your Knee Massagers NOW Risk-Free With Our Best Offer!",
    "Livraison GRATUITE et RAPIDE !": "FREE and FAST Shipping!",
    "REMARQUE :": "NOTE:",
    "Non Disponible sur Amazon ou eBay": "Not Available on Amazon or eBay",
    "La vente se termine aujourd'hui ou lorsque le stock actuel est épuisé": "Sale ends today or when current stock runs out",
    "Grande Réduction Spéciale": "Big Special Discount",
    "Garantie de Résultats ou Remboursement de 90 Jours": "90-Day Results or Money-Back Guarantee",
    "Livraison GRATUITE sur les commandes de plus de 50€": "FREE Shipping on orders over $50",

    # FAQ
    "Vous Avez une Question ? Nous Sommes Là pour Vous Aider !": "Do You Have a Question? We're Here to Help!",
    "À quelle vitesse puis-je m'attendre à ressentir un soulagement avec le Masseur de Soulagement du Genou ?": "How quickly can I expect to feel relief with the Knee Relief Massager?",
    "De nombreux utilisateurs signalent ressentir un soulagement dès les premières utilisations. Cependant, les résultats peuvent varier selon les conditions individuelles. Une utilisation régulière est recommandée pour de meilleurs résultats.": "Many users report feeling relief from the first uses. However, results may vary depending on individual conditions. Regular use is recommended for best results.",
    "À quelle fréquence dois-je utiliser le Masseur de Soulagement du Genou ?": "How often should I use the Knee Relief Massager?",
    "Vous pouvez utiliser le masseur quotidiennement pendant des séances de 15 à 20 minutes. Il est sûr pour une utilisation régulière et peut être intégré à votre routine quotidienne.": "You can use the massager daily for 15-20 minute sessions. It is safe for regular use and can be integrated into your daily routine.",
    "Que se passe-t-il si le Masseur de Soulagement du Genou ne fonctionne pas pour moi ?": "What if the Knee Relief Massager doesn't work for me?",
    "Nous offrons une garantie de remboursement de 90 jours. Si vous n'êtes pas satisfait des résultats, vous pouvez le retourner pour un remboursement complet - sans poser de questions.": "We offer a 90-day money-back guarantee. If you are not satisfied with the results, you can return it for a full refund - no questions asked.",
    "Pouvez-vous me parler de votre politique de retour ?": "Can you tell me about your return policy?",
    "Nous avons une politique de retour sans tracas de 90 jours. Si vous n'êtes pas entièrement satisfait, contactez simplement notre équipe de service client pour un remboursement complet.": "We have a hassle-free 90-day return policy. If you are not completely satisfied, simply contact our customer service team for a full refund.",

    # Guarantee
    "Essayez-le 90 Jours Avec Notre Garantie \"Résultats ou Remboursement\"": "Try It for 90 Days With Our \"Results or Money-Back\" Guarantee",
    "Notre promesse envers vous :": "Our promise to you:",
    "Nous croyons en nos produits et nous ne voulons pas que vous dépensiez un centime avant d'être sûr à 100% qu'il fonctionnera pour vous.": "We believe in our products and we don't want you to spend a penny before you are 100% sure it will work for you.",
    "C'est pourquoi nous offrons une garantie de 90 jours : résultats ou vous ne payez pas.": "That's why we offer a 90-day guarantee: results or you don't pay.",
    "Si pour une raison quelconque vous n'aimez pas le produit, vous récupérez tout votre argent.": "If for any reason you don't like the product, you get all your money back.",
    "En d'autres termes, vous ne payez que si vous bénéficiez d'un avantage du produit.": "In other words, you only pay if you benefit from the product.",
    "Sur la base des statistiques, nous osons dire que nous sommes presque sûrs à 100% que vous le ferez.": "Based on statistics, we dare say we are almost 100% sure you will.",

    # Return policy - additional
    "Essayez-le sans risque pendant 90 jours !": "Try it risk-free for 90 days!",
    "En d'autres termes, vous pouvez essayer le produit en utilisation normale pendant deux mois.": "In other words, you can try the product in normal use for two months.",
    "Retour gratuit si vous n'êtes pas satisfait.": "Free return if you are not satisfied.",
    "Contactez info@barakastore.net pour initier un remboursement.": "Contact info@barakastore.net to initiate a refund.",
    "Nous rembourserons les produits défectueux, les colis perdus et les commandes expédiées incorrectement.": "We will refund defective products, lost packages, and incorrectly shipped orders.",
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

def translate_json_file(filepath):
    """Translate a JSON file from French to English"""
    try:
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

        return True, f"Successfully translated {filepath}"
    except Exception as e:
        return False, f"Error translating {filepath}: {str(e)}"

def main():
    # All template files with French content
    template_files = [
        "templates/product.knee-massager.json",
        "templates/product.cold-laser-therapy.json",
        "templates/product.hot-compress-waist-massag.json",
        "templates/product.knee-brace.json",
        "templates/product.led-photon-therapy.json",
        "templates/product.octopus-scalp-massager.json",
        "templates/product.json",
        "templates/index.json",
        "templates/page.about.json",
    ]

    print("Starting comprehensive French to English translation...")
    print("=" * 70)

    success_count = 0
    error_count = 0

    for filepath in template_files:
        path = Path(filepath)
        if path.exists():
            success, message = translate_json_file(filepath)
            print(message)
            if success:
                success_count += 1
            else:
                error_count += 1
        else:
            print(f"File not found: {filepath}")
            error_count += 1

    print("=" * 70)
    print(f"Translation complete!")
    print(f"Successfully translated: {success_count} files")
    print(f"Errors: {error_count} files")

if __name__ == "__main__":
    main()
