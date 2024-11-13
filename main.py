from requests_html import HTMLSession
session = HTMLSession()


def generate_raider_io_character_spec_url(character_class: str, character_spec: str, region: str, season: str, page: int) -> str:
    '''
    https://raider.io/api/mythic-plus/rankings/specs?region=eu&season=season-tww-1&class=warlock&spec=affliction&page=101
    '''
    return f"https://raider.io/api/mythic-plus/rankings/specs?region={region}&season={season}&class={character_class}&spec={character_spec}&page={page}"
def generate_raider_io_character_details_url(character_path: str, season:str) -> str:
    '''
    https://raider.io/characters/eu/antonidas/Davilevo?season=season-tww-1
    '''
    return f"https://raider.io{character_path}?season={season}"

def fetch_url_request(url: str) -> "json":
    with session.get(url) as response:
        return response.json()




url_ranks = generate_raider_io_character_spec_url("warlock", "affliction", "eu", "season-tww-1", 1)
print(fetch_url_request(url_ranks))