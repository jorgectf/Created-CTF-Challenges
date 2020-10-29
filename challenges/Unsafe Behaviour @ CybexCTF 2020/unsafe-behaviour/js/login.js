var a = [
    'YXBwbHk=',
    'ZnVuY3Rpb24gKlwoICpcKQ==',
    'aW5pdA==',
    'aW5wdXQ=',
    'cmV0dXJuIChmdW5jdGlvbigpIA==',
    'e30uY29uc3RydWN0b3IoInJldHVybiB0aGlzIikoICk=',
    'Y29uc29sZQ==',
    'd2Fybg==',
    'ZGVidWc=',
    'aW5mbw==',
    'ZXhjZXB0aW9u',
    'dGFibGU=',
    'dHJhY2U=',
    'bG9n',
    'ZXJyb3I=',
    'Z2V0RWxlbWVudEJ5SWQ=',
    'dXNlcm5hbWU=',
    'cGFzc3dvcmQ=',
    'dmFsdWU=',
    'aW5jbHVkZXM=',
    'YWRtaW4=',
    'TG9naW4gc3VjY2Vzc2Z1bGx5',
    'd3JpdGU=',
    'bG9jYXRpb24=',
    'aGlkZGVuZmxhZy5odG1s',
    'c3RyaW5n',
    'Y29uc3RydWN0b3I=',
    'd2hpbGUgKHRydWUpIHt9',
    'Y291bnRlcg==',
    'bGVuZ3Ro',
    'Z2dlcg==',
    'Y2FsbA==',
    'ZGVidQ==',
    'c3RhdGVPYmplY3Q='
];
var b = function (c, d) {
    c = c - 0x0;
    var e = a[c];
    if (b['SDoTQa'] === undefined) {
        (function () {
            var g;
            try {
                var i = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');');
                g = i();
            } catch (j) {
                g = window;
            }
            var h = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
            g['atob'] || (g['atob'] = function (k) {
                var l = String(k)['replace'](/=+$/, '');
                var m = '';
                for (var n = 0x0, o, p, q = 0x0; p = l['charAt'](q++); ~p && (o = n % 0x4 ? o * 0x40 + p : p, n++ % 0x4) ? m += String['fromCharCode'](0xff & o >> (-0x2 * n & 0x6)) : 0x0) {
                    p = h['indexOf'](p);
                }
                return m;
            });
        }());
        b['SWvSjU'] = function (r) {
            var s = atob(r);
            var t = [];
            for (var u = 0x0, v = s['length']; u < v; u++) {
                t += '%' + ('00' + s['charCodeAt'](u)['toString'](0x10))['slice'](-0x2);
            }
            return decodeURIComponent(t);
        };
        b['TmAQcf'] = {};
        b['SDoTQa'] = !![];
    }
    var f = b['TmAQcf'][c];
    if (f === undefined) {
        e = b['SWvSjU'](e);
        b['TmAQcf'][c] = e;
    } else {
        e = f;
    }
    return e;
};
var e = function () {
    var g = !![];
    return function (h, i) {
        var j = g ? function () {
            if (i) {
                var k = i[b('0x0')](h, arguments);
                i = null;
                return k;
            }
        } : function () {
        };
        g = ![];
        return j;
    };
}();
(function () {
    e(this, function () {
        var l = new RegExp(b('0x1'));
        var m = new RegExp('\x5c+\x5c+\x20*(?:[a-zA-Z_$][0-9a-zA-Z_$]*)', 'i');
        var n = d(b('0x2'));
        if (!l['test'](n + 'chain') || !m['test'](n + b('0x3'))) {
            n('0');
        } else {
            d();
        }
    })();
}());
var c = function () {
    var o = !![];
    return function (p, q) {
        var r = o ? function () {
            if (q) {
                var s = q[b('0x0')](p, arguments);
                q = null;
                return s;
            }
        } : function () {
        };
        o = ![];
        return r;
    };
}();
var f = c(this, function () {
    var t = function () {
    };
    var u;
    try {
        var v = Function(b('0x4') + b('0x5') + ');');
        u = v();
    } catch (w) {
        u = window;
    }
    if (!u[b('0x6')]) {
        u[b('0x6')] = function (x) {
            var y = {};
            y['log'] = x;
            y[b('0x7')] = x;
            y[b('0x8')] = x;
            y[b('0x9')] = x;
            y['error'] = x;
            y[b('0xa')] = x;
            y[b('0xb')] = x;
            y[b('0xc')] = x;
            return y;
        }(t);
    } else {
        u[b('0x6')][b('0xd')] = t;
        u[b('0x6')][b('0x7')] = t;
        u[b('0x6')][b('0x8')] = t;
        u[b('0x6')][b('0x9')] = t;
        u[b('0x6')][b('0xe')] = t;
        u[b('0x6')][b('0xa')] = t;
        u['console'][b('0xb')] = t;
        u[b('0x6')][b('0xc')] = t;
    }
});
f();
function validate() {
    var z = document[b('0xf')](b('0x10'))['value'];
    var A = document['getElementById'](b('0x11'))[b('0x12')];
    if (z[b('0x13')]('\x27')) {
        alert('Attack\x20Detected');
    }
    if (z == b('0x14') && A == 'hunter2') {
        alert(b('0x15'));
        document[b('0x16')]('A');
        window[b('0x17')] = b('0x18');
        return ![];
    }
}
function d(B) {
    function C(D) {
        if (typeof D === b('0x19')) {
            return function (E) {
            }[b('0x1a')](b('0x1b'))[b('0x0')](b('0x1c'));
        } else {
            if (('' + D / D)[b('0x1d')] !== 0x1 || D % 0x14 === 0x0) {
                (function () {
                    return !![];
                }['constructor']('debu' + b('0x1e'))[b('0x1f')]('action'));
            } else {
                (function () {
                    return ![];
                }[b('0x1a')](b('0x20') + 'gger')[b('0x0')](b('0x21')));
            }
        }
        C(++D);
    }
    try {
        if (B) {
            return C;
        } else {
            C(0x0);
        }
    } catch (F) {
    }
}