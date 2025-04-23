$(document).ready(function () {
    // Initialize animation
    $('.siri-message').textillate({
        autoStart: false,
        in: {
            effect: 'fadeInUp',
            delay: 50,
            sync: true
        },
        out: {
            effect: 'fadeOutUp',
            delay: 50,
            sync: true
        }
    });

    // Expose this to Python
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $('#SiriWave').prop('hidden', false); // Show the SiriWave section
        $('.siri-message').text(message).textillate('start');
    }

    //display hood
    eel.expose(ShowHood)
    function ShowHood(){
        $('#oval').attr("hidden",false);
        $('#SiriWave').attr("hidden",true);

    }

    eel.expose(senderText)
    function senderText(message){
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() != ""){
            chatbox.innerHTML += `<div class="row justify-content-end mb-4">
            <div class="width-size">
            <div class="sender_message">${message}</div>
            </div>
            `
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }

    eel.expose(receiverText)
    function receiverText(message){
        var chatbox = document.getElementById("chat-canvas-body");
        if (message.trim() != ""){
            chatbox.innerHTML += `<div class="row justify-content-start mb-4">
            <div class="width-size">
            <div class="reciever_message">${message}</div>
            </div>
            `
            chatbox.scrollTop = chatbox.scrollHeight;
        }
    }
});
