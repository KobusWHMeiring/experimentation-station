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

function send(){
    let prompt_content = document.getElementById("input").value
    let model_type = document.getElementById("model-type").value
    let model = "gpt3.5"
    if(model_type == "question-answer"){
        model = document.getElementById("question-answer").value
    }

    
    document.getElementById("input").value = ""
    console.log('prompt_content', prompt_content)
    displayUserMessage(prompt_content)
    response = sendUserMessage(prompt_content, model)
}

function sendUserMessage(prompt_content, model){

    let content = 
        {
            "prompt": prompt_content,
            "model": model
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