# UberNet API Documentation #
This is an overview of UberNet REST API endpoints.
For details check out the individual documents.

## Available Hosts ##
These API calls are at least available on `http://uberent.com` and `https://uberent.com`.
There is also `https://uberdevent.com` for which you probably need special credentials.

The file `cacert.pem` contains the CA certificate needed to verify the identity of `https://uberent.com`.
You only need it if your certificate store doesn't already have the *Go Daddy Root Certificate Authority - G2* certificate.

## Authentication ##
In order to use most of the service endpoints described here, you need to have a valid session ticket.
Session tickets are requested from [`/GC/Authenticate`](https://pa-pyrus.github.io/ubernet/GC/Authenticate.html).
They are a rather large string identifying your current session.
This string needs to be passed as the value of the `X-Authorization` HTTP request header for most calls.

## Miscellaneous ##
This section details various endpoints not belonging to a larger topic.

* [`GameClient/GetNews`](https://pa-pyrus.github.io/ubernet/GameClient/GetNews.html) can be used to retrieve a certain number of news items for a specific game.
