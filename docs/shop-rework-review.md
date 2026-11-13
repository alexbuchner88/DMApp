# Shop rework: review list

Source: there is no import file in the repo. The shop items live in Firestore. I read them live:
`sessions/_shared` has 4 shops with 88 items. The Shady Magic Shop is **Majeeks Shop**, which exists only in session `lostmine` (22 items).
The in-app importer (`impf` in `index.html`) reads only name, cost, weight, description, rules and dmNote, and only writes to `_shared`.

Columns: **Slots**, **Uses**, **Type** (actionType), **useText** (for the future actions panel), then the change and the reason.
`=` means it stays as it is apart from the new fields. Weight is dropped from all items because slots replace it.
Upgrades and addons are 0 slots (they become part of the weapon or armor).

---

## Thread and Needle (26 → 22 here, 1 moved out)

| | Item | Slots | Uses | Type | useText | Change / reason |
|---|---|---|---|---|---|---|
| = | Barbed Net | 1 | | Action | Throw 15 ft, Dex save or Restrained; escape hurts | Grappler/control |
| = | Reinforced Net | 1 | | Action | Throw 15 ft, Dex save or Restrained, escape DC 13 | |
| = | Weighted Net | 1 | | Action | Throw 10 ft, Dex save or Restrained and Prone | |
| ~ | Silk Fowler's Net | ½ | | Action | Throw 30 ft, Dex save or Restrained; fliers fall | Light variant (3 HP), so one step lower |
| ~ | Gambeson | 2 | | Passive | AC 11 + Dex; Adv on cold exposure saves | **2 slots.** At 1 slot it beats Leather Armour outright. Bulk is the trade-off |
| ~ | Oilskin Cloak | 1 | | Passive | Rain: Con saves −1 instead of −2 | **Rule change.** It fully cancelled the rain penalty for 5 gp. Now it halves it |
| ~ | Winter Furs | 2 | | Passive | Adv on cold exposure saves; Disadv vs heat | Rule is fine: in your weather rules, Advantage is the protective-gear level and only Cold Resistance auto-succeeds. Bulky, so 2 slots |
| = | Desert Wrap | ½ | | Passive | Adv on heat exposure saves | Light clothing |
| = | Ghillie Cloak | 1 | | Passive | Chosen terrain: Adv to Hide if you didn't move | Ranger |
| = | Shadowweave Cloak | 1 | | Passive | +2 Stealth in Dim Light or Darkness | Rogue |
| ~ | Smuggler's Coat | 1 | | Passive | 3 hidden pockets for ½-slot items, DC 15 to find | **Slot rewrite:** each pocket holds one ½-slot item; pocketed items take no pack slots |
| = | Reversible Outfit | 1 | | none | Swap looks in 1 min; Adv on Deception in role | |
| = | Shield Sling | ½ | | Bonus Action | Don or doff a shield | Tank quick item |
| ~ | Potion Bandolier | ½ | | Passive | 6 quick spaces for potions, flasks, bombs | **Slot rewrite:** counts as a quick-access bag with 6 spaces for ½-slot items. Drawing from it doesn't use your free object interaction |
| = | Climbing Harness | 1 | | Passive | Roped in: a fall stops after 10 ft, no damage | |
| = | Grip Gloves | 0 | | Passive | +1 Athletics to climb and hold ropes | |
| → | Knotted Silk Rope (50 ft) | | | | | **Move** to General Store next to the hemp rope (see there) |
| = | Rope Ladder (25 ft) | 2 | | none | No climb check; Utilize action to anchor | Bulky |
| ~ | Bedroll (lightweight) | ½ | | Passive | Counts as a bedroll | Renamed from Lightweight Bedroll to get the Bedroll icon. Light variant (Bedroll is 1) |
| = | Net Hammock | 1 | | none | Sleep off the ground; needs two anchors | |
| ~ | Two-Person Tent (quick-pitch) | 2 | | none | Tent; set up in 1 min | Renamed from Quick-Pitch Tent for the tent icon |
| ~ | Two-Person Tent (camouflage) | 2 | | none | Tent; DC 15 Perception to spot beyond 60 ft | Renamed from Camouflage Tent for the tent icon |
| ~ | Explorer's Pavilion | 3 | | none | Sleeps 4; rest DC −7 instead of −5 | **Rule change.** "Counts as sheltered" reads like a building (no roll), which fully cancels weather. Now it's a better tent |
| ~ | Sailcloth Tarp | 1 | | none | Shelter for 6 (−5 rest DC); no help in Gust or Storm | **Rule change.** A 1 gp tarp for 6 made tents pointless. Now it blows away in strong wind |
| ✕ | Folding Stretcher | | | | | **Cut:** rarely used, and the tarp already works as a stretcher |
| ✕ | Red Cloak | | | | | Cut. Story item; you'll re-add it when needed |

