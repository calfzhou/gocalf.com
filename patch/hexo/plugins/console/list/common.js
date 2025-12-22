"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.stringLength = void 0;
async function loadStripAnsi() {
    return (await import("strip-ansi")).default;
}
let strip_ansi_1;
(async () => {
    strip_ansi_1 = await loadStripAnsi();
})();
function stringLength(str) {
    str = (0, strip_ansi_1)(str);
    const len = str.length;
    let result = len;
    // Detect double-byte characters
    for (let i = 0; i < len; i++) {
        if (str.charCodeAt(i) > 255) {
            result++;
        }
    }
    return result;
}
exports.stringLength = stringLength;
//# sourceMappingURL=common.js.map
