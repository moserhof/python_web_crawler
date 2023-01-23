# 🍫 | ESPN Web Crawler 🕸️

##### Using Python, send a GET request to ESPN's [Barclay Premier League Standings Table](https://www.espn.com/soccer/standings/_/league/ENG.1/) and crawl through the HTML to locate and heist all the juicy data.

##### After all table data has been mined, programatically build a new HTML document called `bpl_standings.html`. The final product is a semantically excellent and fully styled HTML table (styles included under `styles.css`)!

## Programming langauges
- Python
- HTML
- CSS
- Regular Expressions

## Python Package's (PyPI)
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

### Using developer tools, we can take a gander at the HTML markup used by ESPN. At first glance, it appears that there's not much going on, but there's surprising complexity under the hood
<img width="1397" alt="espn_with_dev_tools" src="https://user-images.githubusercontent.com/33382461/213993281-973732c0-8e52-4e23-a714-5411d2ec1e58.png">

---
### Our Python web crawler needs to creep around ESPN and _only_ extract the data we really care about, ignoring the rest of the noise!
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

I have included lots of code comments in all the files invovled with this project to help with understanding what the heck is going on. To run this yourself, fork the repo and call the Python script via your command line to see the magic unfold 🪄

`$ python3 script.py`

Doing this will set things in motion and build out the `bpl_standings.html` and place it in your current directory. If one already exists, it will get overwritten. 

Additionally, you can open the `bpl_standings.html` that's already included in the forked repo in your browser to see the **finished product**. The `styles.css` should already be hooked up as well!

`$ open bpl_standings.html`

---

<img width="1486" alt="new_html_table" src="https://user-images.githubusercontent.com/33382461/213997306-f53d49f8-4da8-4cf9-a176-ec8ee03a2ae3.png">
