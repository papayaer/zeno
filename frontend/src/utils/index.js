// 验证token过期
export function isValidJwt (jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false
  }
  const data = JSON.parse(atob(jwt.split('.')[1]))
  const exp = new Date(data.exp * 1000)
  const now = new Date()
  return now < exp
}

// 登录/注册from正则验证
export function fromValid(email,pw) {
  const emailRules = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/
  const pwRules = /^.*(?=.{8,15})(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#\$%\^&\*\?\(\),\.;:'"<>\{\}\[\]\\/\+-=\|_]).*$/
  if (emailRules.test(email) && pwRules.test(pw)) {
    return true
  }
  return false
}

// 格式化时间为(ago)
export function format(timestamp) {
  let t = parseInt((Date.parse(Date()) - Date.parse(timestamp)) / 6e4)
  return t < 60 ? parseInt(t) + "分钟前" : 60 <= t && t < 1440 ? parseInt(t / 60) + "小时前" : 1440 <= t && t < 43200 ? parseInt(t / 1440) + "天前" : 43200 <= t && t < 525600 ? parseInt(t / 43200) + "个月前" : parseInt(t / 525600) + "年前"
}

// 格式化为 昨天10:32 
export function formatTime() {
  C = function(t, e) {
    let s = {
        "M+": t.getMonth() + 1,
        "d+": t.getDate(),
        "h+": t.getHours(),
        "m+": t.getMinutes(),
        "s+": t.getSeconds(),
        "q+": Math.floor((t.getMonth() + 3) / 3),
        S: t.getMilliseconds()
    };
    /(y+)/.test(e) && (e = e.replace(RegExp.$1, (t.getFullYear() + "").substr(4 - RegExp.$1.length)));
    for (var n in s)
        new RegExp("(" + n + ")").test(e) && (e = e.replace(RegExp.$1, 1 === RegExp.$1.length ? s[n] : ("00" + s[n]).substr(("" + s[n]).length)));
    return e
  },
  b = function() {
    var t, e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : new Date, s = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "yyyy-MM-dd hh:mm:ss",
    n = window.parseInt;
    return "string" == typeof e && (e = new Date(e.replace(/-/g, "/"))),
    (t = ((new Date).getTime() - e.getTime()) / 1e3) < 60 ? "刚刚" : t < 3600 ? n(t / 60) + "分钟前" : t < 86400 ? n(t / 3600) + "小时前" : t < 172800 ? "昨天" + C(e, "hh:mm") : t < 259200 ? "前天" + C(e, "hh:mm") : t < 2592e3 ? n(t / 86400) + "天前" : C(e, s)
  }
}

// 瀑布流实现
export function mstool(params) {
  console.log(params)
}