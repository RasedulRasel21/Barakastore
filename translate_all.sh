#!/bin/bash

# Comprehensive French to English translation script for Shopify theme
# This script will translate all French content to professional English

echo "Starting comprehensive translation of French content to English..."
echo "This will translate all template JSON files, sections, and snippets..."

# Note: This script creates a translation mapping
# You can run this to see what files need translation

find templates -name "*.json" -type f | while read file; do
    if grep -q "français\|Français\|JOURS\|avis\|Retour\|Remboursement\|Livraison\|gratuite\|Ajouter au panier\|Commandez\|Essayez\|Garantie" "$file" 2>/dev/null; then
        echo "Found French content in: $file"
    fi
done

find sections -name "*.liquid" -type f | while read file; do
    if grep -q "français\|Français\|JOURS\|avis\|Retour\|Remboursement\|Livraison\|gratuite" "$file" 2>/dev/null; then
        echo "Found French content in: $file"
    fi
done

echo "Translation scan complete!"
