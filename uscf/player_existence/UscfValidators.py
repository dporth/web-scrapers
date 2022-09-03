from bs4 import BeautifulSoup
import requests
from player_existence.PlayerIdValidator import PlayerIdValidator, ValidatorUsingRegexMixin, ValidatorHttpMixin

class UscfPlayerIdValidatorQueryString(PlayerIdValidator, ValidatorUsingRegexMixin, ValidatorHttpMixin):
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

class UscfPlayerIdValidatorFormData(PlayerIdValidator, ValidatorUsingRegexMixin, ValidatorHttpMixin):
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