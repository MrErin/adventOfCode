import { intcodeInput } from './data';
// const testData: number[] = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50];
const testData: number[] = [1, 1, 1, 4, 99, 5, 6, 0, 99];

const intcodeComputer = (intcodeProgram: number[]) => {
  let processedProgram: number[] = intcodeProgram;
  let instructionPointerAddress: number = 0;

  const increments = {
    1: 4,
    2: 4,
    99: 1,
  };

  processedProgram.map(d => {
    while (processedProgram[instructionPointerAddress] !== 99) {
      let noun = processedProgram[instructionPointerAddress + 1];
      let verb = processedProgram[instructionPointerAddress + 2];
      let output = processedProgram[instructionPointerAddress + 3];
      let opcode = processedProgram[instructionPointerAddress];

      if (opcode === 1) {
        processedProgram[output] =
          processedProgram[noun] + processedProgram[verb];
      } else if (opcode === 2) {
        processedProgram[output] =
          processedProgram[noun] * processedProgram[verb];
      } else {
        console.log('oops');
      }

      // console.log(opcode)
      instructionPointerAddress += increments[opcode];
    }
  });
  // console.log(processedProgram);
  console.log(processedProgram[0]);
};

// intcodeComputer(testData);
intcodeComputer(intcodeInput);
