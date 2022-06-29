//清除所有定时器

(function () {
    var gid = setInterval(clearAllInterval, 0);

    function clearAllInterval() {
        var id = setInterval(function () {
        }, 0);
        while (id > 0) {
            if (id !== gid) {
                clearInterval(id);
            }
            id--;
        }
    }
})();