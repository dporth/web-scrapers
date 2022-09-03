from abc import abstractmethod, ABC
import re

class RatedPlayerIdValidator(ABC):
    
    @abstractmethod
    def validId(self, player_id):
        """Validates the provided player id. Indicates whether or not this instance's
        api lookup says the id is valid."""
        pass

class RatedPlayerIdValidatorHttp:
    def __init__(self, lookup_base_url):
        self.lookup_base_url = lookup_base_url
        
class ValidatorUsingRegex:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def isErrorHtml(self, soup):
        error_indicator_regex = f'{self.failed_validation_regex}'
        error_occurrences = soup.findAll(text=re.compile(error_indicator_regex))
        return len(error_occurrences) > 0