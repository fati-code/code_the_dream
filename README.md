# Country Region Explorer

Pick a region, and this tool shows you every country in it: name, capital, population, and area.

Built for the Code the Dream Python Advanced prework.

## What it does

Type a region like Europe or Asia. The program pulls live data for every country from the countries.dev API, keeps only the ones in your region, and prints them in a clean, easy-to-read list.

It also handles the things that can go wrong:

- **No internet?** You'll get a friendly message to check your connection.
- **Typed nothing?** It reminds you to enter a region.
- **Region doesn't exist?** It tells you no countries were found.
- **Missing data?** Some countries don't list a capital or area, so those show as "N/A" instead of crashing the program.

## API used

[countries.dev](https://countries.dev/docs): free, no API key, no signup. This project uses the `/countries` endpoint.

## How to run it

1. Install what you need:

   ```
   pip install -r requirements.txt
   ```

2. Start the program:

   ```
   python main.py
   ```

3. Enter a region: Africa, Americas, Asia, Europe, or Oceania.

## Example

```
Enter a region: oceania
Name: Wallis and Futuna
Capital: Mata-Utu
Population: 11,750
Area: 142
------------------------------
```