## Smith (20 → 31)

New standard armor, D&D 2024 rules and prices. Shields are in their own section below. The names are the library names, so the icons match (the library uses "Armour").

| | Item | Slots | Uses | Type | useText | Change / reason |
|---|---|---|---|---|---|---|
| + | Leather Armour | 1 | | Passive | AC 11 + Dex | 10 gp |
| + | Studded Leather Armour | 1 | | Passive | AC 12 + Dex | 45 gp. Standard upgrade of leather |
| + | Chain Shirt | 2 | | Passive | AC 13 + Dex (max 2) | 50 gp |
| + | Scale Mail | 2 | | Passive | AC 14 + Dex (max 2); Stealth Disadv | 50 gp |
| + | Breastplate | 2 | | Passive | AC 14 + Dex (max 2) | 400 gp |
| + | Half Plate Armour | 2 | | Passive | AC 15 + Dex (max 2); Stealth Disadv | 750 gp |
| + | Chain Mail | 3 | | Passive | AC 16; Str 13; Stealth Disadv | 75 gp |
| + | Splint Armour | 3 | | Passive | AC 17; Str 15; Stealth Disadv | 200 gp |
| + | Plate Armour | 3 | | Passive | AC 18; Str 15; Stealth Disadv | 1,500 gp |
| ~ | Brigandine | 3 | | Passive | AC 14 + Dex (max 2); quiet | **3 slots.** It was a Breastplate at half price. Now it's the cheap but heavy choice; the cost and quiet stay |
| ~ | Reinforced Fitting (upgrade) | 0 | | Passive | Medium armor: Str instead of Dex for AC (max 2) | Renamed from Strong Medium Armor. Its rule was in the description field. **Trade-off:** the armor takes 1 more slot. 50 → 100 gp |
| = | Parrying Dagger | ½ | | Passive | Off hand: +1 AC vs melee | Rogue/duelist |
| = | Chain Net | 2 | | Action | Throw 10 ft, Dex save or Restrained; hard to cut | Steel, so heavier than the other nets |
| = | Bolas | ½ | | Action | Throw 30 ft, Dex save or Speed 0 | |
| ~ | Throwing Knives | ½ | 6 | Bonus Action | Throw 15/30 ft, 1d4 Piercing | Renamed from "Throwing Knives (6)" because uses now count the knives. **Suggest:** no ability modifier to damage on the Bonus Action throw, as with the 2024 Light rule. Otherwise it beats two-weapon fighting |
| ~ | Broadhead Arrows | ½ | 10 | none | +1 damage; normal range halved | Uses = arrows |
| ~ | Whistling Arrows | ½ | 3 | none | Signal shot, heard 600 ft | Sold as 3 (3 gp); one arrow alone was too small to track |
| = | Balanced Weapon (upgrade) | 0 | | Passive | +1 to hit with this weapon | |
| = | Serrated Edge (upgrade) | 0 | | Passive | Crit: roll one more weapon die | |
| = | Hooked Polearm (upgrade) | 0 | | Passive | Hit (1/turn): Str save or pulled 5 ft | Grappler |
| ~ | Silver Wash | ½ | 3 | Action | Coat a weapon or 10 ammo: silvered for 1 h | 3 uses for 50 gp (was 1 use for 20 gp) |
| = | Steel Gorget (addon) | 0 | | Reaction | A crit becomes a normal hit, 1/Long Rest | Tank |
| ~ | Spiked Armour (addon) | 0 | | Passive | Grappling: 1d4 Piercing each turn | Renamed from Armor Spikes to get the library icon |
| + | Focus Bracer | ½ | | Passive | Your focus works while that hand holds a weapon | **Caster** (casters had nothing). 25 gp. Somatic components still need a free hand |

