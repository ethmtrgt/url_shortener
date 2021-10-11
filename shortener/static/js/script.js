function formSubmit(formdata) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: "/shorten",
        data: {
            alias: formdata['alias'].value,
            long_url: formdata['long_url'].value,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(data){
            if (data.status == 'success'){
                $('#output').css('display','block')
                let result = $('#output a');
                let shortUrl = `${window.location.origin}/${data.result}`
                result.attr('href', shortUrl)
                result.text(shortUrl)
            } else {
                alert(data.message)
            }
        }
    });
}