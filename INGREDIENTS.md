# Ingredient catalog

Every ingredient used in a recipe must appear here. Recipes refer to ingredients by `id`, and
always use the `unit` given in this table, so quantities for the same ingredient can be summed
across a week's meal plan without conversion.

Columns:

- **id**: the key recipes use in `ingredients[].item`.
- **unit**: the only unit recipes may use for this ingredient (see units in [README.md](README.md#units)).
- **type**: how to shop for it.
  - `fresh`: perishable, buy for the week's plan.
  - `frozen`: freezer stock, top up when low.
  - `pantry`: long-life cupboard stock, check what's left before buying.
  - `staple`: used in small amounts (spices, oil, baking powder); only buy when nearly empty.
- **buy_as**: a typical shop pack, to round the summed quantity up to whole packs.
- **approx**: rough conversion for counted items, useful for substitutions and weighing.
- **keeps**: how long it lasts once bought (unopened unless noted), for ordering meals within a week.

| id | name | aisle | unit | type | buy_as | approx | keeps |
|---|---|---|---|---|---|---|---|
| banana | Banana | produce | piece | fresh | loose | 120 g peeled | 5 days, room temp |
| lemon | Lemon | produce | piece | fresh | loose | | 3 weeks, fridge |
| onion | Brown onion | produce | piece | fresh | 1 kg net (~6) | 150 g | 3 weeks, cool & dark |
| garlic | Garlic | produce | clove | fresh | bulb (~10 cloves) | | 4 weeks, cool & dark |
| carrot | Carrot | produce | piece | fresh | 1 kg bag (~10) | 100 g | 2 weeks, fridge |
| courgette | Courgette (zucchini) | produce | piece | fresh | loose | 200 g | 5 days, fridge |
| red-pepper | Red bell pepper | produce | piece | fresh | loose or 3-pack | 150 g | 1 week, fridge |
| broccoli | Broccoli | produce | g | fresh | head (~350 g) | | 5 days, fridge |
| baby-spinach | Baby spinach | produce | g | fresh | 200 g bag | | 4 days, fridge |
| potato | Potatoes (floury, e.g. Maris Piper / Russet) | produce | g | fresh | 2 kg bag | 200 g each | 2 weeks, cool & dark |
| sweet-potato | Sweet potato | produce | g | fresh | loose or 1 kg bag | 250 g each | 2 weeks, cool & dark |
| frozen-peas | Frozen peas | frozen | g | frozen | 1 kg bag | | months |
| frozen-sweetcorn | Frozen sweetcorn | frozen | g | frozen | 1 kg bag | | months |
| frozen-berries | Frozen mixed berries | frozen | g | frozen | 500 g bag | | months |
| frozen-white-fish | Frozen skinless boneless white fish fillets (cod, haddock or pollock) | frozen | g | frozen | 500 g bag | 100-120 g per fillet | months; defrost overnight in the fridge |
| eggs | Eggs, medium | dairy & eggs | piece | fresh | box of 12 | | 3 weeks, fridge |
| milk | Whole milk | dairy & eggs | ml | fresh | 2 l bottle | | 1 week, fridge |
| greek-yogurt | Plain full-fat Greek-style yogurt | dairy & eggs | g | fresh | 500 g pot | | 1 week, fridge |
| cheddar | Mild cheddar | dairy & eggs | g | fresh | 400 g block | | 3 weeks unopened, 1 week opened |
| cream-cheese | Light cream cheese | dairy & eggs | g | fresh | 180 g tub | | 2 weeks unopened, 4 days opened |
| butter | Unsalted butter | dairy & eggs | g | fresh | 250 g block | | 4 weeks, fridge |
| chicken-thighs | Boneless skinless chicken thigh fillets | meat & fish | g | fresh | 500 g or 1 kg pack | | 2 days, fridge (or freeze) |
| beef-mince | Lean beef mince (5-10% fat) | meat & fish | g | fresh | 500 g pack | | 2 days, fridge (or freeze) |
| salmon-fillets | Skinless boneless salmon fillets | meat & fish | piece | fresh | 4-pack | 120 g each | 2 days, fridge (or buy frozen) |
| wholemeal-bread | Wholemeal sliced bread | bakery | slice | fresh | 800 g loaf (~20 slices) | | 5 days, or freeze |
| wholemeal-tortillas | Wholemeal tortilla wraps (~25 cm) | bakery | piece | fresh | pack of 8 | | 2 weeks unopened |
| rolled-oats | Rolled oats | pantry | g | pantry | 1 kg bag | | months |
| plain-flour | Plain flour | pantry | g | pantry | 1.5 kg bag | 1 tbsp ≈ 8 g | months |
| wholemeal-pasta | Wholemeal pasta (any shape) | pantry | g | pantry | 500 g bag | | months |
| long-grain-rice | Long-grain or basmati rice | pantry | g | pantry | 1 kg bag | | months |
| red-lentils | Split red lentils | pantry | g | pantry | 500 g bag | | months |
| chopped-tomatoes | Chopped tomatoes | pantry | tin | pantry | 400 g tin | | months |
| passata | Passata (sieved tomatoes) | pantry | g | pantry | 500 g carton | | months; 5 days opened, fridge |
| tomato-puree | Tomato purée (double concentrate) | pantry | tbsp | staple | 200 g tube | 1 tbsp ≈ 15 g | months; 4 weeks opened, fridge |
| chickpeas | Chickpeas in water, no added salt | pantry | tin | pantry | 400 g tin | 240 g drained | months |
| kidney-beans | Red kidney beans in water, no added salt | pantry | tin | pantry | 400 g tin | 240 g drained | months |
| tinned-sweetcorn | Sweetcorn in water, no added sugar or salt | pantry | tin | pantry | 198 g tin | 165 g drained | months |
| tinned-tuna | Tuna chunks in spring water | pantry | tin | pantry | 145 g tin | 110 g drained | months |
| coconut-milk | Light coconut milk | pantry | ml | pantry | 400 ml tin | | months; 2 days opened, fridge |
| stock-cube | Low-salt vegetable stock cube | pantry | piece | staple | box of 8-10 | makes 500 ml | months |
| soy-sauce | Reduced-salt soy sauce | pantry | tbsp | staple | 150 ml bottle | | months |
| olive-oil | Olive oil | pantry | tbsp | staple | 500 ml bottle | | months |
| baking-powder | Baking powder | pantry | tsp | staple | 100 g tub | | months |
| cinnamon | Ground cinnamon | spices | tsp | staple | jar | | months |
| cumin | Ground cumin | spices | tsp | staple | jar | | months |
| paprika | Sweet (not hot) paprika | spices | tsp | staple | jar | | months |
| mild-curry-powder | Mild curry powder | spices | tsp | staple | jar | | months |
| dried-oregano | Dried oregano | spices | tsp | staple | jar | | months |
| garlic-granules | Garlic granules | spices | tsp | staple | jar | 0.25 tsp ≈ 1 clove | months |

Not listed on purpose: tap water, salt and black pepper. Recipes never add salt to the
children's food; adults season their own plates at the table.

## Allergen notes

- **Stock cubes** often contain **celery**, and sometimes milk or gluten. Recipes using them list
  `celery`; check the label of the brand actually bought.
- **Soy sauce** usually contains **wheat** (gluten). Tamari is a gluten-free swap.
- **Oats** are listed as `gluten` because most oats are processed alongside wheat. Certified
  gluten-free oats exist.
