#!/usr/bin/env node
import {AccessToken} from '../src/access_token.js'
import {ApiConfig} from '../src/api_config.js'
import {Scope} from '../src/oauth_scope.js'

async function main () {
  // get configuration from defaults and/or the environment
  const api_config = new ApiConfig();

  // imports that depend on the version of the API
  const {User} = await import(`../src/${api_config.version}/user.js`);

  // Note: It's possible to use the same API configuration with
  // multiple access tokens, so these objects are kept separate.
  const access_token = new AccessToken(api_config, {
    scopes: [Scope.READ_USERS],
    refreshable: true
  });
  await access_token.oauth();
  console.log('hashed access token:', access_token.hashed());
  console.log('hashed refresh token:', access_token.hashed_refresh_token());

  // use the access token to get information about the user
  const user_me = new User('me', api_config, access_token);
  const user_me_data = await user_me.get();
  user_me.print_summary(user_me_data);
}

if (!process.env.TEST_ENV) {
  main();
}
