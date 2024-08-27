const p1 = new Promise((resolve, reject) => {
    resolve('hello');
})
    

const p2 = new Promise((resolve, reject) => {
    // throw new Error('报错了');
    resolve('hello');


})


Promise.all([p1, p2])
    .then(result => console.log(result))
    .catch(e => console.log(e))
    .finally(()=>{
        console.log(123);
    })
// ["hello", Error: 报错了]