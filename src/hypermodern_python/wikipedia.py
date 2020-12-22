import click
import requests

API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"

def random_page(language):
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as error:
        err_message = str(error)
        # click.secho(f"Error: {err_message}", fg="red")
        raise click.ClickException(err_message)