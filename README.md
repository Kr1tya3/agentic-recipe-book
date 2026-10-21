# Family Recipe Book

Healthy, easy recipes for a family with small children, written so that a meal-planning agent
(OpenClaw) can choose meals for the week and build the shopping list from them.

The recipes are chosen to:

- be liked by small children (mild, soft, often finger food, vegetables blended or hidden where
  that helps);
- take little hands-on time, with ordinary kitchen equipment;
- share a small set of about 50 ingredients, so a week of meals means a short shopping list and
  little waste.

## Layout

| Path | What it is |
|---|---|
| [`recipes/`](recipes/) | One Markdown file per recipe: YAML frontmatter for machines, prose steps for the cook. |
| [`INGREDIENTS.md`](INGREDIENTS.md) | The ingredient catalog: every ingredient id, the unit recipes use for it, shop pack size, aisle and shelf life. |
| [`TEMPLATE.md`](TEMPLATE.md) | Copy this to add a recipe. |
| [`scripts/validate.py`](scripts/validate.py) | Checks every recipe against this format and the catalog. |

## Recipes

| Recipe | Meals | Main protein | Total time | Freezes |
|---|---|---|---|---|
| [Banana Oat Pancakes](recipes/banana-oat-pancakes.md) | breakfast | egg | 20 min | yes |
| [Berry Overnight Oats](recipes/berry-overnight-oats.md) | breakfast | dairy | 5 min + overnight | no |
| [Veggie Egg Muffins](recipes/veggie-egg-muffins.md) | breakfast, lunch, snack | egg | 30 min | yes |
| [Cheese and Sweetcorn Quesadillas](recipes/cheese-sweetcorn-quesadillas.md) | lunch | dairy | 15 min | no |
| [Tomato and Red Lentil Soup](recipes/tomato-lentil-soup.md) | lunch, dinner | legume | 35 min | yes |
| [Pea and Sweetcorn Fritters](recipes/pea-sweetcorn-fritters.md) | lunch, dinner | egg | 25 min | yes |
| [Cheesy Broccoli Pasta](recipes/cheesy-broccoli-pasta.md) | lunch, dinner | dairy | 25 min | no |
| [Hidden Veg Bolognese](recipes/hidden-veg-bolognese.md) | dinner | beef | 55 min | yes |
| [Mini Meatballs in Tomato Sauce](recipes/mini-meatballs-tomato-sauce.md) | dinner | beef | 45 min | yes |
| [Chicken and Sweet Potato Traybake](recipes/chicken-sweet-potato-traybake.md) | dinner | chicken | 45 min | no |
| [Chicken and Veg Fried Rice](recipes/chicken-fried-rice.md) | dinner, lunch | chicken | 25 min | no |
| [Mild Chicken Fajita Wraps](recipes/chicken-fajita-wraps.md) | dinner | chicken | 25 min | no |
| [Salmon Fishcakes](recipes/salmon-fishcakes.md) | dinner | oily fish | 60 min | yes |
| [Creamy Salmon and Pea Pasta](recipes/salmon-pea-pasta.md) | dinner | oily fish | 20 min | no |
| [Sweet Potato and Lentil Dahl](recipes/sweet-potato-lentil-dahl.md) | dinner | legume | 40 min | yes |
| [Tuna and Sweetcorn Tomato Pasta](recipes/tuna-sweetcorn-tomato-pasta.md) ¹ | lunch, dinner | fish | 20 min | no |
| [Mild Chickpea and Coconut Curry](recipes/chickpea-coconut-curry.md) ¹ | dinner, lunch | legume | 30 min | yes |
| [Mild Bean and Sweetcorn Chilli](recipes/mild-bean-chilli.md) ¹ | dinner, lunch | legume | 35 min | yes |
| [Homemade Fish Fingers with Sweet Potato Wedges](recipes/crispy-fish-fingers-wedges.md) | dinner | white fish | 50 min + defrost overnight | no |
| [Baked Sweet Potato Falafel Wraps](recipes/sweet-potato-falafel-wraps.md) | dinner, lunch | legume | 50 min | yes |
| [Instant Pot Chicken and Pea Pilaf](recipes/instant-pot-chicken-pea-pilaf.md) ² | dinner, lunch | chicken | 40 min | no |
| [Instant Pot Mac and Cheese with Peas and Sweetcorn](recipes/instant-pot-mac-and-cheese.md) ² | lunch, dinner | dairy | 25 min | no |
| [Instant Pot Carrot and Sweet Potato Soup](recipes/instant-pot-carrot-sweet-potato-soup.md) ² | lunch, dinner | legume | 40 min | yes |
| [Instant Pot Mild Chicken and Chickpea Tagine](recipes/instant-pot-chicken-chickpea-tagine.md) ² | dinner | chicken, legume | 45 min | yes |
| [Instant Pot Red Lentil Bolognese](recipes/instant-pot-lentil-bolognese.md) ² | dinner | legume | 40 min | yes |
| [Slow Cooker Pulled Chicken Wraps](recipes/slow-cooker-pulled-chicken-wraps.md) ³ | dinner, lunch | chicken | 20 min + 4 h slow cook | yes |
| [Slow Cooker Beef and Vegetable Stew](recipes/slow-cooker-beef-stew.md) ³ | dinner | beef | 30 min + 5 h slow cook | yes |
| [Slow Cooker Minestrone Soup](recipes/slow-cooker-minestrone.md) ³ | lunch, dinner | legume | 45 min + 4 h slow cook | yes |
| [Slow Cooker Hidden Veg Pasta Sauce](recipes/slow-cooker-hidden-veg-pasta-sauce.md) ³ | dinner, lunch | legume | 30 min + 4 h slow cook | yes |
| [Slow Cooker Chicken and Sweetcorn Chowder](recipes/slow-cooker-chicken-sweetcorn-chowder.md) ³ | dinner, lunch | chicken | 30 min + 4 h slow cook | no |

