const input = [356261, 846303];
// const input = [111110, 111112]

const passwordCriteriaChecker = (password, p2 = false) => {
  let increases = true;
  const matches = password.match(/(\d)\1+/g);

  if (password.length !== 6) {
    return false;
  }
  if (!matches) {
    return false;
  }

  if (p2 && !matches.map(match => match.length).includes(2)) {
    return false;
  }

  [...password].reduce((acc, val) => {
    if (increases && parseInt(acc) > parseInt(val)) {
      increases = false;
    }
    return val;
  });

  if (!increases) {
    return false;
  }
  return true;
};

const countPasswordContenders = (min: number, max: number) => {
  const matches_p1 = new Set();
  const matches_p2 = new Set();

  for (let i = min; i <= max; i++) {
    if (passwordCriteriaChecker(i.toString())) matches_p1.add(i.toString());
    if (passwordCriteriaChecker(i.toString(), true))
      matches_p2.add(i.toString());
  }
  console.log(matches_p1.size);
  console.log(matches_p2.size);
};

countPasswordContenders(input[0], input[1]);

// const passwordContenders = (min: number, max: number) => {
//   let contenders: number[] = [];
//   let doubles: number[] = [];

//   for (let i = min + 1; i < max; i++) {
//     let iString = i.toString()
//     let doublesMatch = iString.match(/(\d)\1+/g)
//     let increases = true
//     [...iString].reduce((acc, val) => {
//       if (increases && parseInt(acc) > parseInt(val)) increases = false)
//     return val
//   })
//   if (!increases) return false

//   // [...i.toString()].reduce

//   console.log(`total number of contenders is ${contenders.length}`);
// };

// passwordContenders(input[0], input[1]);

//   let increases: number[] = [];
//   let digits = i.toString();
//   for (let d = 0; d < digits.length; d++) {
//     let pass = true;
//       if (digits[d] < digits[d - 1]) {
//         pass = false;
//         return;
//       }
//     if (pass && d === digits.length -1){
//       increases.push(Number(digits))
//     }
//   }
//   console.log(increases)
