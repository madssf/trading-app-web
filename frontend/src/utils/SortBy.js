function sortBy(property, dir){  
  return function(a,b){  
     if(a[property] > b[property])
        if (dir) {
        return 1;  
      } else
      return -1;
     else if(a[property] < b[property])  
     if (dir){
      return -1;  
     } else {
       return 1
     }
       
     return 0;  
  }  
}

export default sortBy;