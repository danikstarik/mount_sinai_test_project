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

    var pict = document.getElementById("picture");        
    if (IsValid(userInput)){
      pict.src = "sad.png";}
    else{
      pict.src = "happy.png";} ;
   

                   
   }
         