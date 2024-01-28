let a = 5, b = 6, c = 7, tmp, tmp2;
tmp = b;
b = a;
tmp2 = c;
c = tmp;
a = tmp2;

console.log(a);
console.log(b);
console.log(c);