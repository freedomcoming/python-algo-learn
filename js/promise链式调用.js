


const test_promise_chain = ()=>{
    return new Promise((resolve,reject)=>{


        resolve("test")
    })
}



test_promise_chain().then(r=>{
    console.log(r);
    return r // 必须return res 下面才能链式调用
}).then(r=>{
    console.log(r);
})