¹ `cupboard-only`: needs nothing fresh or frozen, so it can always be cooked from household stock.
² `pressure-cook`: cooked under pressure in the Instant Pot.
³ `slow-cook`: cooked on the Instant Pot's Slow Cook setting; start it in the morning.

## Recipe format

Each file in `recipes/` starts with YAML frontmatter, followed by a Markdown body:

```yaml
---
id: chicken-fried-rice            # same as the file name, without .md
title: Chicken and Veg Fried Rice
meal_types: [dinner, lunch]       # breakfast | lunch | dinner | snack | dessert
servings: 4                       # always 4: see "Servings" below
prep_minutes: 10                  # hands-on preparation
cook_minutes: 15                  # cooking (hob or oven)
wait_minutes: 0                   # unattended time: chilling overnight, resting, marinating
difficulty: easy                  # easy | medium
protein: [chicken, egg]           # main protein sources, for variety across the week
diet: [dairy-free]                # vegetarian | vegan | gluten-free | dairy-free
allergens: [egg, soy, gluten]     # EU/UK 14 allergens, lower-case
tags: [quick, uses-leftovers]     # free-form, see "Tags" below
equipment: [wok-or-large-frying-pan]
storage: { fridge_days: 1, freezer: false }   # how long cooked leftovers keep
ingredients:
  - { item: long-grain-rice, qty: 250, unit: g, prep: "dry weight; cooked and cooled" }
  - { item: eggs, qty: 3, unit: piece, prep: beaten }
  - { item: lemon, qty: 0.5, unit: piece, optional: true }
---
```

Ingredient entries:

- `item`: an `id` from [INGREDIENTS.md](INGREDIENTS.md). Required.
- `qty`: a positive number. Required. Pasta, rice and lentils are always dry weight.
- `unit`: must be the unit the catalog gives for that item, so the same ingredient can be summed
  across recipes without conversion. Required.
- `prep`: free text for the cook ("grated", "to serve"). Quote it if it contains a comma.
- `optional`: `true` for garnishes and sides the meal works without. The planner may leave these
  off the shopping list.

`allergens` include the optional ingredients (to stay on the safe side). `diet` describes the
recipe without its optional ingredients.

The body always has a `# Title` heading, then `## Steps` (numbered), and usually
`## For little ones`, `## Make ahead and leftovers` and `## Swaps`. Water, salt and pepper appear
only in the steps; they are never shopped for.

### Units

`g`, `ml`, `piece`, `clove`, `slice`, `tin`, `tsp`, `tbsp`. Weighed foods use `g` or `ml`;
counted foods use `piece` with an approximate weight in the catalog.

### Servings

Every recipe is written for **4 servings: 2 adults and 2 small children (about 2-6 years old)**,
roughly 3 adult-sized portions. To scale, multiply every `qty` by the factor needed. Recipes
marked `batch-friendly` scale up well for freezing.

### Tags

Tags used so far: `quick` (30 min or less in total), `no-cook`, `make-ahead`, `batch-friendly`,
`freezer-friendly`, `one-pot`, `one-pan`, `hands-off`, `finger-food`, `lunchbox`,
`uses-leftovers`, `oily-fish`, `budget`, `no-added-sugar`, `build-your-own`, `comfort-food`,
`family-classic`, `freezer-staples`, `cupboard-only`, `pressure-cook`, `slow-cook`.

