document.addEventListener("DOMContentLoaded", function() {
    var dropdown = document.getElementById("model-type");
    dropdown.addEventListener("change", function() {
        if (dropdown.value === "question-answer") {
          document.getElementById("question-answer-container").classList.remove("hidden")
        } else {
            document.getElementById("question-answer-container").classList.add("hidden")
        }
      });
})

function handleKeyDown(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        send();
    }
}
var inputTextArea = document.getElementById('input');
inputTextArea.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key == 'Enter') {
        send();
    }
});



function sendUserMessage(prompt_content, model){

    displaySettings(model)
    let content = 
        {
            "prompt": prompt_content,
            "model": model,
            "guid": guid,
        }
    let config = 
        {
            type: "POST",
            url:  '/prompt/',
            data: content,
            dataType: 'json',
            success: displayResponseMessage
        };
        
    $.ajax(config);
}
function send(){
    console.log('guid in send', guid)
    let prompt_content = document.getElementById("input").value
    let model_type = document.getElementById("model-type").value
    let model = "gpt3.5"
    if(model_type == "question-answer"){
        model = document.getElementById("question-answer").value
    }

    
    document.getElementById("input").value = ""
    console.log('prompt_content', prompt_content)
    displayUserMessage(prompt_content)
    response = sendUserMessage(prompt_content, model, guid)
}

function displaySettings(model){
    model = "Selected Model: " + model
    let settings = document.createElement('div')
    settings.classList.add("settings-output")
    settings.innerHTML = model
    let settingsContainer = document.createElement('div')
    settingsContainer.classList.add("settings-output-container")
    settingsContainer.appendChild(settings)
    document.getElementById("output").appendChild(settingsContainer)
}

function displayResponseMessage(input){
    
    console.log('input', input)
    let newMessage = document.createElement("p");
    newMessage.classList.add("response-message");
    newMessage.innerHTML = input.answer;
    console.log('newMessage', newMessage)

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    console.log('messageContainer', messageContainer)

    let output = document.getElementById("output");
    console.log('output', output)
    output.appendChild(messageContainer);
}

function displayUserMessage(userMessage){
   
    let newMessage = document.createElement("p");
    newMessage.classList.add("user-message");
    newMessage.innerHTML = userMessage;
    console.log('newMessage', newMessage)

    let messageContainer = document.createElement("div");
    messageContainer.classList.add("user-message-container")
    messageContainer.appendChild(newMessage);
    console.log('messageContainer', messageContainer)

    let output = document.getElementById("output");
    console.log('output', output)
    output.appendChild(messageContainer);

}