function getPoint() {
    const x = 1;
    const y = 10;
    return { x, y };
}

console.log(getPoint());



const o = {
    method() {
        return "Hello!";
    }
};


console.log(o.method());

let lastWord = 'last word';

const a = {
  'first word': 'hello',
  [lastWord]: 'world'
};

console.log(a[lastWord] );


// assign 用法

const target = { a: 1, b: 1 };

const source1 = { b: 2, c: 2 };
const source2 = { c: 3 };

Object.assign(target, source1, source2);
// target // {a:1, b:2, c:3}
console.log(target);