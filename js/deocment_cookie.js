var cookis = ''

function new_cookie(cookie) {
    var cookieParts = cookie.split("; ");
    for (const cookiePartsKey in cookieParts) {
        var cookieP = cookieParts[cookiePartsKey].split("=");
        var cookieName = cookieP[0]
        var newCookieValue = cookieP[1]
        document.cookie = cookieName + "=" + newCookieValue;
    }
}
new_cookie(cookis)
