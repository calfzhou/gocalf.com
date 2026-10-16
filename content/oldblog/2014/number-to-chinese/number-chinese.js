export function translateNumber(input) {
  let numberText = input.trim();
  if (numberText === '') return '';
  if (!/^-?[0-9]+$/.test(numberText)) throw new RangeError('请输入整数：仅允许数字，可选前导负号；不支持小数或科学计数法。');
  if (numberText.replace(/^-/, '').length > 52) throw new RangeError('最多支持 52 位数字（不含负号）。');
  const digits = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九'];
  const units = ['', '十', '百', '千'];
  const groups = ['', '万', '亿', '兆', '京', '垓', '杼', '穰', '溝', '澗', '正', '載', '極'];
  numberText = numberText.replace(/^0+/, '').replace(/^-0+/, '-');
  if (numberText === '' || numberText === '-') return '零';
  let result = '';
  if (numberText[0] === '-') { result = '负'; numberText = numberText.slice(1); }
  let groupIsZero = true;
  let needZero = false;
  for (let i = 0; i < numberText.length; i++) {
    const position = numberText.length - 1 - i;
    const digit = Number(numberText[i]);
    const unit = position % 4;
    const group = Math.floor(position / 4);
    if (digit !== 0) {
      if (needZero) result += '零';
      if (digit !== 1 || unit !== 1 || !groupIsZero || (group === 0 && needZero)) result += digits[digit];
      result += units[unit];
    }
    groupIsZero = groupIsZero && digit === 0;
    if (unit === 0 && !groupIsZero) result += groups[group];
    needZero = digit === 0 && (unit !== 0 || groupIsZero);
    if (unit === 0) groupIsZero = true;
  }
  return result;
}
