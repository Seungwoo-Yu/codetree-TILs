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
    const a = Number(await read());

    console.log(a * 2 + 3);
    rl.close();
})()