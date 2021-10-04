function formSubmit(formdata) {
    event.preventDefault();
    $.ajax({
      type:"POST",
      url:"/shorten",
      data:  {
        alias: formdata['alias'].value,
        long_url: formdata['long_url'].value,
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
    },
      success: function(data){
          $('#output').css('display','block')
          let result=$('#output a');
          result.attr('href',data['result'])
          result.text(data['result'])
    }
    });
  }