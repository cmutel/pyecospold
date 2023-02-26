"""Test cases for the __helpers__ module."""

import pytest
from lxml.etree import DocumentInvalid

from pyecospold.core import parse_file_v1
from pyecospold.model_v1 import ProcessInformation


@pytest.fixture(name="process_information")
def _process_information() -> ProcessInformation:
    """Fixture for getting ReferenceFunction element."""
    ecoSpold = parse_file_v1("data/v1/v1_1.xml")
    return ecoSpold.dataset.metaInformation.processInformation


def test_set_attribute_validator(process_information: ProcessInformation) -> None:
    "It sets attribute correctly."
    casNumberInput = "    0000110-63-4\n"
    casNumberExpected = "0000110-63-4"
    process_information.referenceFunction.CASNumber = casNumberInput

    assert process_information.referenceFunction.CASNumber == casNumberExpected


def test_set_attribute_fail(process_information: ProcessInformation) -> None:
    "It raises DocumentInvalid error."
    with pytest.raises(DocumentInvalid):
        process_information.referenceFunction.amount = "abc"


def test_set_attribute_success(process_information: ProcessInformation) -> None:
    "It sets attribute correctly."
    amount = 2.0
    process_information.referenceFunction.amount = amount

    assert process_information.referenceFunction.amount == amount


def test_set_attribute_list_success(process_information: ProcessInformation) -> None:
    "It sets attribute list correctly."
    synonyms = ["0", "1", "2"]
    process_information.referenceFunction.synonyms = synonyms

    assert process_information.referenceFunction.synonyms == synonyms


def test_set_element_text_success(process_information: ProcessInformation) -> None:
    "It sets attribute correctly."
    startYear = "2000"
    process_information.timePeriod.startYear = startYear

    assert process_information.timePeriod.startYear == startYear
