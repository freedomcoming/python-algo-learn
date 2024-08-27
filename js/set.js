let set = new Set([1, 4, 9]);
set.forEach((value, key) => console.log(key + ' : ' + value))





// 数组
let arr = [3, 5, 2, 2, 5, 5];
let unique1 = [...new Set(arr)]; // [3, 5, 2]

// 字符串
let str = "352255";
let unique2 = [...new Set(str)].join(""); // "352"



console.log(unique1, unique2);