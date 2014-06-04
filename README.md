# UberNet API #
This is an unofficial documentation of UberNet REST API calls.
By no means is it complete or entirely accurate.

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

### POST /GC/Authenticate ###
Request a session ticket.
You need to pass JSON-encoded Uber credentials.

#### Request Method ####
`POST`

#### Request Data ####
<dl>
  <dt><code>TitleId</code></dt>
  <dd><em>Assumption</em>: This identifies the context this request belongs to.
    <dl>
      <dt><code>4</code></dt>
      <dd>This is a request for <em>Planetary Annihilation</em>.</dd>
    </dl>
  </dd>

  <dt><code>AuthMethod</code></dt>
  <dd>The means of authentication.
    <dl>
      <dt><code>UberCredentials</code></dt>
      <dd>Use UberName and password for authentication.</dd>
    </dl>
  </dd>

  <dt><code>UberName</code></dt>
  <dd>The user requesting a session ticket.</dd>

  <dt><code>Password</code></dt>
  <dd>The user's password.</dd>
</dl>

#### Response Data ####
<dl>
  <dt><code>UberId</code>, <code>UberIdString</code></dt>
  <dd>The user's numeric ID on Ubernet.</dd>

  <dt><code>UberName</code></dt>
  <dd>The user requesting the session ticket.</dd>

  <dt><code>DisplayName</code>, <code>TitleDisplayName</code></dt>
  <dd>
    The user's current display name.
    The distinction between <code>DisplayName</code> and <code>TitleDisplayName</code> is not yet sufficiently clear.
  </dd>

  <dt><code>SessionTicket</code></dt>
  <dd>The session ticket used for further authorization.</dd>
</dl>

#### Return Codes ####
<dl>
  <dt><code>200</code></dt>
  <dd>The credentials are in order and a session ticket is returned.</dd>

  <dt><code>401</code></dt>
  <dd>
    The credentials are invalid.
    Response contains a corresponding error message.
  </dd>
</dl>

#### Example Request ####
```HTTP
POST /GC/Authenticate HTTP/1.1
Host: uberent.com
Content-Type: application/json

{
  "TitleId": 4,
  "AuthMethod": "UberCredentials",
  "UberName": "DummyUser",
  "Password": "DummyPass"
}
```

#### Example Response ####
```HTTP
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
```

## Miscellaneous ##
This section details various endpoints not belonging to a larger topic.

### GET /GameClient/News?TitleId=&lt;int&gt;&amp;Count=&lt;int&gt; ###
Retrieve news items for Uber Entertainment games.
This endpoint does **NOT** require authentication.

#### Request Method ####
`GET`

#### Query String Parameters ####
<dl>
  <dt><code>TitleId (int)</code></dt>
  <dd>The game you want to retrieve news items for.
    <dl>
      <dt><code>4</code></dt>
      <dd>Request news items for <em>Planetary Annihilation</em>.</dd>
    </dl>
  </dd>

  <dt><code>Count (int)</code></dt>
  <dd>
    The number of news items to retrieve.
    This parameter is <em>optional</em>.
    If it is omitted, all available news items are returned.
  </dd>
</dl>

#### Response Data ####
<dl>
  <dt><code>News</code><dt>
  <dd>An array of the following structure:
    <dl>
      <dt><code>Timestamp (string)</code></dt>
      <dd>
        The news item's time stamp.
        It's format is <code>%Y-%m-%d.%H:%M:%S</code> (cf. <code>strptime(3)</code>).
      </dd>

      <dt><code>Title (string)</code></dt>
      <dd>The news item's title.</dd>

      <dt><code>HtmlBody (string)</code></dt>
      <dd>The news item's full text, formatted in HTML</dd>
    </dl>
  </dd>
</dl>

#### Return Codes ####
<dl>
  <dt><code>200</code></dt>
  <dd>
    An array of news items is returned.
    If an invalid <code>TitleId</code> is specified, the array is empty.
  </dd>

  <dt><code>400</code></dt>
  <dd>
    The query string parameters are invalid.
    Response contains a corresponding error message.
  </dd>
</dl>

#### Example Request ####
```HTTP
GET /GameClient/GetNews?TitleId=4&Count=1 HTTP/1.1
Host: uberent.com
```

#### Example Response ####
```HTTP
HTTP/1.1 200 OK
Content-Type: application/json

{
  "News":
    [
      {
        "Timestamp": "2014-05-30.16:36:29",
        "Title": "Dummy News: Build 12345",
        "HtmlBody": "<div>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>"
      }
    ]
}
```
