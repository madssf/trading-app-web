export default function nthIndex(str, pat, n){
  var L= str.length, i= -1;
  while(n-- && i++<L){
      i= str.indexOf(pat, i);
      if (i < 0) break;
  }
  return i;
}

/*
var s= "XYZ 123 ABC 456 ABC 789 ABC";

nthIndex(s,'ABC',3)

returned value: (Number)
24

*/