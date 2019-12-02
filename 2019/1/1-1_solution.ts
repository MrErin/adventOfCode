import { modules } from './data';

const results: number[] = modules.map(m => {
  return Math.floor(m / 3) - 2;
});

const requiredToLaunch: number = results.reduce((a, b) => {
  return a + b;
});

console.log(requiredToLaunch);
