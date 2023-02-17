$(document).on('submit', '#post-form', function(e){
        e.preventDefault();
        
        $.ajax({
            type: 'POST',
            url: "song/"+songId+"/",
            data: {
                song_title: $('#id_song_title').val(),
                description: $('#id_description').val(),
                mp3: $('#id_mp3').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data){
            },
        });
    });
