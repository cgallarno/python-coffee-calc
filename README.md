# Coffee CLI

A simple command-line interface (CLI) tool to calculate the amount of water or coffee needed for a given number of cups, milliliters of water, grams of coffee, etc. This tool uses a recipe ratio of 1:16 (1g of coffee for every 16ml of water).

## Usage

### Basic Usage

```sh
python3 coffee.py [options]
```

### Options

- `water`: The amount of water in milliliters (ml).
- `--coffee`: The amount of coffee in grams (g).
- `--cups`: The number of cups.
- `--size`: The size of the cups in ounces (oz). Default is 8 oz.

### Examples

1. Calculate the amount of coffee needed for 700ml of water:
    ```sh
    python3 coffee.py 700
    ```

2. Calculate the water to coffee ratio for 700ml of water and 50g of coffee:
    ```sh
    python3 coffee.py 700 --coffee 50
    ```

3. Calculate the amount of water needed for 50g of coffee:
    ```sh
    python3 coffee.py --coffee 50
    ```

4. Calculate the amount of water and coffee needed for 4 cups of 8oz each:
    ```sh
    python3 coffee.py --cups 4
    ```

5. Calculate the amount of water and coffee needed for 4 cups of 12oz each:
    ```sh
    python3 coffee.py --cups 4 --size 12
    ```

## License

This project is licensed under the MIT License.
