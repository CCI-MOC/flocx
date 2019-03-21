import pytest
from tradingPlatform import api


#def test_AssertTrue():
#    assert True

def test_accept_bid():
    """Accepts bids from users"""
    sample_bid = {'buying_price_hourly': 10,
                  'duration_hours': 40,
                  'server_config': {'CPU': 16, 'RAM_GB': 64},
                  'server_id': 'alphnumericid_012',
                  'server_qty': 12
                  }

    bid_id = 201903210055_01


    result = api.accept_bid(sample_bid)
    assert result == bid_id

def test_accept_offer():
    """ Accepts offer from users"""
    assert False

def test_get_bid():
    """"Returns details of a particular bid to user"""

    bid_id = 201903210055_01
    result = api.get_bid(bid_id)
    result_bid = { 'bid_id':201903210055_01,
                   'buying_price_hourly': 10,
                   'duration_hours': 40,
                   'server_config': {'CPU': 16, 'RAM_GB': 64},
                   'server_id': 'alphnumericid_012',
                   'server_qty': 12
                   }
    assert result == result_bid


def test_get_offer():
    """Returns details of a particular offer to user"""
    assert False

def test_delete_bid():
    """ Remove the bid from its database"""
    assert False

def test_delete_offer():
    """ Removes offer from its database"""
    assert False
