import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from datetime import datetime
import math
import ssl
import re

######### ######### ######### ######### #########
######### ######### ######### ######### #########
            # CRAWL CRAWL CRAWL CRAWL #
######### ######### ######### ######### #########
######### ######### ######### ######### #########

# Send GET requests without running into SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Send a GET request to ESPN pages, pass in ctx context, crawl the webpage for HTML
espn_url = 'https://www.espn.com/soccer/standings/_/league/ENG.1/'
html = urllib.request.urlopen(espn_url, context=ctx).read()

# !!! HTML SOUP OBJECT HERE !!! #
# Use Python's html.parser on the urllib object
soup = BeautifulSoup(html, 'html.parser')


def get_bpl_team_names(soup_html):
    # Grab all anchor tags that match a soccer url - re module used here to find a match from regular expressions
    team_names = soup_html.find_all(href=re.compile('/soccer/team/_/id'))

    # Some links have no content which return as None, there are also abbreviated team names that are 3 characters long. We only want the actual team names
    premier_league_teams = list()

    for tag in team_names:
        if tag.string != None and len(tag.string) > 3:
            premier_league_teams.append(str(tag.string))
    
    return premier_league_teams[2:]
    # ['Arsenal', 'Manchester City', 'Newcastle United', 'Manchester United', 'Tottenham Hotspur', 'Brighton & Hove Albion', 'Fulham', 'Liverpool', 'Brentford', 'Chelsea', 'Aston Villa', 'Crystal Palace', 'Nottingham Forest', 'Leicester City', 'West Ham United', 'Leeds United', 'Wolverhampton Wanderers', 'AFC Bournemouth', 'Everton', 'Southampton']

def get_column_headers():
    return ['2022-2023', 'GP', 'W', 'D', 'L', 'F', 'A', 'GD', 'P']


### Return a list of all team's standings data
def get_team_stats(soup_html, team_names):
    table_stats = soup_html.find_all('span', class_='stat-cell')
    
    basket = list()
    final_product = list()
    count = 0

    for tag in table_stats:
        basket.append(tag.string)
        count += 1
        
        if count == 8:
            final_product.append(basket)
            count = 0
            basket = []
    
    for i in range(0, len(final_product)):
        standings_data_list = final_product[i]
        standings_data_list.insert(0, team_names[i])
    
    return final_product


###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### 

###### ###### ###### ###### ###### ###### 
###### ###### ###### ###### ###### ###### 


# Create and return the <thead> HTML element string
#   - loop through and turn col_headers list into <th>'s
#   - add a score="col" attribute
def create_t_head_html(col_headers):
    html_start = '''
    <thead>
        <tr>
    '''
    html_end = '''
        </tr>
    </thead>
    '''

    #  Let's use Python3's novelty f-strings to interpolate strings
    for col in col_headers:
        formatted = f'<th scope="col">{col}</th>'
        html_start += formatted
    
    return html_start + html_end

    

#  Create and return <tbody> HTML element string
#   - loop through and create the standings data rows

def create_t_body_html(standings_list_data): 
    row_header_html = str()
    
    tbody_opening_tag = '''
    <tbody class="t-body">
    '''
    tbody_closing_tag = '''
    </tbody>
    '''

    champions_league = standings_list_data[:4]
    europa_qualified = standings_list_data[4]
    relegation_teams = standings_list_data[-3:]

    for standing in standings_list_data:
        # Each 'standing' is a list of 9 items. This loop will run 9 times and finish
        # --> standing = ['Arsenal', '18', '15', '2', '1', '42', '14', '+28', '47'] ->
        
        for i in range(0, len(standing)):
            is_team_name = len(standing[i]) > 3
            
            if standing in champions_league and is_team_name:
                row_header_html += f'<tr class="champions-league"><td><b>{standing[i]}</b></td>'
            elif standing == europa_qualified and is_team_name:
                row_header_html += f'<tr class="europa-league"><td><b>{standing[i]}</b></td>'
            elif standing in relegation_teams and is_team_name:
                row_header_html += f'<tr class="relegation"><td><b>{standing[i]}</b></td>'
            elif is_team_name == True:
                row_header_html += f'<tr><td><b>{standing[i]}</b></td>'
            else:
                row_header_html += f'<td>{standing[i]}</td>'       
        row_header_html += '</tr>'
    
    final_html =  tbody_opening_tag + row_header_html + tbody_closing_tag
    return final_html


######### ######### ######### ######### #########
######### ######### ######### ######### #########

######### ######### ######### ######### #########
######### ######### ######### ######### #########

######### ######### ######### ######### #########
######### ######### ######### ######### #########

# IMPORTANT - returns a list of standings lists
team_names = get_bpl_team_names(soup)
team_stats_list = get_team_stats(soup, team_names)

# T E S T I N G --
# print(create_t_body_html(team_stats_list))

html_template_top = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>ESPN BPL Web Crawl</title>
</head>
<body>

<table>
'''
html_template_bottom = '''
</table>
<footer>
        <nav class="legend">
            <ul>
                <li class="cl">Champions League Qualified</li>
                <li class="europa">Europa League Qualified</li>
                <li class="rele">Relegation Danger!</li>
            </ul>
        </nav>
    </footer>
</body>
</html>
'''

######### ######### ######### ######### #########
######### ######### ######### ######### #########
######### ######### ######### ######### #########
######### ######### ######### ######### #########

######### ######### ######### ######### #########
######### ######### ######### ######### #########
######### ######### ######### ######### #########
######### ######### ######### ######### #########

######### ######### ######### ######### #########
########## PROGRAM STARTS HERE
html_file = open('bpl_standings.html', 'w')

# Build the first part of the HTML document.
html_file.write(html_template_top)

# Build out the caption element, use datetime to timestamp the ranking table. 
def generate_caption_html():
    today = datetime.now()
    hour = today.hour
    minute = today.minute
    second = float(today.second)

    caption_html = f'<!-- Keep table data organized and HTML5 compliant --> <caption>English Premier League Standings | Updated: {datetime.date(today)} @ {hour}:{minute}:{math.floor(second)}</caption>'

    return caption_html

######### ######### ######### ######### 
html_file.write(generate_caption_html())

# # Build the <thead> section of rankings table - setups up the table headers
col_headers = get_column_headers() # returns an array of table col headers
html_file.write(create_t_head_html(col_headers))

# # Build the <tbody> section of rankings table.
html_file.write(create_t_body_html(team_stats_list))

# # Attach the final part of the HTML - this will have the closing </table> </body> and </html> tags
html_file.write(html_template_bottom)

# # Finished, close the file input. You now have a "bpl_standings.html" document that you can open in a browser.
# # CSS styles included in the same directory and the .html already has a stylesheet linked for you
html_file.close()