## Shields (Smith; replaces Shield, Buckler, Spiked, Polished Steel, Tower, Havel's, Pavise)

Six base shields: small, medium and large, each in an offensive and a defensive version.
- **Offensive:** Bash grows with size. Small and medium add Riposte. Large has no reaction (heavy shields stay slow).
- **Defensive:** what it protects grows with size: you (Block), your neighbour (Interpose), the group (Wall, Cover).
- No shield goes past +2 AC. Large shields pay with slots, Strength and Stealth.

| | Item | Slots | Type | AC | Str / Stealth | Properties | Cost | Category |
|---|---|---|---|---|---|---|---|---|
| + | Bossed Buckler | 1 | Reaction | +1 | | Bash 1d4 (Vex), Riposte | 5 gp | Armor |
| ~ | Strapped Buckler | 1 | Reaction | +1 | | Strapped, Block | 10 gp | Armor |
| ~ | Spiked Shield | 2 | Reaction | +2 | | Bash 1d6 (Push), Riposte | 15 gp | Armor |
| + | Kite Shield | 2 | Reaction | +2 | | Interpose | 15 gp | Armor |
| + | Spiked Tower Shield | 3 | Action | +2 | Str 13, Stealth Disadv | Bash 1d8 (Topple) | 30 gp | Armor |
| ~ | Tower Shield | 3 | Bonus Action | +2 | Str 13, Stealth Disadv | Wall, Cover | 30 gp | Armor |
| + | Shield Upgrade | 0 | Passive | | | Pick one: +1 AC, or one property from the same line | 150 gp | Armor |
| ~ | Pavise | 3 | Bonus Action | – | Str 15, Stealth Disadv | Cover (Three-Quarters) | 12 gp | Weapons (archer gear, not worn) |
| ~ | Havel's Shield | 4 | Passive | +3 | Str 17, Stealth Disadv, Speed −5 ft | – | 150 gp | Armor. The one oddity |
| ✕ | Shield, Buckler, Polished Steel Shield | | | | | | | Cut: replaced by the six above |

**Shield Upgrade:** one per shield. Choose either +1 AC, or one property that shield's line already uses. Offensive line: Bash, Riposte. Defensive line: Strapped, Block, Interpose, Wall, Cover. A large offensive shield can't gain a Reaction, which keeps heavy shields static. Example: a Kite Shield with Block, or a Strapped Buckler at +2.

**Properties (11 → 7):**
- **Bash:** a melee attack with the shield: its listed die + Str, Bludgeoning, with its listed mastery.
- **Block:** Reaction when you're attacked: +1 AC against that attack. (Flat +1, so no shield reaches +4.)
- **Riposte:** Reaction when a melee attack against you misses: make an Opportunity Attack against the attacker.
- **Interpose:** Reaction when a creature within 5 ft of you is attacked: +2 AC for it against that attack.
- **Strapped:** the hand stays free to hold a focus, torch or potion, but not a weapon. (Free-Handed is merged into this.)
- **Wall:** up to two allies within 5 ft of you get +1 AC. (The chain-cover clause is dropped.)
- **Cover:** Bonus Action to plant it. You and one ally behind it have Half Cover (Pavise: Three-Quarters) from the front. Your Speed is 0 until you pick it up (Bonus Action).
- Dropped: **Hook** (contested check, extra micromanagement), **Mounted**, **Free-Handed** (merged into Strapped), **Light**. Madu, Punch Buckler, Heater, Round and Center-Boss shields are not used.
- Shield Sling stays: it lets you don or doff any shield as a Bonus Action.

## Shop categories (new)

Each item gets a `cat`. Inside a shop, category chips appear above the items (All + only the categories that shop has), in both the DM view and on the tablet. No new shops needed.

| Category | Contents |
|---|---|
| Armor | Armor, shields, armor addons |
| Weapons | Weapons, ammo, weapon upgrades, Focus Bracer |
| Combat | Bombs, nets, bolas, caltrops, traps, oils, grease, smoke |
| Healing | Potions, healer items, antitoxin, salves |
| Travel | Weather clothing, tents, bedrolls, ropes, climbing gear, food |
| Tools | Thieves' tools, manacles, spyglass, lamp, bags, disguise, incense, everything else |

