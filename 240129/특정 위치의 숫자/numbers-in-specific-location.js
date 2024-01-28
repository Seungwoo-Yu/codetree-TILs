const readline = require('readline')
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})

async function read() {
  return await new Promise(resolve => {
    rl.once('line', (line) => {
      resolve(line);
    });
  })
}

(async () => {
  const set = String(await read()).split(' ');


  console.log(Number(set[2]) + Number(set[4]) + Number(set[9]));
  rl.close();
})();