# -*- coding: utf-8 -*-

"""
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import I2C_LCD_driver
from time import *
import urllib3
import json

http = urllib3.PoolManager()
mylcd = I2C_LCD_driver.lcd()

# Currency Symbols:
# ¥ -> \\\\
# $ -> $
# £ -> \4 (Custom Font)
# € -> \5 (Custom Font) [Will be other if modified]
# Others - Add font to below font array (draw here -> https://omerk.github.io/lcdchargen/) and then copy all of the lines starting with 0, and replace the lines in the marked array,
# Then use symbol \5 for your currency.

currency = {"code":"gbp", "symbol": "\4"}

font = [
    [
        0b01001,
        0b10010,
        0b10010,
        0b10010,
        0b01001,
        0b01001,
        0b01001,
        0b10010
    ],
    [
        0b00100,
        0b01000,
        0b01000,
        0b01000,
        0b00100,
        0b00100,
        0b00100,
        0b01000
    ],
    [
        0b00000,
        0b00010,
        0b00101,
        0b01110,
        0b11111,
        0b01110,
        0b00101,
        0b00010
    ],
    [
        0b00000,
        0b10000,
        0b01000,
        0b10100,
        0b00010,
        0b10100,
        0b01000,
        0b10000
    ],
    [
        0b01110,
        0b10001,
        0b10000,
        0b10000,
        0b11100,
        0b10000,
        0b10000,
        0b11111
    ],
    # Custom Currency array, replace inner content with custom currency symbol from https://omerk.github.io/lcdchargen/
    [
        0b00110,
        0b01001,
        0b01000,
        0b11100,
        0b01000,
        0b11100,
        0b01001,
        0b00110
    ],
    [
        0b00100,
        0b11110,
        0b10101,
        0b10101,
        0b11111,
        0b10101,
        0b11110,
        0b00100
    ],
    [
        0b00100,
        0b11110,
        0b10101,
        0b10101,
        0b10101,
        0b10101,
        0b11110,
        0b00100
    ]
]    

mylcd.lcd_load_custom_chars(font)

while True:
    request_success = False
    while not request_success:
        try:
            request = http.request('GET', 'https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin%2CDogecoin%2CSTEEM%2CSTEEM-DOLLARS%2CHIVE%2CHIVE_Dollar&vs_currencies=' + currency["code"] + '&include_24hr_change=true')
            api_data = json.loads(request.data)
            request_success = True
        except:
            request_success = False
            sleep(5)
    sleep(10)
    mylcd.lcd_display_string(f'''\0\1 {currency["symbol"]}{api_data["steem"][currency["code"]]:.3f} {api_data["steem"][currency["code"] + "_24h_change"]:+.1f}%     ''',1)
    mylcd.lcd_display_string(f'''\2\3 {currency["symbol"]}{api_data["hive"][currency["code"]]:.3f} {api_data["hive"][currency["code"] + "_24h_change"]:+.1f}%     ''',2)
    sleep(10)
    mylcd.lcd_display_string(f'''\0\1$ {currency["symbol"]}{api_data["steem-dollars"][currency["code"]]:.3f} {api_data["steem-dollars"][currency["code"] + "_24h_change"]:+.1f}%     ''',1)
    mylcd.lcd_display_string(f'''\2\3$ {currency["symbol"]}{api_data["hive_dollar"][currency["code"]]:.3f} {api_data["hive_dollar"][currency["code"] + "_24h_change"]:+.1f}%     ''',2)
    sleep(10)
    mylcd.lcd_display_string(f'''\6 {currency["symbol"]}{api_data["bitcoin"][currency["code"]]:.0f} {api_data["bitcoin"][currency["code"] + "_24h_change"]:+.1f}%     ''',1)
    mylcd.lcd_display_string(f'''k\7 {currency["symbol"]}{api_data["dogecoin"][currency["code"]] * 1000:.3f} {api_data["dogecoin"][currency["code"] + "_24h_change"]:+.1f}%     ''',2)
    