## Potion (20 → 25)

| | Item | Slots | Uses | Type | useText | Change / reason |
|---|---|---|---|---|---|---|
| = | Healing Draught | ½ | | Bonus Action | Drink or give: 1d4 + 2 HP | |
| = | Potion of Healing | ½ | | Bonus Action | Drink or give: 2d4 + 2 HP | |
| = | Potion of Greater Healing | ½ | | Bonus Action | Drink or give: 4d4 + 4 HP | |
| ~ | Mending Salve | ½ | 3 | none | Short Rest: the first Hit Die rolls max | 3 uses for 80 gp (was 1 for 30 gp) |
| ~ | Smelling Salts | 0 | 3 | Action | Wake a creature; a Stable creature at 0 HP gets 1 HP | 3 uses for 25 gp. Healer |
| ~ | Snakebite Tonic | ½ | | Bonus Action | Poisoned: save again now with Adv | **Rule change:** the 1 h Advantage is dropped. It was cheaper than Antitoxin and did more |
| + | Antitoxin (vial) | ½ | | Bonus Action | Adv on saves vs Poisoned for 1 h | 50 gp, 2024 rules |
| + | Healer's Kit | 1 | 10 | Action | Stabilize a creature at 0 HP, no check | 5 gp, 2024 rules |
| + | Field Bandage | ½ | 3 | Bonus Action | Stabilize a creature at 0 HP, no check | **Healer** quick variant: fewer uses, smaller, faster. 5 gp. Uses the Bandage icon |
| ~ | Restful Sleep Elixir | ½ | | none | Adv on your weather rest roll | **Rule change:** a 2024 Long Rest already restores all Hit Dice, so the old effect did nothing. It softens a bad-weather rest without cancelling it |
| = | Darkvision Draught | ½ | | Bonus Action | Darkvision 60 ft for 1 h | |
| = | Fleetfoot Tincture | ½ | | Bonus Action | +10 ft Speed for 10 min | |
| = | Bear's Brew | ½ | | Bonus Action | 2d6 + 2 temp HP; Adv on Str checks 1 min | Grappler |
| = | Liquid Courage | ½ | | Bonus Action | Adv vs Frightened 1 h; Disadv on Int checks | |
| = | Gillweed Gum | 0 | | Bonus Action | Breathe underwater 10 min; no Verbal spells | |
| = | Fireproof Gel | ½ | | Action | Fire Resistance for 1 min | |
| = | Flame Oil | ½ | | Action | Coat a weapon: +1d4 Fire for 1 min | |
| + | Alchemist's Fire (flask) | ½ | | Action | Throw 20 ft, Dex save or 1d4 Fire and Burning | 50 gp, standard, so Sticky has something to upgrade from |
| = | Sticky Alchemist's Fire | ½ | | Action | Throw 20 ft, Dex save or 1d6 Fire and Burning; hard to put out | |
| + | Acid (vial) | ½ | | Action | Throw 20 ft, Dex save or 2d6 Acid | 25 gp, standard |
| ~ | Corrosive Acid | ½ | | Action | As Acid; metal armor −1 AC | Renamed from Corrosive Acid Flask to get the Acid icon |
| = | Tanglefoot Bag | ½ | | Action | Throw 20 ft, Dex save or Restrained 1 min | |
| = | Thunderstone | ½ | | Action | Throw 30 ft: Con save or 1d6 Thunder and Deafened | |
| = | Flash Powder | ½ | | Action | Throw 20 ft: Con save or Blinded 1 turn | |
| ~ | Holy Water (flask) | ½ | | Action | Throw 20 ft, Dex save or 2d8 Radiant (Fiend/Undead) | Renamed to the library name |

## General Store (22 → 25)

