#!/usr/bin/env python
from os.path import dirname, abspath, join
import argparse
import sys

sys.path.append(abspath(join(dirname(__file__), '..', 'src')))

from api_config import ApiConfig
from access_token import AccessToken
from oauth_scope import Scope
from pin import Pin

def main(argv=[]):
    parser = argparse.ArgumentParser(description='Get Pinterest OAuth token')
    parser.add_argument('-p', '--pin_id', required=True, help='pin identifier')
    args = parser.parse_args(argv)

    # get configuration from defaults and/or the environment
    api_config = ApiConfig()
    api_config.verbosity = 3

    # Note: It's possible to use the same API configuration with
    # multiple access tokens, so these objects are kept separate.
    access_token = AccessToken(api_config)
    access_token.fetch(scopes=[Scope.READ_PINS])

    pin = Pin(args.pin_id, api_config, access_token)
    pin_data = pin.get()
    pin.print_summary(pin_data)

if __name__ == '__main__':
    main(sys.argv[1:])
