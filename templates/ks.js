
// Calculating the time elapsed from 
// 1970-01-01 to up to now
  
// set the time
let past = new Date('2023-06-16 21:43:00');
console.log(past)
pas = past/(60*60*1000)
console.log('past',pas)
// assigning present time to now variable
let now = new Date();
console.log(now)
pasu = now/(60*60*1000)
console.log('pastu',pasu)

// console.log(no) 

let elapsed = (pas-pasu);
  
// by dividing by 1000 we will get 
// the time in seconds
console.log(elapsed/(60*60*1000));
