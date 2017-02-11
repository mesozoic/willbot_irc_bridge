from multiprocessing import Queue
import mock
import pytest

import irc_bridge


@pytest.yield_fixture
def mock_reactor(monkeypatch):
    mock_reactor = mock.Mock()
    monkeypatch.setattr(irc_bridge, 'reactor', mock_reactor)
    yield mock_reactor


@pytest.fixture
def mock_bridge(mock_reactor):
    bridge = irc_bridge.IrcHipchatBridge(
        host='fakeserver.example.com',
        port=8000,
        password='',
        nickname='bridge',
        channels=[],
        use_ssl=False,
        hipchat_to_irc_queue=Queue(),
        irc_to_hipchat_queue=Queue(),
    )
    bridge.ircbot = mock.Mock()
    bridge.ircbot.msg = mock.Mock()
    return bridge


def test_update_irc(mock_bridge):
    raise NotImplementedError()
