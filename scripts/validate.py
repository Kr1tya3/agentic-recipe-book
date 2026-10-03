#!/usr/bin/env python3
"""Check every recipe against the format described in README.md.

Usage: python3 scripts/validate.py
Requires PyYAML (pip install pyyaml). Exits non-zero if any recipe is invalid.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

MEAL_TYPES = {"breakfast", "lunch", "dinner", "snack", "dessert"}
DIFFICULTY = {"easy", "medium"}
PROTEINS = {"beef", "chicken", "fish", "egg", "dairy", "legume", "pork", "turkey", "tofu"}
DIETS = {"vegetarian", "vegan", "gluten-free", "dairy-free"}
ALLERGENS = {
    "gluten", "milk", "egg", "fish", "crustaceans", "molluscs", "peanuts", "nuts",
    "soy", "sesame", "celery", "mustard", "lupin", "sulphites",
}
REQUIRED = [
    "id", "title", "meal_types", "servings", "prep_minutes", "cook_minutes",
    "wait_minutes", "difficulty", "protein", "diet", "allergens", "tags",
    "equipment", "storage", "ingredients",
]
INGREDIENT_KEYS = {"item", "qty", "unit", "prep", "optional"}


def load_catalog():
    catalog = {}
    for line in (ROOT / "INGREDIENTS.md").read_text().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 8 and cells[0] not in ("id", "---") and re.fullmatch(r"[a-z0-9-]+", cells[0]):
            catalog[cells[0]] = {"unit": cells[3], "type": cells[4]}
    return catalog


def check(path, catalog):
    errors = []
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return ["missing YAML frontmatter"]
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return [f"invalid YAML: {e}"]

    for key in REQUIRED:
        if key not in data:
            errors.append(f"missing field '{key}'")
    if errors:
        return errors

    if data["id"] != path.stem:
        errors.append(f"id '{data['id']}' does not match file name '{path.stem}'")
    if f"# {data['title']}" not in text:
        errors.append("body should start with a '# <title>' heading")
    if data["servings"] != 4:
        errors.append("servings must be 4 (scale in the planner, not the recipe)")
    for field, allowed in [("meal_types", MEAL_TYPES), ("protein", PROTEINS),
                           ("diet", DIETS), ("allergens", ALLERGENS)]:
        bad = set(data[field]) - allowed
        if bad:
            errors.append(f"unknown {field}: {sorted(bad)}")
    if data["difficulty"] not in DIFFICULTY:
        errors.append(f"difficulty must be one of {sorted(DIFFICULTY)}")
    for key in ("prep_minutes", "cook_minutes", "wait_minutes"):
        if not isinstance(data[key], int) or data[key] < 0:
            errors.append(f"{key} must be a non-negative integer")
    if set(data["storage"]) != {"fridge_days", "freezer"}:
        errors.append("storage must have exactly fridge_days and freezer")

    for i, ing in enumerate(data["ingredients"]):
        where = f"ingredient {i + 1} ({ing.get('item', '?')})"
        extra = set(ing) - INGREDIENT_KEYS
        if extra:
            errors.append(f"{where}: unknown keys {sorted(extra)} (quote prep text containing commas)")
        item = ing.get("item")
        if item not in catalog:
            errors.append(f"{where}: not in INGREDIENTS.md")
            continue
        if ing.get("unit") != catalog[item]["unit"]:
            errors.append(f"{where}: unit must be '{catalog[item]['unit']}', got '{ing.get('unit')}'")
        if not isinstance(ing.get("qty"), (int, float)) or ing["qty"] <= 0:
            errors.append(f"{where}: qty must be a positive number")
    return errors


def main():
    catalog = load_catalog()
    failed = False
    recipes = sorted((ROOT / "recipes").glob("*.md"))
    used = set()
    for path in recipes:
        errors = check(path, catalog)
        if errors:
            failed = True
            for e in errors:
                print(f"{path.relative_to(ROOT)}: {e}")
        else:
            fm = yaml.safe_load(path.read_text().split("---\n")[1])
            used |= {i["item"] for i in fm["ingredients"]}
    unused = sorted(set(catalog) - used)
    if unused:
        print(f"note: catalog ingredients not used by any recipe: {unused}")
    print(f"{len(recipes)} recipes checked, {len(catalog)} catalog ingredients")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
