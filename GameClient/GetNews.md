# GET /GameClient/GetNews?TitleId=&lt;int&gt;&amp;Count=&lt;int&gt; #
Retrieve news items for Uber Entertainment games.
This endpoint does **NOT** require authentication.

## Request Method ##
`GET`

## Query String Parameters ##
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

## Response Data ##
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

## Return Codes ##
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

## Example Request ##
```HTTP
GET /GameClient/GetNews?TitleId=4&Count=1 HTTP/1.1
Host: uberent.com
```

## Example Response ##
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
