import {modules} from './data'

const testData2: number[] = [12, 14, 1969, 100756];

const calculateFuelForFuel = (fuelModules: number[]) => {
  let totalFuel: number = 0;

  fuelModules.map(m => {
    let currentFuelNeeded = Math.floor(m / 3 - 2);
    while (currentFuelNeeded >= 0) {
      totalFuel += currentFuelNeeded;
      currentFuelNeeded = Math.floor(currentFuelNeeded / 3 - 2);
    }
    // console.log(`m = ${m}, totalFuel = ${totalFuel}`)
  });
  console.log(totalFuel);
};

calculateFuelForFuel(testData2);
calculateFuelForFuel(modules);
