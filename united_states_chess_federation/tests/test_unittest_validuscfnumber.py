import pytest
from player_existence.ValidateUscfNumber import UscfPlayerIdValidatorQueryString, UscfPlayerIdValidatorFormData

query_string_lookup_base_url='https://www.uschess.org/datapage/player-search.php'
form_data_lookup_base_url='https://www.uschess.org/assets/msa_joomla/MbrLst.php'
form_data_failed_validation_regex = 'Sorry - No matches were found for'
query_string_failed_validation_regex = 'Players found: 0'

@pytest.mark.unittest
def testValidIdUscfPlayerIdValidatorQueryString_InvalidId_False():
    """Test valid id method of UscfPlayerIdValidatorQueryString class."""
    invalid_id = '13579606'
    rated_player_validator_query_string = UscfPlayerIdValidatorQueryString(
        lookup_base_url=query_string_lookup_base_url,
        failed_validation_regex=query_string_failed_validation_regex,
        )
    assert rated_player_validator_query_string.validId(invalid_id) == False

@pytest.mark.unittest
def testValidIdUscfPlayerIdValidatorFormData_InvalidId_False():
    """Test valid id method of UscfPlayerIdValidatorFormData class."""
    invalid_id = '13579606'
    rated_player_validator_form_data = UscfPlayerIdValidatorFormData(
        lookup_base_url=form_data_lookup_base_url,
        failed_validation_regex=form_data_failed_validation_regex,
        )
    assert rated_player_validator_form_data.validId(invalid_id) == False

@pytest.mark.unittest
def testValidIdUscfPlayerIdValidatorQueryString_ValidId_True():
    """Test valid id method of UscfPlayerIdValidatorQueryString class."""
    valid_id = '15218444'
    rated_player_validator_query_string = UscfPlayerIdValidatorQueryString(
        lookup_base_url=query_string_lookup_base_url,
        failed_validation_regex=query_string_failed_validation_regex,
        )
    assert rated_player_validator_query_string.validId(valid_id) == True

@pytest.mark.unittest
def testValidIdUscfPlayerIdValidatorFormData_ValidId_True():
    """Test valid id method of UscfPlayerIdValidatorFormData class."""
    valid_id = '15218444'
    rated_player_validator_form_data = UscfPlayerIdValidatorFormData(
        lookup_base_url=form_data_lookup_base_url,
        failed_validation_regex=form_data_failed_validation_regex,
        )
    assert rated_player_validator_form_data.validId(valid_id) == True