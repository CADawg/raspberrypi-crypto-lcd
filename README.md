# Raspberry Pi - Crypto Ticker LCD
Crypto prices and 24 hour price changes from Coingecko, displayed over I<sup>2</sup>C

### Setup:

For GPIO Pin Layouts: See https://pinout.xyz/

You'll need a 16x2/1602 Screen with a backpack to convert it to a 2-data-pin I<sup>2</sup>C connection (plus 2 pins for 5V and Ground). Connect The VCC to any +5V on the PI and the GND to Ground on the PI. Connect the I<sup>2</sup>C to BCM2 (SDA) & BCM3 (SCL) Pins on the PI, and make sure your PI has I<sup>2</sup>C enabled in RaspiConfig:

![I2C Setting](https://imgur.com/I81310j.png)

If this is all done, when running `run.sh`, your LCD screen should show go blank for a little while, and then show the Steem & Hive Prices, Then The SBD and HBD prices, and finally the Dogecoin and Bitcoin prices.

### (Fiat) Currency Settings:

This app has symbol support for 4 currencies by default:
|Currency|Currency Symbol|Software Currency Symbol|
|---|---|---|
|US Dollars|$|`$`|
|British Pounds|£|`\4`|
|Euros|€|`\5`|
|Japaneese Yen|¥|`\\\\`|

If you want to change your currency from the default `GBP` / `£`, then you need to go into `steemprice.py` and edit the currency object on line 19. Currency codes must be a standard code recognised by CoinGecko, in all lowercase, e.g. `usd`, `gbp`, `jpy`, `eur`. Currency codes are as above, but you can add a custom code which will overwrite the Euros symbol.

To add your own currency symbol, Go [here](https://omerk.github.io/lcdchargen/) and draw the currency symbol, then copy the lines starting in `0b` (highlighted below)

![Lines starting 0b](https://i.imgur.com/oWS2LTh.png)

Then replace the lines from `74` - `81` with the data you copied from above and use `\5` as your currency symbol.

### Run it at startup?

Personally, I used [the method in this answer](https://raspberrypi.stackexchange.com/a/109626) to run the `run.sh` file at startup, and it works a charm, of course, other methods are available.
