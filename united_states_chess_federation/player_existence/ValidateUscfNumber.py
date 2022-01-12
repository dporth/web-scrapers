from bs4 import BeautifulSoup
import requests
from .RatedPlayerIdValidator import RatedPlayerIdValidator, ValidatorUsingRegex, RatedPlayerIdValidatorHttp

class UscfPlayerIdValidatorQueryString(ValidatorUsingRegex, RatedPlayerIdValidator, RatedPlayerIdValidatorHttp):
    def __init__(self, failed_validation_regex, **kwargs):
        self.failed_validation_regex = failed_validation_regex
        super().__init__(**kwargs)
    
    def validId(self, player_id):
        """Validates the provided id. Indicates whether or not this instance's
        api lookup says the id is valid."""
        lookup_request_url = self._getLookupUrlWithQueryString(player_id)
        lookup_page = self._fetchLookupRequest(lookup_request_url)
        soup = BeautifulSoup(lookup_page.content, 'html.parser')
        return not self.isErrorHtml(soup)

    def _getLookupUrlWithQueryString(self, player_id):
        """Returns this instance's request lookup url with a query string."""
        return f'{self.lookup_base_url}?name={player_id}'

    def _fetchLookupRequest(self, url):
        """Returns the HTTP request for the request url"""
        return requests.get(url, )

class UscfPlayerIdValidatorFormData(ValidatorUsingRegex, RatedPlayerIdValidator, RatedPlayerIdValidatorHttp):
    def __init__(self, failed_validation_regex, **kwargs):
        self.failed_validation_regex = failed_validation_regex
        super().__init__(**kwargs)
    
    def validId(self, player_id):
        """Validates the provided id. Indicates whether or not this instance's
        api lookup says the id is valid."""
        lookup_request_form_data = self._getLookupRequestFormDataDict(player_id)
        lookup_page = self._fetchLookupRequest(self.lookup_base_url, lookup_request_form_data)
        soup = BeautifulSoup(lookup_page.content, 'html.parser')
        return not self.isErrorHtml(soup)

    def _getLookupRequestFormDataDict(self, player_id):
        """Returns a dictionary for a post request
        to this instance's request lookup url."""
        return {'eMbrKey': f'{player_id}'}

    def _fetchLookupRequest(self, url, form_data):
        """Returns the HTTP request for the request url"""
        return requests.post(url, data=form_data, files=[])

if __name__ == '__main__':
    rated_player_validator_form_data = UscfPlayerIdValidatorFormData(
        lookup_base_url='https://www.uschess.org/assets/msa_joomla/MbrLst.php',
        failed_validation_regex='No matches were found for',
        )
    print(rated_player_validator_form_data.validId('13579606'))

    rated_player_validator_query_string = UscfPlayerIdValidatorQueryString(
        lookup_base_url='https://www.uschess.org/datapage/player-search.php',
        failed_validation_regex='Players found: 0',
        )
    print(rated_player_validator_query_string.validId('13579606'))