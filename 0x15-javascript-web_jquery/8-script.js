$(document).ready(function(){
    $.get( "https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
     jQuery.each(data.results, function(index, value) {
      $("ul#list_movies").append("<li>"+value.title+"</li>");
       });
        })
   });
   