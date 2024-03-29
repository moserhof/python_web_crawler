# Python Command Line Tool: HTML table build of Premier League Standings via ESPN Data

##### Using Python, send a GET request to ESPN's [Barclay Premier League Standings Table](https://www.espn.com/soccer/standings/_/league/ENG.1/) and crawl through the HTML Response to locate and capture the *Barclay Premier League* standings data.

##### After all table data has been mined, programatically build a new HTML document called `bpl_standings.html`. The final product is a minimalist, semantic HTML table (styles included under `styles.css`)!

## Programming languages
- Python
- HTML
- CSS

## Python Packages (PyPI)
- Urllib.request, Urllib.parse, Urllib.error
    - to send GET request and read in response
- SSL
    - to help us bypass the `https` certificate errors we'll run into when making our GET request
    - passed into the `context` parameter in `urllib.request.open()`
- BeautifulSoup ([_source_](https://beautiful-soup-4.readthedocs.io/en/latest/))
    - to easily parse the HTML and heist the goodies
- Datetime
    - to timestamp _when_ we retrieved the rankings data from ESPN (_found in the caption of the HTML table_)
- Math
    - to make our timestamp more understandable using the `Math.floor()`
- Re (regular expressions)
    - to help us locate BPL teams via BeautifulSoup's built-in method
    - check `script.py` to see this in action -> `get_bpl_team_names(soup_html)`
---
### This is the page that we crawl
<img width="1397" alt="espn_page" src="https://user-images.githubusercontent.com/33382461/213992247-59dd65ca-c734-4875-a7b9-9ac7e6dd2999.png">

### Using browser developer tools, we can take a gander at the HTML markup used by ESPN. We also have a way to scope out the CSS used.
<img width="1397" alt="espn_with_dev_tools" src="https://user-images.githubusercontent.com/33382461/213993281-973732c0-8e52-4e23-a714-5411d2ec1e58.png">

---
### Our Python web crawler needs to creep around ESPN's HTML markup and _only_ extract the data we really care about, ignoring the rest.
- Table column names
- Team names
- Row stats for each team, which include the following:
    - Current season
    - Games played
    - Wins
    - Draws
    - Losses
    - Goals for
    - Goals against
    - Goal difference
    - Total points earned

There are code comments galore, this helps when debugging or adding new functionality.

### How to run

1. Open your favorite command line (iTerm, Terminal etc.) 
2. Fork and download the the repo
3. Go into the `python_web_crawler` folder | --> `$ cd python_web_crawler`
4. Type `$ python3 script.py`

Open the `bpl_standings.html` file that got generated. Behold the _updated __BPL Standings Table___, rendered with elegantly simple CSS.

`$ open bpl_standings.html`

💥 **BONUS** 💥 Current EU League statuses and more!

- Champions League 🔵
- Europa League 🟡
- Relegation 🔴


The `styles.css` is already hooked up for you!

---
# The final result!
<img width="1486" alt="new_html_table" src="https://user-images.githubusercontent.com/33382461/213997306-f53d49f8-4da8-4cf9-a176-ec8ee03a2ae3.png">

## 🛡️ Feel free to check for accuracy at the [ESPN Premier League Standings page](https://www.espn.com/soccer/standings/_/league/ENG.1/).
