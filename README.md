# UberNet API #
This is an unofficial documentation of UberNet REST API calls.
By no means is it complete or entirely accurate.

Each endpoint is documented in its own file.
All documentation is written in the Markdown dialect understood by [Python-Markdown](http://pythonhosted.org/Markdown/).
It relies on the `def_list` and `codehilite` extensions.
This also means that github will not render the files properly.
You can either generate the HTML output yourself or check (https://pa-pyrus.github.io/ubernet/).

## Available Hosts ##
These API calls are at least available on `http://uberent.com` and `https://uberent.com`.
There is also `https://uberdevent.com` for which you probably need special credentials.

The file `cacert.pem` contains the CA certificate needed to verify the identity of `https://uberent.com`.
You only need it if your certificate store doesn't already have the *Go Daddy Root Certificate Authority - G2* certificate.

## Authentication ##
In order to use most of the service endpoints described here, you need to have a valid session ticket.
Session tickets are requested from `/GC/Authenticate`.
They are a rather large string identifying your current session.
This string needs to be passed as the value of the `X-Authorization` HTTP request header for most calls.

## Miscellaneous ##
This section details various endpoints not belonging to a larger topic.

* `GameClient/GetNews` can be used to retrieve a certain number of news items for a specific game.
