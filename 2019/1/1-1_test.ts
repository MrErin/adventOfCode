const testData: number[] = [12, 14, 1969, 100756];

const results: number[] = testData.map(d => {
  return Math.floor(d / 3) - 2;
});

console.log(results);

const requiredToLaunch: number = results.reduce((a, b) => {
  return a + b;
});
console.log(requiredToLaunch);
