import md5 from './md5.js';
// Original Kindle 4 recovery formula: uppercase, remove whitespace, append LF,
// MD5, then take hex characters 8–11 (zero-based slice 7..11).
export function normalizeSerial(serial) {
  return serial.toUpperCase().replace(/\s+/g, '');
}
export function kindlePassword(serial) {
  const normalized = normalizeSerial(serial);
  if (!normalized) return '';
  if (!/^[A-Z0-9]+$/.test(normalized)) throw new RangeError('请仅使用英文字母和数字，空格和换行会被忽略。');
  if (normalized.length > 128) throw new RangeError('序列号过长。');
  return 'fiona' + md5(normalized + '\n').slice(7, 11);
}
