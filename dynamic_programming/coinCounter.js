const coins = [1,5,10,25,50,100]
const coinCounterHandler = (cents) => {
  if (cents < 0) throw new Error("pick a better number")

  const coinCounter = (cents, memo = []) => {
    if (memo[cents]) return memo[cents];
    if (cents === 0) return 0;
    if (cents < 0) return Number.MAX_SAFE_INTEGER;
    if (coins.includes(cents)) return 1;
  
    // check value of adding a coin
    memo[cents] = 1 + Math.min(...coins.map(coin => {
        return coinCounter(cents - coin, memo);
      })
    )
    return memo[cents];
  } 
  return coinCounter(cents);
}


for(let i = -1; i<=10;i++) {
  console.log(coinCounterHandler(i));
}
