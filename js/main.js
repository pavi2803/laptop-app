function validateForm() {
  var x = document.forms["myForm"]["cname"].value;
  if (x == "") {
    alert("Fill all the fields");
    return false;
  }
  var y = document.forms["myForm"]["tname"].value;
  if (y == "") {
    alert("Fill all the fields");
    return false;
  }
   var z = document.forms["myForm"]["rname"].value;
   if (z == "") {
    alert("Fill all the fields");
    return false;
  }
}
