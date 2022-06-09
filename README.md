# snowy_terminal

snowy_terminal is a little python script that make snow fall into your terminal. :)

## Installation

No package installation is necessary because this script use built-in package :
- random
- os
- time
- platform

## Usage

To run this script use :

```bash
python3 __main__.py
```
in a terminal/cmd/powershell window.

## Tweaks

You can change the number of snowflakes in __main__.py file :

```python
from classes import *

if __name__ == '__main__':
    screen = Screen(10) # Change 10 to the desired number of snowflakes.
    screen.start()
```

## License
- romainflcht
