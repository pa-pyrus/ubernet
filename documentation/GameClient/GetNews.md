# GET /GameClient/GetNews #
Retrieve news items for Uber Entertainment games.
This endpoint does **NOT** require authentication.

## Request Method ##
`GET`

## Query String Parameters ##
`TitleId (int)`
:   The game you want to retrieve news items for.

    `4`
    :   Request news items for *Planetary Annihilation*.

`Count (int)`
:   The number of news items to retrieve.
    This parameter is *optional*.
    If it is omitted, all available news items are returned.

## Response Data ##
`News (array)`
:   An array of the following structure:

    `Timestamp (string)`
    :   The news item's time stamp.
        Its format is `%Y-%m-%d.%H:%M:%S` (cf. `strptime(3)`).

    `Title (string)`
    :   The news item's title.

    `HtmlBody (string)`
    :   The news item's full text, formatted in HTML.

## Return Codes ##
`200`
:   An array of news items is returned.
    If an invalid `TitleId` is specified, the array is empty.

`400`
:   The query string paramters are invalid.
    Response contains a corresponding error message.

## Example Request ##
    :::HTTP
    GET /GameClient/GetNews?TitleId=4&Count=1 HTTP/1.1
    Host: uberent.com

## Example Response ##
    :::HTTP
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