`cupboard-only` means every non-optional ingredient has catalog type `pantry` or `staple`: no
fresh or frozen food. The validator enforces this.

### Instant Pot recipes

Recipes with `instant-pot` in `equipment` are written for a 6-quart (5.7 l) Instant Pot and use its
button names (**Sauté**, **Pressure Cook**, **Slow Cook**). Each is tagged either `pressure-cook`
or `slow-cook`.

- `pressure-cook`: `cook_minutes` includes sautéing, the ~10 minutes the pot takes to come up to
  pressure, the pressure time and the release. Nothing needs starting ahead.
- `slow-cook`: the slow-cook time on **Slow Cook, More (high)** goes in `wait_minutes`; the steps
  also give the longer time on **Normal**, for leaving it all day. `prep_minutes` and
  `cook_minutes` are the hands-on work before and after.
- A 3-quart pot takes half quantities with the same pressure times. An 8-quart pot needs at least
  375 ml of thin liquid for pressure cooking; scale up the liquid if the recipe has less.

## Guidance for the planning agent

### Building the shopping list

1. Sum `qty` per `item` across the week's chosen recipes (scaled if needed). Units already match.
2. Decide whether to include `optional: true` ingredients.
3. Use the catalog `type`:
   - `fresh`: buy for this week's plan.
   - `frozen`, `pantry`: check household stock first; buy only if there isn't enough.
   - `staple`: buy only when nearly empty.
4. Round up to whole packs using `buy_as`.

### Planning the week

- **Perishables first.** Cook meals using fish, chicken, mince and baby spinach in the first 2-3
  days after shopping (catalog `keeps` column), or freeze the meat on the day of purchase.
- **Use up open packs.** A 200 g bag of spinach covers egg muffins, quesadillas and the salmon
  pasta or dahl in the same week. A 500 g pack of mince covers one bolognese, with the rest
  frozen or used in meatballs.
- **Chain leftovers.** Cook double rice with the dahl or meatballs and use the rest for
  [fried rice](recipes/chicken-fried-rice.md) the next day (within 24 hours). Double batches of
  `freezer-friendly` recipes give quick meals on busy days.
- **Variety.** Aim for fish twice a week, one of them oily (salmon recipes are tagged
  `oily-fish`; tinned tuna does not count as oily), as NHS guidance recommends for children
  and adults. Vary `protein` across the week and avoid repeating a recipe within 7 days.
- **Keep a cupboard meal in stock.** Always keep the ingredients for at least one `cupboard-only`
  recipe at home (for example 2 tins of tuna, a tin of sweetcorn, a carton of passata and a bag
  of pasta), and top them up when one is cooked. It is the fallback when plans change or a
  delivery is missed, and a good choice for the last day before the next shop, when fresh food
  has run out.
- **Time.** Prefer `quick` recipes on weekdays. Recipes with `wait_minutes` need to be started
  ahead (overnight oats the evening before, defrosting fish for the fish fingers).
- **Instant Pot.** There is one pot, so plan at most one Instant Pot recipe per meal. `slow-cook`
  recipes suit busy days when someone is home in the morning (start them `wait_minutes` plus
  `cook_minutes` before the meal on More, or earlier on Normal). `pressure-cook` recipes are good last-minute dinners. Cooking a
  slow-cook recipe double and freezing half gives a ready meal for later in the month.

### Children and safety

These rules are already applied in the recipes; keep them when adding new ones.

- No added salt in children's food; use low-salt stock cubes and reduced-salt soy sauce. The
  NHS recommends at most 2 g of salt a day for 1-3 year olds and 3 g for 4-6 year olds.
- No whole nuts for under-5s. Cut round foods (grapes, cherry tomatoes, blueberries) lengthways
  or squash them.
- No honey for babies under 12 months.
- Fish: check for bones. Eggs for young children should be fully cooked.
- Mild spices only (sweet paprika, cumin, mild curry powder); adults add heat at the table.

Source: NHS, [Foods to avoid giving babies and young children](https://www.nhs.uk/conditions/baby/weaning-and-feeding/foods-to-avoid-giving-babies-and-young-children/).

## Adding a recipe

1. Copy [TEMPLATE.md](TEMPLATE.md) to `recipes/<id>.md`.
2. Reuse catalog ingredients where possible. If a new one is really needed, add a row to
   [INGREDIENTS.md](INGREDIENTS.md) first.
3. Add the recipe to the table above.
4. Run `python3 scripts/validate.py` (needs `pip install pyyaml`) and fix anything it reports.
