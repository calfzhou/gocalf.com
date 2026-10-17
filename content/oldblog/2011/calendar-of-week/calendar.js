export const weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'];
export const months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'];
export const mod7 = value => ((value % 7) + 7) % 7;
export const isLeapYear = year => year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
export function daysInMonth(year, month) {
  return [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1];
}
export function calendarTrace(year, month, day) {
  if (!Number.isInteger(year) || year < 1 || year > 9999) throw new RangeError('请输入 1 到 9999 之间的年份。');
  if (!Number.isInteger(month) || month < 1 || month > 12) throw new RangeError('请选择月份。');
  if (!Number.isInteger(day) || day < 1 || day > daysInMonth(year, month)) throw new RangeError(`该月有 ${daysInMonth(year, month)} 天。`);
  const century = Math.floor(year / 100);
  const ending = year % 100;
  const yearSlot = ending + Math.floor(ending / 4);
  const centuryRow = [1, 3, 5, 0][century % 4];
  const yearColumn = yearSlot % 7;
  const letter = mod7(yearColumn - centuryRow);
  const monthRow = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5][month - 1] - (isLeapYear(year) && month <= 2 ? 1 : 0);
  const monthColumn = mod7(letter + monthRow);
  const dayRow = (day - 1) % 7;
  return { year, month, day, century, ending, yearSlot, centuryRow, yearColumn,
    letter, monthRow: mod7(monthRow), monthColumn, dayRow,
    weekday: weekdays[(dayRow + monthColumn) % 7], leap: isLeapYear(year) };
}
export function localToday() {
  const now = new Date();
  return { year: now.getFullYear(), month: now.getMonth() + 1, day: now.getDate() };
}
// Generate the gaps before leap-year endings rather than copying the old table's
// final-row alignment typo (96–99). Every year now occupies its arithmetic column.
export const yearRows = Array.from({ length: 18 }, () => Array(7).fill(null));
for (let ending = 0; ending < 100; ending++) {
  const slot = ending + Math.floor(ending / 4);
  yearRows[Math.floor(slot / 7)][slot % 7] = ending;
}
export const monthRows = [
  [{ month: 1 }, { month: 10 }], [{ month: 5 }],
  [{ month: 2, leap: true }, { month: 8 }],
  [{ month: 2 }, { month: 3 }, { month: 11 }], [{ month: 6 }],
  [{ month: 9 }, { month: 12 }], [{ month: 1, leap: true }, { month: 4 }, { month: 7 }]
];

// Coordinates are those of the original, continuous 17-column paper sheet.
export const centuryRows = [3, 0, null, 1, null, 2, null].map((residue, row) => residue === null ? [] : [
  { key: `cycle-${residue}`, label: residue ? `4n+${residue}` : '4n', value: null, residue, row: 19 + row, column: 1 },
  ...[15 + ((residue + 1) % 4), 19 + ((residue + 1) % 4)].map((value, index) =>
    ({ key: String(value), label: String(value), value, residue, row: 19 + row, column: 2 + index }))
]);
export const paperMonths = monthRows.flatMap((row, index) => row.map((item, column) => ({
  ...item, key: `${item.month}${item.leap ? '-prime' : ''}`, label: `${item.month}${item.leap ? '′' : ''}`,
  row: 19 + index, column: 11 + column
})));
export function paperSelection(date) {
  const trace = calendarTrace(date.year, date.month, date.day);
  const centuries = centuryRows.flat();
  const century = centuries.find(cell => cell.value === trace.century) ||
    { ...centuries.find(cell => cell.value === null && cell.residue === trace.century % 4), value: trace.century };
  const month = paperMonths.find(cell => cell.month === trace.month && !!cell.leap === (trace.leap && trace.month <= 2));
  return { century, ending: trace.ending, month, day: trace.day };
}
export function paperPath({ century, ending, month, day }) {
  const path = new Set();
  const junctions = new Set();
  const horizontal = (row, from, to) => { for (let col = from; col <= to; col++) path.add(`${row}:${col}`); };
  const vertical = (col, from, to) => { for (let row = from; row <= to; row++) path.add(`${row}:${col}`); };
  const yearSlot = ending === null ? null : ending + Math.floor(ending / 4);
  const yearColumn = yearSlot === null ? null : 4 + yearSlot % 7;
  if (century) horizontal(century.row, century.column, yearColumn ?? 10);
  if (yearColumn !== null) vertical(yearColumn, 1 + Math.floor(yearSlot / 7), century?.row ?? 25);
  const yearKey = century && yearColumn !== null ? mod7(yearColumn - 4 - (century.row - 19)) : null;
  const monthColumn = month && yearKey !== null ? 4 + mod7(yearKey + month.row - 19) : null;
  if (yearKey !== null) junctions.add(`${century.row}:${yearColumn}`);
  if (month) horizontal(month.row, monthColumn ?? 4, month.column);
  if (monthColumn !== null) junctions.add(`${month.row}:${monthColumn}`);
  let weekday = null;
  if (day !== null) {
    const row = 26 + (day - 1) % 7;
    horizontal(row, monthColumn ?? 4, 11 + Math.floor((day - 1) / 7));
    if (monthColumn !== null) {
      vertical(monthColumn, month.row, row);
      junctions.add(`${row}:${monthColumn}`);
      weekday = weekdays[mod7(day - 1 + monthColumn - 4)];
    }
  }
  let warning = '';
  if (century && ending !== null && month) {
    const year = (century.value ?? century.residue) * 100 + ending;
    if (month.month <= 2 && !!month.leap !== isLeapYear(year)) {
      warning = `该年应选择 ${month.month}${isLeapYear(year) ? '′（闰年月份）' : '（不带撇号的月份）'}。`;
    } else if (day !== null && day > daysInMonth(year, month.month)) {
      warning = `该月有 ${daysInMonth(year, month.month)} 天；高亮路径对应的日期无效。`;
    }
  }
  return { path, junctions, yearKey, weekday, warning };
}
