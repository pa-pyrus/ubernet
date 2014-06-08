# POST /GC/Authenticate #
Request a session ticket.
You need to pass JSON-encoded Uber credentials.

## Request Method ##
`POST`

## Request Data ##
`TitleId (int)`
:   *Assumption*: This identifies the context this request belongs to.

    `4`
    :   This is a request for *Planetary Annihilation*.

`AuthMethod (string`)
:   The means of authentication.

    `UberCredentials`
    :   Use UberName and password for authentication.

`UberName (string)`
:   The user requesting a session ticket.

`Password (string)`
:   The user's password.

## Response Data ##
`UberId (int)`, `UberIdString (string)`
:   The user's numeric ID on Ubernet.

`UberName (string)`
:   The user requesting the session ticket.

`DisplayName (string)`, `TitleDisplayName (string)`
:   The user's current display name.
    The distinction between `DisplayName` and `TitleDisplayName` is not yet sufficiently clear.

`SessionTicket (string)`
:   The session ticket used for further authorization.

## Return Codes ##
`200`
:   The credentials are in order and a session ticket is returned.

`401`
:   The credentials are invalid.
    Response contains a corresponding error message.

## Example Request ##
    :::HTTP
    POST /GC/Authenticate HTTP/1.1
    Host: uberent.com
    Content-Type: application/json

    {
      "TitleId": 4,
      "AuthMethod": "UberCredentials",
      "UberName": "DummyUser",
      "Password": "DummyPass"
    }

#### Example Response ####
    :::HTTP
    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "UberId": 0123456789,
      "UberIdString": "0123456789",
      "UberName": "DummyUser",
      "DisplayName": "DummyUser",
      "TitleDisplayName": "DummyUser",
      "SessionTicket": "0123456789ABCDEF-0123456789ABCDEF0-1-2-3456789ABCDEF01-23456789ABCDEF01.23456789ABCDEF01"
    }
