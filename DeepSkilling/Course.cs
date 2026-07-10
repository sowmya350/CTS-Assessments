{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "Jwt": {
    "Key": "THIS_IS_A_DEMO_SECRET_KEY_CHANGE_ME_32BYTES+",
    "Issuer": "JwtAuthWebApi",
    "Audience": "JwtAuthWebApiClients",
    "ExpiryMinutes": "60"
  }
}
