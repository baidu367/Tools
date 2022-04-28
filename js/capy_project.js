

let getObjectValue = function (obj) {
    let newObj = new Object();
    for (let key in obj) {
        if (obj[key] == null) {
            newObj[key] = null;
            continue;
        }
        if (typeof obj[key] == "string" || typeof obj[key] == "number" || typeof obj[key] == "boolean") {
            newObj[key] = obj[key];
        } else if (typeof obj[key] == "function") {
            newObj[key] = "function";
        } else if (Array.isArray(obj[key])) {
            newObj[key] = obj[key];
        }

    }
    return newObj;
}

// 对象有 document，navigator，location，history，screen等。
let newObj = getObjectValue(window);
copy(newObj) // 粘贴的结果需要把 "function" 替换成 function (){}