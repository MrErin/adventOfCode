import { intcodeInput as data } from './data';

export default class IntcodeComputer {
  constructor() {
    const intcodeInput = data;
    let solution1 = this.processCodeList(intcodeInput);
    console.log(solution1[0]);
    let solution2 = this.findNounAndVerb(intcodeInput, 19690720);
    console.log(solution2);
  }

  public increments = {
    1: 4,
    2: 4,
    99: 1,
  };
  public processCodeList(memory: number[]): number[] {
    let result = [...memory];
    let instructionPointerAddress = 0;

    result.map(() => {
      while (result[instructionPointerAddress] !== 99) {
        let noun = result[instructionPointerAddress + 1];
        let verb = result[instructionPointerAddress + 2];
        let output = result[instructionPointerAddress + 3];
        let opCode = result[instructionPointerAddress];
        switch (opCode) {
          case 1: {
            result[output] = result[noun] + result[verb];
            break;
          }
          case 2: {
            result[output] = result[noun] * result[verb];
            break;
          }
          case 99: {
            return result;
          }
          default: {
            return result;
          }
        }
        instructionPointerAddress += this.increments[opCode];
      }
    });

    return result;
  }

  public findNounAndVerb(memory: number[], result: number): number {
    let noun = 1;
    let verb = 1;
    let currentResultAttempt = 0;

    while (true) {
      while (currentResultAttempt < result) {
        noun += 1;
        let newInstruction = [...memory];
        newInstruction[1] = noun;
        newInstruction[2] = verb;
        currentResultAttempt = this.processCodeList(newInstruction)[0];
        if (currentResultAttempt === result) {
          return 100 * noun + verb;
        }
      }
      verb += 1;
      noun = 1;
      currentResultAttempt = 0;
    }
    return 0;
  }
}

new IntcodeComputer();
