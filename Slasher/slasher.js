function slasher(arr, howMany) {
  
  /*
    Return the remaining elements of an array after chopping off  n  
    elements from the head. The head means the beginning 
    of the array, or the zeroth index.
  */
  
   var trash = [];
  
  // if howMany is greater than length of arr
  if ( howMany > arr.length )
  {
      return [];
  }
  
  // if howMany is less than zero
  if ( howMany < 0 )
  {
    return false;    
  }
  
  // if howMany is zero
  if ( howMany === 0 )
  {
    return arr;    
  }
  
  // Get useless elements 
  trash = arr.slice(0, howMany);
  
  // Remove useless elements from arr
  arr.splice(trash, howMany);
  
  // Return remaining elements
  return arr;
  
}