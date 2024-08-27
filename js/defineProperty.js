const obj = {}
Object.defineProperty(obj, 'foo', {
    get() {
        let val = "test"
        console.log(`get foo:${val}`);
        return val
    },
    set(newVal) {
        console.log(`new val ${newVal}`);
    }
})



obj.foo
obj.foo = 'new'
obj.bar  = '新属性'