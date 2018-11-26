interface AuthConfig {
  clientID: string;
  domain: string;
  callbackURL: string;
}

export const AUTH_CONFIG: AuthConfig = {
  clientID: '3B3L1WG7c9WyVhi117UJqXSiOmfLWoH7',
  domain: 'coursehub.auth0.com',
  callbackURL: 'http://localhost:4200/callback'
};
