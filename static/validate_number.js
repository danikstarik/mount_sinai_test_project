  function IsValid(str)
  {    // this regular expression checks validity of the input
       var regex = /^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$/;
       if (str.match(regex) == null){
               return true;
             }
            else{
             return false;
                  }
                 
  }
  function test()
  {
    var userInput = document.getElementById("userInput").value;

    var pict_happy = document.getElementById("picture_happy");   
    var pict_sad = document.getElementById("picture_sad");      
    if (IsValid(userInput)){
      pict_sad.style.display = 'block';
      pict_happy.style.display = 'none';
    }
    else{
      pict_happy.style.display = 'block';
      pict_sad.style.display = 'none';} ;
   

                   
   }
         