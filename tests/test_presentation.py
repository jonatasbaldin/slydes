import pytest

from slydes import Presentation
from slydes.presentation import RIGHT_KEY, DOWN_KEY, INTERRUPT, LEFT_KEY, UP_KEY


class TestPresentLoop:

    @pytest.fixture
    def mocked_read_input(self, mocker):
        def inner(keys):
            mocker.patch('slydes.presentation.Presentation._read_input',
                         lambda x: keys.pop(0))
        return inner

    @pytest.fixture
    def mocked_next(self, mocker):
        return mocker.patch('slydes.presentation.Presentation.next')

    @pytest.fixture
    def mocked_previous(self, mocker):
        return mocker.patch('slydes.presentation.Presentation.previous')

    def test_present_interrupt(self, mocked_read_input, mocked_next):
        mocked_read_input(keys=[INTERRUPT])

        talk = Presentation()
        talk.present()

        assert mocked_next.call_count == 1

    @pytest.mark.parametrize('key, label', (
            (RIGHT_KEY, 'Right Arrow Key'),
            (DOWN_KEY, 'Down Arrow Key')
        )
    )
    def test_present_next(self, key, label, mocked_read_input, mocked_next):
        mocked_read_input(keys=[key, INTERRUPT])

        talk = Presentation()
        talk.present()

        assert mocked_next.call_count == 2

    @pytest.mark.parametrize('key, label', (
            (LEFT_KEY, 'Left Arrow Key'),
            (UP_KEY, 'Up Arrow Key')
        )
    )
    def test_present_previous(self, key, label, mocked_read_input, mocked_next,
                              mocked_previous):
        mocked_read_input(keys=[key, INTERRUPT])

        talk = Presentation()
        talk.present()

        assert mocked_next.call_count == 1
        assert mocked_previous.call_count == 1