| | Item | Slots | Uses | Type | useText | Change / reason |
|---|---|---|---|---|---|---|
| + | Caltrops (bag of 20) | ½ | 2 | Action | Cover 5 ft square: Dex save or 1 Piercing, Speed 0 | 1 gp, standard |
| ~ | Barbed Caltrops | ½ | 2 | Action | Cover 5 ft square: Dex save or 1d4, Speed 0 | Converted to uses (two 5 ft squares instead of one 10 ft); DC 15 to spot stays |
| ~ | Hunting Trap (folding) | 1 | | Bonus Action | Set trap: Dex save or 1d4 and Speed 0 | Renamed for the icon. Light variant (Hunting Trap is 2) |
| = | Toothed Bear Trap | 3 | | Action | Set trap: Dex save or 1d10 and Speed 0; Adv vs it | Big trap |
| = | Tripwire Bell Kit | ½ | | none | 10 min: 60 ft alarm perimeter | Ranger |
| ~ | Grease Jar | ½ | 2 | Action | Pour or throw 20 ft: 10 ft square, Dex save or Prone | Renamed from Grease Pot for the Jar icon. 2 uses |
| = | Smoke Bomb | ½ | | Action | Throw 30 ft: 10 ft cloud, Heavily Obscured | Rogue |
| ~ | Grappling Hook (folding) | ½ | | Action | Throw 50 ft at a ledge, DC 13 to catch | Renamed for the icon. Light variant (hook is 1) |
| = | Grappling Bolt | ½ | | Action | Fire a rope line up to 60 ft | Archer |
| ~ | Hempen Rope (knotted) | 1 | | none | +2 Athletics to climb it | Renamed. **Advantage → +2.** Advantage cancelled the rain penalty to climbing |
| ~ | Silk Rope (knotted) | ½ | | none | +2 Athletics to climb it | Moved from Thread and Needle; light variant. Same +2 change |
| ~ | Pole (collapsible) | 1 | | none | Packs to 2 ft; Utilize action to assemble | Renamed for the icon. Light variant (10-ft pole is 2) |
| ~ | Crampons | ½ | | Passive | Adv to stay standing on ice | Library name. **Rule change:** "Ice isn't Difficult Terrain" is removed because it came close to a full cancel. Advantage and the Stealth drawback stay |
| ~ | Thieves' Tools (fine) | ½ | | none | +1 to Thieves' Tools checks | Renamed for the icon |
| = | Lockpick Wire | 0 | | none | Hidden pick; Thieves' Tools with Disadv | |
| ~ | Manacles (masterwork) | 1 | | none | Escape DC 23, break DC 28 | Renamed for the icon |
| = | Cheap Spyglass | 1 | | none | Adv on sight Perception beyond 60 ft | |
| = | Glowcap Lamp | ½ | | none | Shake: light 15 ft for 1 h, works wet; 1/Long Rest | |
| = | Signal Mirror | 0 | | none | Sunlight flash, seen 3 miles | |
| ~ | Hardtack | ½ | 2 | none | 1 use = 1 day of food; never spoils | **Slot rewrite:** rations are ½ slot per day, so 2 days in ½ slot is half the weight. 1 gp |
| = | Hearty Stew Mix | ½ | | none | Short Rest meal: up to 5 eaters +1 per Hit Die | |
| ~ | Ginger Jerky | 0 | | none | +2 Con saves vs cold for 8 h | **Rule change.** Advantage for 2 gp at 0 slots made Winter Furs pointless. +2 now stacks with gear |
| ~ | Strong Black Tea | 0 | 3 | none | On watch: Adv on Perception 2 h; no sleep 4 h | 3 uses, 1 gp |
| ~ | Shovel (folding) | ½ | | none | Dig a 5 ft foxhole in 1 h | Renamed for the icon. Light variant (Shovel is 1) |
| + | Blocks of Incense | ½ | 3 | none | Ritual casting adds 5 min instead of 10 | **Caster.** 15 gp. Library name |

**Optional standards** (not counted above). Each light variant would have its standard version in the shop to compare against: Grappling Hook (1), Bedroll (1), Pole (10-foot) (2), Two-Person Tent (2), Hunting Trap (2), Shovel (1), Hempen Rope (1), Thieves' Tools (½). That's 8 more items at 2024 prices.

## Majeeks Shop (Shady Magic Shop, session `lostmine`, 22 items, all kept)

