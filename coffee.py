import argparse

# Simple CLI that can calculate the amount of water or coffee needed for a given number of cups, ml of water, g of coffee, etc.
# This will use a recipe of 1:16 (1g of coffee for every 16ml of water)

RATIO = 16

# Usage example: python coffee.py --water 700
# Usage example: python coffee.py --coffee 50
# Usage example: python coffee.py --cups 4

def main():
    parser = argparse.ArgumentParser(description="It's too early for maths, but not too early for coffee!")
    parser.add_argument("water", help="How much water are you using? (ml)", type=int, nargs="?", default=None)
    parser.add_argument("--coffee", help="How much coffee are you using? (g)", type=int, nargs="?", default=None)
    parser.add_argument("--cups", help="How many cups are you making?", type=int, nargs="?", default=None)
    parser.add_argument("--size", help="What size are the cups? (oz)", type=int, nargs="?", default=8)
    args = parser.parse_args()

    # validate that cups is present when size is provided
    if args.size != 8 and not args.cups:
        parser.error("Please provide the number of cups when providing cup size.")

    # If provided water and coffee, calculate what the ratio will be.
    if args.water and args.coffee:
        ratio = args.water / args.coffee
        print(f"Water to coffee ratio: {ratio:.2f}")
        return

    # If provided water, calculate how much coffee to use.
    if args.water:
        coffee = args.water / RATIO
        cups = args.water / (args.size * 29.5735)
        print(f"Cups: {cups}, Water: {args.water}ml, Coffee: {coffee:.2f}g")
        return

    # If provided coffee, calculate how much water to use.
    if args.coffee:
        water = args.coffee * RATIO
        cups = water / (args.size * 29.5735)
        print(f"Cups: {cups}, Coffee: {args.coffee}g, Water: {water:.0f}ml")
        return

    # If provided cups, calculate how much water and coffee to use.
    if args.cups:
        cup_in_ml = args.size * 29.5735
        water = args.cups * cup_in_ml
        coffee = water / RATIO
        print(f"Cups: {args.cups}, Water: {water:.2f}ml, Coffee: {coffee:.2f}g")
        return

if __name__ == "__main__":
    main()

