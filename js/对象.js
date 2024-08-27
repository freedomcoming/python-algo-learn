let user = {
    name: "John",
    age: 30,
    "likes birds": true  // 多词属性名必须加引号
};


console.log(user.name);
console.log(user["likes birds"])



console.log("name" in user); // true

let user2 = { name: 'John' };

let admin = user2;

admin.name = 'Pete'; // 通过 "admin" 引用来修改

console.log(user2.name); // 'Pete'，修改能通过 "user" 引用看到

let user3 = { name: "John" };

Object.assign(user3, { name: "Pete" });

console.log(user3);