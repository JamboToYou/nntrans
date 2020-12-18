
$(document).ready(function(){
    $("#gtltranslate").click(function(){
      var $this = $(this);
      $this.attr('disabled', true);
      var value = document.getElementById('gtlsource').value;
      var src = document.getElementById('gtlfrom').value;
      var dest = document.getElementById('gtlto').value;
      var passw = "2956684590ru85";
  
      setTimeout(function() {$this.attr('disabled', false);}, 9000);
      $.post("/gtranslate/",
      {
          text  : value,
          gfrom : src,
          gto   : dest,
          key   : passw
      },
      function(data, status){
          var resultBody = document.getElementById("gtlresults_body");
          resultBody.value = data;
          $this.attr('disabled', false);
      });
    }); 
  });
  

// _ga=GA1.2.59477960.1607621274; _ym_uid=1607621274948142885; _ym_d=1607621274; _gid=GA1.2.1364996764.1607793101; _ym_isad=1; sc_is_visitor_unique=rx12015710.1607793102.0EC744C31B2C4FB29D49074E9D8A1D81.3.3.3.3.3.3.2.1.1
// _ga=GA1.2.59477960.1607621274; _ym_uid=1607621274948142885; _ym_d=1607621274; _gid=GA1.2.1364996764.1607793101; _ym_isad=1; sc_is_visitor_unique=rx12015710.1607799034.0EC744C31B2C4FB29D49074E9D8A1D81.4.4.3.3.3.3.2.1.1; _gat=1
// Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36