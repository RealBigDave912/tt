import pytest
from unittest.mock import AsyncMock
import ccxt
from tt.config import settings
from tt.plugins.cex_exchange_plugin import CexExchangePlugin


@pytest.fixture(scope="session", autouse=True)
def set_test_settings_CEX():
    settings.configure(FORCE_ENV_FOR_DYNACONF="cex")


@pytest.fixture(name="order")
def order_params():
    """Return order parameters."""
    return {
        'action': 'BUY',
        'instrument': 'BTCUSDT',
        'quantity': 10,
    }


@pytest.fixture(name="plugin")
def test_fixture_plugin():
    return CexExchangePlugin()


def test_dynaconf_is_in_testing_env_CEX():
    print(settings.VALUE)
    assert settings.VALUE == "On Testing CEX_binance"
    assert settings.cex_name == "binance"
    assert settings.cex_api == 'api_key'


@pytest.mark.asyncio
async def test_plugin(plugin):
    enabled = plugin.enabled
    exchange = plugin.exchange
    assert enabled is True
    assert isinstance(exchange, ccxt.binance)

@pytest.mark.asyncio
async def test_parse_quote(plugin, caplog):
    """Test parse_message balance """
    enabled = plugin.enabled
    exchange = plugin.exchange
    print(exchange.id)
    await plugin.handle_message('/q BTCUSDT')
    assert "🏦" in caplog.text


@pytest.mark.asyncio
async def test_info_message(plugin):
    """test exchange cex"""
    output = plugin.info_message()
    assert output is not None


@pytest.mark.asyncio
async def test_execute_order(plugin, order):
    plugin.exchange.execute_order = AsyncMock()
    await plugin.handle_message(order)
    plugin.exchange.execute_order.assert_called_once()


# @pytest.mark.asyncio
# async def test_parse_balance(plugin):
#     """Test balance """
#     # get_account_balance= AsyncMock()
#     await plugin.handle_message('/bal')
#     get_account_balance.assert_called_once

# @pytest.mark.asyncio
# async def test_parse_position(plugin):
#     """Test position """
#     get_account_position= AsyncMock()
#     await plugin.handle_message('/pos')
#     get_account_position.assert_called_once