| | Item | Slots | Uses | Type | useText | Change / reason |
|---|---|---|---|---|---|---|
| ~ | Rope of Entanglement | 1 | | none | | Cost "50" → "50 gp" |
| ~ | Helmet of Mind Reading | 1 | | none | | Cost "50" → "50 gp" |
| ~ | Amulet of Magic Detection | 0 | | none | | Cost "50" → "50 gp" |
| ~ | Boots of Levitation | 1 | | none | | Cost "50" → "50 gp" (library icon) |
| = | Mirror of Undying Beauty | ½ | | none | Shows a young, beautiful you | |
| = | Lucky Rabbit's Foot | 0 | | none | 1/Long Rest: reroll a d20 | |
| = | Ring of Mild Warmth | 0 | | Passive | Adv on cold exposure saves | Advantage only, so it fits the weather rule |
| = | Whispering Skull | ½ | | Action | 1/day: ask one question | |
| = | Dancer's Slippers | ½ | | Passive | +5 ft Speed | |
| = | Coin of Two Heads | 0 | | none | Always lands on the called side | |
| ~ | Sack of Slightly Holding | 1 | | Passive | +3 pack slots | **Slot rewrite:** takes 1 slot and holds 3 slots of items (set Pack +3) |
| = | Jar of Eternal Fireflies | ½ | | none | Dim Light 10 ft, forever | |
| = | Amulet of Vigor | 0 | | Passive | Dawn: 5 temp HP | |
| = | Gloves of Sticky Fingers | 0 | | Passive | Adv on Sleight of Hand to lift or palm | |
| = | Hat of Questionable Disguise | ½ | | Action | 1/day: Disguise Self | |
| = | Unlabeled Potion | ½ | | Bonus Action | Drink: effect unknown | |
| = | Mystery Box | 1 | | none | Open it. No refunds | |
| = | Bottled Scream | ½ | | Action | Uncork: scream heard 300 ft | |
| = | Glass Eye | 0 | | Action | 1/Long Rest: see through it for 1 min | Library icon |
| = | Bloodthirsty Shortsword | 1 | | Action | Shortsword, +1 damage, magical | |
| = | Talking Lockpick | 0 | | none | +2 to Thieves' Tools checks | |
| ~ | Wand of Secrets | ½ | 3 | Action | Points to a trap or secret within 30 ft | Rule text moves from description to rules; 3 charges as uses; cost "65gp" → "65 gp" |

---

## Class coverage check

- **Archer:** Broadhead and Whistling Arrows, Pavise, Grappling Bolt, Silver Wash. OK.
- **Rogue:** Thieves' Tools (fine), Lockpick Wire, Smuggler's Coat, Shadowweave Cloak, Throwing Knives, Smoke Bomb, Flash Powder, Parrying Dagger. Good.
- **Tank:** 9 armors, 6 shields + upgrade, Gorget, Reinforced Fitting, Shield Sling. Good.
- **Grappler:** 5 nets, Bolas, Spiked Shield, Spiked Armour, Hooked Polearm, Bear's Brew, Manacles. Good.
- **Ranger/survival:** traps, Ghillie Cloak, camo tent, Tripwire Bell Kit, food, weather gear. Good.
- **Healer:** was potions only. Adds Healer's Kit, Antitoxin and **Field Bandage** (Bonus Action).
- **Caster:** had nothing. Adds **Focus Bracer** and **Blocks of Incense**.
- **Bonus Action quick items:** Throwing Knives, all potions, Antitoxin, Field Bandage, Shield Sling, folding trap, Polished and Tower Shield, Potion Bandolier for free draws.

## Weather check (normal items must not fully cancel a penalty)

Fixed: Oilskin Cloak, Explorer's Pavilion, Sailcloth Tarp, knotted ropes, Ginger Jerky, Crampons.
OK as is: Winter Furs, Gambeson, Desert Wrap and Ring of Mild Warmth give Advantage. In your rules that is the gear level, and only resistance (rare) auto-succeeds.

## Other things found

- Your slot guide doesn't match `item_sizes.json` (Armour folder: shields 1, Half Plate and Ring Mail 3, Chain/Scale/Splint/Plate 4). These are the sizes players get when they add armor by hand from suggestions.
- The importer ignores slots and uses and has no replace mode. Step 2 needs a small importer change (read slots, uses, actionType, useText; set stock 0).
- Old leftover fields on some items (`pic`, `kind`, `holds`, `spaces`, `stack`) aren't read by the app anymore. A full replace drops them.
